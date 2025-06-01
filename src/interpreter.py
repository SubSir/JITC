import sys
import rename
import mmap
import struct, ctypes
from antlr4 import *
from llvmparser.llvmLexer import llvmLexer
from llvmparser.llvmParser import llvmParser
from llvmparser.llvmVisitor import llvmVisitor
import builtins

import hex
from trampoline import get_trampoline_address, set_global_callback
import func2mem

CALL_TIMES = 2


def create_shared_memory(size):
    if sys.platform.startswith("win"):
        return mmap.mmap(-1, size, access=mmap.ACCESS_WRITE)
    elif sys.platform.startswith("linux"):
        return mmap.mmap(-1, size, prot=mmap.PROT_READ | mmap.PROT_WRITE)


class Function:
    def __init__(self, name="", variables={}):
        self.name = name
        self.variables = variables
        self.jmp_block = None
        self.last_block = None
        self.return_value = None


class StaticFunction:
    def __init__(self, name="", basic_blocks=None):
        self.name = name
        self.basic_blocks = {}
        self.next_block = {}
        if basic_blocks:
            next_block = None
            for block in basic_blocks[::-1]:
                self.basic_blocks[block.Label().getText()] = block
                self.next_block[block.Label().getText()] = next_block
                next_block = block.Label().getText()
        else:
            self.next_block = {}
            self.basic_blocks = {}


