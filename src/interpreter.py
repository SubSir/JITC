import sys
import mmap
import struct, ctypes
from antlr4 import *
from llvmparser.llvmLexer import llvmLexer
from llvmparser.llvmParser import llvmParser
from llvmparser.llvmVisitor import llvmVisitor


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

    def visitModule(self, ctx):
        main_ = None
        for child in ctx.children:
            if isinstance(child, llvmParser.FunctionContext):
                name = child.Global_var().getText()
                basic_blocks = child.basic_block()
                self.static_functions[name] = StaticFunction(name, basic_blocks)
                self.functions[name] = child
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
        self.visit(next_block)

    def visitBinary_op(self, ctx):
        inst = ctx.getText()
        print(inst)
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
            self.stack[-1].variables[ctx.params().parameter(0).getText()] = val
            return

        args = {}
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
        self.stack.append(Function(func_name, args))
        self.visit(self.functions[func_name])
        if ctx.Privatevariable():
            self.stack[-2].variables[ctx.Privatevariable().getText()] = self.stack[
                -1
            ].return_value
        self.stack.pop()

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
            self.stack[-1].jmp_block = ctx.Label().getText()

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


def main():
    input_stream = (
        FileStream(sys.argv[1]) if len(sys.argv) > 1 else InputStream(sys.stdin.read())
    )

    lexer = llvmLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = llvmParser(stream)

    tree = parser.module()
    interpreter = LLVMInterpreter()
    interpreter.visit(tree)


if __name__ == "__main__":
    main()