class LLVMInterpreter(llvmVisitor):
    def __init__(self):
        self.functions = {}
        self.stack = []
        self.static_functions = {}
        self.strmap = {}
        self.globalvariables = {}
        self.sizemap = {}
        self.count_map = {}
        self.mem = func2mem.Stack()
        self.func_call = {}
        self.func_asmed = set()
        self.func_asm = {}
        set_global_callback(self.function_call)
        hex.trampoline = get_trampoline_address() - 8
        hex.function_map["print"] = 0
        hex.function_map["println"] = 1
        hex.function_map["printstr"] = 2
        hex.function_map["input"] = 3
        self.func_index = ["print", "println", "printstr", "input"]

    def visitModule(self, ctx):
        main_ = None
        for child in ctx.children:
            if isinstance(child, llvmParser.FunctionContext):
                name = child.Global_var().getText()
                self.func_call[name] = self.call_record(child)
                basic_blocks = child.basic_block()
                self.static_functions[name] = StaticFunction(name, basic_blocks)
                self.functions[name] = child
                hex.function_map[name[1:]] = len(self.func_index)
                self.func_index.append(name[1:])
                if name == "@main":
                    main_ = child
            elif isinstance(child, llvmParser.String_declareContext):
                self.strmap[
                    child.Global_var().getText()
                ] = child.StringLiteral().getText()[1:-1]
            elif isinstance(child, llvmParser.GlobalarrayContext):
                name = child.Global_var().getText()
                size = int(child.INTEGER().getText())
                mm = create_shared_memory(16 * size)
                self.globalvariables[name] = mm
                mm.write(b"\x00" * (16 * size))
            elif isinstance(child, llvmParser.GlobalvariableContext):
                name = child.Global_var().getText()
                val = child.constant().getText()
                if val == "null":
                    val = 0
                else:
                    val = int(val)
                mm = create_shared_memory(16)
                self.globalvariables[name] = mm
                self.memory_write(mm, val)
            elif isinstance(child, llvmParser.TypedelcareContext):
                name = child.Privatevariable().getText()
                self.sizemap[name] = len(child.types())

        if main_:
            self.stack.append(Function("@main"))
            self.visit(main_)
            print(f"Main function exited with code {self.stack[-1].return_value}")
        else:
            raise Exception("No main function found")

    def call_record(self, ctx: llvmParser.FunctionContext):
        func_name = ctx.Global_var().getText()
        call_set = set()
        for block in ctx.basic_block():
            for instr in block.instruction():
                if instr.call():
                    name = instr.call().Global_var().getText()
                    if name != func_name:
                        call_set.add(name)
        return call_set

    def function_call(self, func_id, a1, a2, a3, a4, a5, a6, sp):
        # print("we are here")
        func_name = "@" + self.func_index[func_id]
        if func_name == "@print":
            print(a1, end="")
            return 0
        elif func_name == "@println":
            print(a1)
            return 0
        elif func_name == "@printstr":
            print(self.strmap[a1], end="")
            return 0
        elif func_name == "@input":
            val = input()
            return int(val)
        if func_name not in self.count_map:
            self.count_map[func_name] = 0
        args = {}
        arg_list = []
        for i in range(len(self.functions[func_name].params().parameter())):
            value = eval(f"a{i+1}")
            val_name = (
                self.functions[func_name]
                .params()
                .parameter()[i]
                .Privatevariable()
                .getText()
            )
            args[val_name] = value
            arg_list.append(value)
        if func_name in self.func_asmed:
            val = self.func_asm[func_name].exec(arg_list, sp - 16)
        elif (
            func_name in self.count_map
            and self.count_map[func_name] > CALL_TIMES
            and "@printstr" not in self.func_call[func_name]
        ):
            code = self.getTextWithSpaces(self.functions[func_name])
            global_info = {}
            for name, value in self.globalvariables.items():
                global_info[name] = ctypes.addressof(ctypes.c_uint64.from_buffer(value))
            for name, value in self.func_asm.items():
                global_info[name[1:]] = value.mem_address
            func = func2mem.code2func(code, global_info)
            val = func.exec(arg_list, sp - 16)
            self.func_asmed.add(func_name)
            self.func_asm[func_name] = func

        else:
            self.count_map[func_name] += 1
            self.stack.append(Function(func_name, args))
            self.visit(self.functions[func_name])
            val = self.stack[-1].return_value
            self.stack.pop()
        return int(val)

    def memory_write(self, mm, val, addr=0):
        packed = struct.pack("<q", val)
        mm.seek(addr)
        mm.write(packed)

    def visitFunction(self, ctx):
        self.visit(ctx.basic_block(0))

    def visitGlobalvariable(self, ctx):
        name = ctx.Global_var().getText()
        var_type = ctx.type_().getText()
        value = (
            ctx.constant().getText()
            if ctx.constant()
            else ctx.string_constant().getText()
        )
        self.global_vars[name] = {"type": var_type, "value": value}

    def visitBasic_block(self, ctx):
        self.stack[-1].jmp_block = None
        for instr in ctx.instruction():
            self.visit(instr)
        if self.stack[-1].jmp_block:
            func_name = self.stack[-1].name
            next_block = self.static_functions[func_name].basic_blocks[
                self.stack[-1].jmp_block
            ]
        else:
            name = ctx.Label().getText()
            func_name = self.stack[-1].name
            next_block = self.static_functions[func_name].next_block[name]
            if not next_block:
                return
            next_block = self.static_functions[func_name].basic_blocks[next_block]
        self.stack[-1].last_block = ctx.Label().getText()
        self.visit(next_block)

    def visitBinary_op(self, ctx):
        dest = ctx.Privatevariable().getText()
        op = ctx.bin_op().getText()
        value1 = self.resolve_value(ctx.value(0))
        value2 = self.resolve_value(ctx.value(1))

        if op == "add":
            result = value1 + value2
        elif op == "sub":
            result = value1 - value2
        elif op == "mul":
            result = value1 * value2
        elif op == "sdiv":
            result = value1 // value2
        elif op == "srem":
            result = value1 % value2
        elif op == "shl":
            result = value1 << value2
        elif op == "ashr":
            result = value1 >> value2
        elif op == "and":
            result = value1 & value2
        elif op == "or":
            result = value1 | value2
        elif op == "xor":
            result = value1 ^ value2
        else:
            raise Exception(f"Unsupported binary operation: {op}")

        self.stack[-1].variables[dest] = result

    def visitInstruction(self, ctx):
        for child in ctx.children:
            self.visit(child)

    def visitRet(self, ctx):
        if ctx.value():
            return_value = self.resolve_value(ctx.value())
            self.stack[-1].return_value = return_value

    def resolve_value(self, value_ctx):
        if value_ctx.Privatevariable():
            return self.stack[-1].variables[value_ctx.Privatevariable().getText()]
        elif value_ctx.Global_var():
            name = value_ctx.Global_var().getText()
            if name in self.globalvariables:
                return ctypes.addressof(
                    ctypes.c_uint64.from_buffer(self.globalvariables[name])
                )
            return name
        elif value_ctx.constant():
            return int(value_ctx.constant().getText())
        raise Exception("Unsupported value type")

    def visitCall(self, ctx):
        func_name = ctx.Global_var().getText()
        if func_name == "@print":
            print(self.resolve_value(ctx.params().parameter(0)), end="")
            return
        elif func_name == "@println":
            print(self.resolve_value(ctx.params().parameter(0)))
            return
        elif func_name == "@printstr":
            print(self.strmap[self.resolve_value(ctx.params().parameter(0))], end="")
            return
        elif func_name == "@input":
            val = input()
            self.stack[-1].variables[ctx.Privatevariable().getText()] = int(val)
            return

        if func_name not in self.count_map:
            self.count_map[func_name] = 0
        args = {}
        arg_list = []
        if ctx.params() != None:
            i = 0
            for param in ctx.params().parameter():
                value = self.resolve_value(param)
                val_name = (
                    self.functions[func_name]
                    .params()
                    .parameter()[i]
                    .Privatevariable()
                    .getText()
                )
                i += 1
                args[val_name] = value
                arg_list.append(value)
        if func_name in self.func_asmed:
            val = self.func_asm[func_name].exec(arg_list, self.mem.stack_top)
        elif (
            func_name in self.count_map
            and self.count_map[func_name] > CALL_TIMES
            and "@printstr" not in self.func_call[func_name]
        ):
            code = self.getTextWithSpaces(self.functions[func_name])
            global_info = {}
            for name, value in self.globalvariables.items():
                global_info[name] = ctypes.addressof(ctypes.c_uint64.from_buffer(value))
            for name, value in self.func_asm.items():
                global_info[name[1:]] = value.mem_address
            func = func2mem.code2func(code, global_info)
            val = func.exec(arg_list, self.mem.stack_top)
            self.func_asmed.add(func_name)
            self.func_asm[func_name] = func

        else:
            self.count_map[func_name] += 1
            self.stack.append(Function(func_name, args))
            self.visit(self.functions[func_name])
            val = self.stack[-1].return_value
            self.stack.pop()
        if ctx.Privatevariable():
            self.stack[-1].variables[ctx.Privatevariable().getText()] = val

    def visitCompare(self, ctx):
        val = None
        cond = ctx.cond().getText()
        value0 = self.resolve_value(ctx.value(0))
        value1 = self.resolve_value(ctx.value(1))
        match cond:
            case "eq":
                val = value0 == value1
            case "ne":
                val = value0 != value1
            case "slt":
                val = value0 < value1
            case "sgt":
                val = value0 > value1
            case "sle":
                val = value0 <= value1
            case "sge":
                val = value0 >= value1
        if val:
            val = 1
        else:
            val = 0
        self.stack[-1].variables[ctx.Privatevariable().getText()] = val

    def visitBranch(self, ctx):
        value = 1
        if ctx.value():
            value = self.resolve_value(ctx.value())

        if value == 1:
            self.stack[-1].jmp_block = ctx.Label(0).getText()
        else:
            self.stack[-1].jmp_block = ctx.Label(1).getText()

    def readfrommem(self, ptr):
        ptr = ctypes.cast(ptr, ctypes.POINTER(ctypes.c_int64))
        return ptr.contents.value

    def visitLoad(self, ctx):
        ptr = self.resolve_value(ctx.var())
        value = self.readfrommem(ptr)
        self.stack[-1].variables[ctx.Privatevariable().getText()] = value

    def visitStore(self, ctx):
        ptr = self.resolve_value(ctx.var())
        ptr = ctypes.cast(ptr, ctypes.POINTER(ctypes.c_int64))
        value = self.resolve_value(ctx.value())
        ptr.contents.value = value

    def visitGetelementptr(self, ctx):
        var = self.resolve_value(ctx.var())
        offset = 0
        value1 = self.resolve_value(ctx.value(0))
        if ctx.ptrtype().Privatevariable():
            value1 *= self.sizemap[ctx.ptrtype().Privatevariable().getText()]
        offset += 8 * value1
        if len(ctx.value()) > 1:
            value2 = self.resolve_value(ctx.value(1))
            offset += 8 * value2
        self.stack[-1].variables[ctx.Privatevariable().getText()] = var + offset

    def visitPhi(self, ctx):
        for i in range(len(ctx.value())):
            if self.stack[-1].last_block == ctx.Label(i).getText():
                self.stack[-1].variables[
                    ctx.Privatevariable().getText()
                ] = self.resolve_value(ctx.value(i))
                break

    def getTextWithSpaces(self, ctx):
        result = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if child.getChildCount() == 0:
                result.append(child.getText())
            else:
                result.append(self.getTextWithSpaces(child))
        return " ".join(result)


def main():
    code = sys.stdin.read()
    input_stream = InputStream(rename.main(code))

    lexer = llvmLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = llvmParser(stream)

    tree = parser.module()
    interpreter = LLVMInterpreter()
    interpreter.visit(tree)


if __name__ == "__main__":
    main()
