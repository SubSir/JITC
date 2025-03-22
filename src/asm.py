import sys
import copy
from antlr4 import InputStream, CommonTokenStream
import antlr4
from llvmparser.llvmListener import llvmListener
from llvmparser.llvmLexer import llvmLexer
from llvmparser.llvmParser import llvmParser
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.tree.Tree import ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener


class Interval:
    beg = -1
    end = -1

    def __init__(self, beg=-1, end=-1) -> None:
        self.beg = beg
        self.end = end


class RegUseList:
    name = ""
    reg_list = []
    len_ = 0

    def __init__(self, name="", reg_list=[]):
        self.name = name
        self.reg_list = reg_list
        for i in reg_list:
            self.len_ += i.end - i.beg + 1

    def __lt__(self, other):
        return self.len_ < other.len_


class Block:
    name = ""
    in_ = set()
    out = set()
    def_ = set()
    use = set()

    def __init__(self, name="", in_=set(), out=set(), def_=set(), use=set()) -> None:
        self.name = name
        self.in_ = in_
        self.out = out
        self.def_ = def_
        self.use = use


class Mylistener3(llvmListener):
    func_list = []
    return_str = ".text\n"
    enter_label = ""
    enter_function = ""
    data = ".data\n"
    variable_map = {}
    variable_cnt = 0
    label_map = {}
    tmp_branch_cnt = 0
    tmp_store = {}
    reg_map = {
        "s0": [],
        "s1": [],
        "s2": [],
        "s3": [],
        "s4": [],
        "s5": [],
        "s6": [],
        "s7": [],
        "s8": [],
        "s9": [],
        "s10": [],
        "s11": [],
        "a0": [],
        "a1": [],
        "a2": [],
        "a3": [],
        "a4": [],
        "a5": [],
        "a6": [],
        "a7": [],
        "t3": [],
        "t4": [],
        "t5": [],
        "t6": [],
        "gp": [],
        "tp": [],
    }

    danger_reg = [
        "a0",
        "a1",
        "a2",
        "a3",
        "a4",
        "a5",
        "a6",
        "a7",
        "t3",
        "t4",
        "t5",
        "t6",
        "gp",
        "tp",
    ]

    def enterRet(self, ctx: llvmParser.RetContext):
        if ctx.value() != None:
            value = ctx.value()
            name = ctx.value().getText()
            if value.Privatevariable() != None:
                self.loadword(self.variable_map[name], "_")
            elif value.Global_var() != None:
                self.return_str += "\tla _, " + name[1:] + "\n"
            else:
                if name == "null":
                    name = "0"
                self.return_str += "\tli _, " + name + "\n"
        self.return_str += "\tld ra, 0(sp)\n"
        for i in self.tmp_store:
            self.loadword(self.tmp_store[i], i)
        if self.variable_cnt > 2047:
            self.return_str += "\tli t0, " + str(self.variable_cnt) + "\n"
            self.return_str += "\tadd sp, sp, t0\n"
        else:
            self.return_str += "\taddi sp, sp, " + str(self.variable_cnt) + "\n"
        self.return_str += "\tret\n"

    def loadword(self, index, name: str = "t0"):
        if isinstance(index, str):
            if name != index:
                self.return_str += "\tmv " + name + ", " + index + "\n"
            return
        if index > 2047 or index < -2048:
            self.return_str += "\tli ra, " + str(index) + "\n"
            self.return_str += "\tadd ra, sp, ra\n"
            self.return_str += "\tld " + name + ", 0(ra)\n"
            return
        self.return_str += "\tld " + name + ", " + str(index) + "(sp)\n"

    def saveword(self, index: int, name: str = "t0"):
        if isinstance(index, str):
            if name != index:
                self.return_str += "\tmv " + index + ", " + name + "\n"
            return
        if index > 2047 or index < -2048:
            self.return_str += "\tli ra, " + str(index) + "\n"
            self.return_str += "\tadd ra, sp, ra\n"
            self.return_str += "\tsd " + name + ", 0(ra)\n"
            return
        self.return_str += "\tsd " + name + ", " + str(index) + "(sp)\n"

    def params_decode(self, code: llvmParser.ParamsContext):
        params = code.parameter()
        mv_list = []
        add_str = ""
        for i in range(min(len(params), 7)):
            param = params[i]
            if param.Global_var() != None:
                name = param.Global_var().getText()[1:]
                if name[0] == ".":
                    add_str += "\tla a" + str(i) + ", " + name + "\n"
                else:
                    add_str += "\tld a" + str(i) + ", " + name + "\n"
            elif param.Privatevariable() != None:
                name = param.Privatevariable().getText()
                index = self.variable_map[name]
                # self.loadword(index, "a" + str(i))
                if index != "a" + str(i):
                    mv_list.append([index, "a" + str(i)])
            else:
                name = param.constant().getText()
                if name == "null":
                    name = "0"
                add_str += "\tli a" + str(i) + ", " + name + "\n"
        while len(mv_list) > 0:
            while True:
                flag = True
                dele = []
                for i in mv_list:
                    check = False
                    for j in mv_list:
                        if i[1] == j[0]:
                            check = True
                            break
                    if not check:
                        self.loadword(i[0], i[1])
                        dele.append(i)
                        flag = False
                if flag:
                    break
                for i in dele:
                    mv_list.remove(i)
            dele = []
            for i in mv_list:
                conflict = []
                for j in mv_list:
                    if i[1] == j[0]:
                        conflict = j
                        break
                self.loadword(i[1], "t0")
                self.loadword(i[0], i[1])
                mv_list.append(["t0", conflict[1]])
                dele.append(conflict)
                dele.append(i)
                break
            for i in dele:
                mv_list.remove(i)
        self.return_str += add_str
        if len(params) > 7:
            self.return_str += "\taddi sp, sp, -" + str((len(params) - 7) * 8) + "\n"
            for i in range(len(params) - 7):
                param = params[i + 7]
                if param.Global_var() != None:
                    name = param.Global_var().getText()[1:]
                    if name[0] == ".":
                        self.return_str += "\tla t0, " + name + "\n"
                    else:
                        self.return_str += "\tld t0, " + name + "\n"
                    t0 = "t0"
                elif param.Privatevariable() != None:
                    name = param.Privatevariable().getText()
                    index = self.variable_map[name]
                    if isinstance(index, str):
                        t0 = index
                    else:
                        t0 = "t0"
                        self.loadword(self.variable_map[name])
                else:
                    name = param.constant().getText()
                    if name == "null":
                        name = "0"
                    self.return_str += "\tli t0, " + name + "\n"
                    t0 = "t0"
                self.saveword(i * 8, t0)

    def enterCall(self, ctx: llvmParser.CallContext):
        i = 0
        if ctx.params() != None:
            self.params_decode(ctx.params())
            i = len(ctx.params().parameter())
        self.return_str += "\tcall " + ctx.Global_var().getText()[1:] + "\n"
        if i > 7:
            self.return_str += "\taddi sp, sp, " + str((i - 7) * 8) + "\n"
        if ctx.Privatevariable() != None:
            self.saveword(self.variable_map[ctx.Privatevariable().getText()], "a0")

    def enterBinary_op(self, ctx: llvmParser.Binary_opContext):
        value1 = ctx.value(0)
        value2 = ctx.value(1)
        if value1.Privatevariable() != None:
            name2 = self.variable_map[value1.Privatevariable().getText()]
            if not isinstance(name2, str):
                self.loadword(name2, "t1")
                t1 = "t1"
            else:
                t1 = name2
        elif value1.Global_var() != None:
            self.return_str += "\tla t1, " + value1.Global_var().getText() + "\n"
            t1 = "t1"
        else:
            name = value1.getText()
            if name == "null":
                name = "0"
            self.return_str += "\tli t1, " + name + "\n"
            t1 = "t1"
        if value2.Privatevariable() != None:
            name2 = self.variable_map[value2.Privatevariable().getText()]
            if not isinstance(name2, str):
                self.loadword(name2, "t2")
                t2 = "t2"
            else:
                t2 = name2
        elif value2.Global_var() != None:
            self.return_str += "\tla t2, " + value2.Global_var().getText() + "\n"
            t2 = "t2"
        else:
            name = value2.getText()
            if name == "null":
                name = "0"
            op = ctx.bin_op().getText()
            if (
                int(name) >= -2048
                and int(name) <= 2047
                and op != "sub"
                and op != "mul"
                and op != "sdiv"
                and op != "srem"
                and op != "shl"
                and op != "ashr"
            ):
                t2 = name
                name2 = self.variable_map[ctx.Privatevariable().getText()]
                if not isinstance(name2, str):
                    t0 = "t0"
                else:
                    t0 = name2
                if op == "add":
                    self.return_str += "\taddi " + t0 + ", " + t1 + ", " + t2 + "\n"
                # elif op == "sub":
                #     self.return_str += "\tli t2, " + name + "\n"
                #     t2 = "t2"
                #     self.return_str += "\tsub " + t0 + ", " + t1 + ", " + t2 + "\n"
                # elif op == "mul":
                #     self.return_str += "\tmuli " + t0 + ", " + t1 + ", " + t2 + "\n"
                # elif op == "sdiv":
                #     self.return_str += "\tdivi " + t0 + ", " + t1 + ", " + t2 + "\n"
                # elif op == "srem":
                #     self.return_str += "\tremi " + t0 + ", " + t1 + ", " + t2 + "\n"
                # elif op == "shl":
                #     self.return_str += "\tslli " + t0 + ", " + t1 + ", " + t2 + "\n"
                # elif op == "ashr":
                #     self.return_str += "\tsrai " + t0 + ", " + t1 + ", " + t2 + "\n"
                elif op == "and":
                    self.return_str += "\tandi " + t0 + ", " + t1 + ", " + t2 + "\n"
                elif op == "or":
                    self.return_str += "\tori " + t0 + ", " + t1 + ", " + t2 + "\n"
                elif op == "xor":
                    self.return_str += "\txori " + t0 + ", " + t1 + ", " + t2 + "\n"
                else:
                    sys.exit(1)
                if t0 == "t0":
                    self.saveword(name2)
                return
            self.return_str += "\tli t2, " + name + "\n"
            t2 = "t2"
        op = ctx.bin_op().getText()
        name2 = self.variable_map[ctx.Privatevariable().getText()]
        if not isinstance(name2, str):
            t0 = "t0"
        else:
            t0 = name2
        if op == "add":
            self.return_str += "\tadd " + t0 + ", " + t1 + ", " + t2 + "\n"
        elif op == "sub":
            self.return_str += "\tsub " + t0 + ", " + t1 + ", " + t2 + "\n"
        elif op == "mul":
            self.return_str += "\tmul " + t0 + ", " + t1 + ", " + t2 + "\n"
        elif op == "sdiv":
            self.return_str += "\tdiv " + t0 + ", " + t1 + ", " + t2 + "\n"
        elif op == "srem":
            self.return_str += "\trem " + t0 + ", " + t1 + ", " + t2 + "\n"
        elif op == "shl":
            self.return_str += "\tsll " + t0 + ", " + t1 + ", " + t2 + "\n"
        elif op == "ashr":
            self.return_str += "\tsra " + t0 + ", " + t1 + ", " + t2 + "\n"
        elif op == "and":
            self.return_str += "\tand " + t0 + ", " + t1 + ", " + t2 + "\n"
        elif op == "or":
            self.return_str += "\tor " + t0 + ", " + t1 + ", " + t2 + "\n"
        elif op == "xor":
            self.return_str += "\txor " + t0 + ", " + t1 + ", " + t2 + "\n"
        else:
            sys.exit(1)
        if t0 == "t0":
            self.saveword(name2)

    def enterBranch(self, ctx: llvmParser.BranchContext):
        if ctx.value() != None:
            value = ctx.value()
            if value.Privatevariable() != None:
                name2 = self.variable_map[value.Privatevariable().getText()]
                if not isinstance(name2, str):
                    self.loadword(name2)
                    t0 = "t0"
                else:
                    t0 = name2
            else:
                name = value.getText()
                if name == "null":
                    name = "0"
                self.return_str += "\tli t0, " + name + "\n"
                t0 = "t0"
            label1 = self.enter_label + ctx.Label(0).getText()
            label2 = self.enter_label + ctx.Label(1).getText()
            tmp_br = "tmp_br" + str(self.tmp_branch_cnt)
            self.return_str += "\tbnez " + t0 + ", " + tmp_br + "\n"
            self.return_str += "\tj " + label2 + "\n"
            self.return_str += tmp_br + ":\n"
            self.return_str += "\tj " + label1 + "\n"
            self.tmp_branch_cnt += 1
            if label1 not in self.label_map:
                self.label_map[label1] = (
                    "\tj " + self.enter_function + ctx.Label(0).getText() + "\n"
                )
            else:
                self.label_map[label1] += (
                    "\tj " + self.enter_function + ctx.Label(0).getText() + "\n"
                )
            if label2 not in self.label_map:
                self.label_map[label2] = (
                    "\tj " + self.enter_function + ctx.Label(1).getText() + "\n"
                )
            else:
                self.label_map[label2] += (
                    "\tj " + self.enter_function + ctx.Label(1).getText() + "\n"
                )
            return
        label = self.enter_label + ctx.Label(0).getText()
        self.return_str += "\tj " + label + "\n"
        if label not in self.label_map:
            self.label_map[label] = (
                "\tj " + self.enter_function + ctx.Label(0).getText() + "\n"
            )
        else:
            self.label_map[label] += (
                "\tj " + self.enter_function + ctx.Label(0).getText() + "\n"
            )

    def enterLoad(self, ctx: llvmParser.LoadContext):
        var = ctx.var()
        if var.Privatevariable() != None:
            name2 = self.variable_map[var.Privatevariable().getText()]
            if isinstance(name2, str):
                t1 = name2
            else:
                self.loadword(self.variable_map[var.Privatevariable().getText()], "t1")
                t1 = "t1"
            name2 = self.variable_map[ctx.Privatevariable().getText()]
            if isinstance(name2, str):
                self.return_str += "\tld " + name2 + ", 0(" + t1 + ")\n"
            else:
                self.return_str += "\tld t0, 0(" + t1 + ")\n"
                self.saveword(name2)
            return
        name = var.Global_var().getText()[1:]
        name2 = self.variable_map[ctx.Privatevariable().getText()]
        if isinstance(name2, str):
            self.return_str += "\tld " + name2 + ", " + name + "\n"
            return
        self.return_str += "\tld t0, " + name + "\n"
        self.saveword(name2)

    def enterGetelementptr(self, ctx: llvmParser.GetelementptrContext):
        value = ctx.value()
        if value.Privatevariable() != None:
            name2 = self.variable_map[value.Privatevariable().getText()]
            if isinstance(name2, str):
                t2 = name2
            else:
                t2 = "t2"
                self.loadword(name2, "t2")
            self.return_str += "\tslli t2, " + t2 + ", 2\n"
        else:
            name = value.getText()
            if name == "null":
                name = "0"
            name = str(int(name) * 8)
            self.return_str += "\tli t2, " + name + "\n"
        var = ctx.var()
        if var.Privatevariable() != None:
            name2 = self.variable_map[var.Privatevariable().getText()]
            if isinstance(name2, str):
                t1 = name2
            else:
                t1 = "t1"
                self.loadword(name2, "t1")
            name2 = self.variable_map[ctx.Privatevariable().getText()]
            if isinstance(name2, str):
                self.return_str += "\tadd " + name2 + ", " + t1 + ", t2\n"
            else:
                self.return_str += "\tadd t0, " + t1 + ", t2\n"
                self.saveword(name2)
            return
        name = var.Global_var().getText()[1:]
        self.return_str += "\tld t0, " + name + "\n"
        name2 = self.variable_map[ctx.Privatevariable().getText()]
        if isinstance(name2, str):
            self.return_str += "\tadd " + name2 + ", t0, t2\n"
        else:
            self.return_str += "\tadd t0, t0, t2\n"
            self.saveword(name2)

    def enterStore(self, ctx: llvmParser.StoreContext):
        value = ctx.value()
        if value.Privatevariable() != None:
            name2 = self.variable_map[value.Privatevariable().getText()]
            if isinstance(name2, str):
                t1 = name2
            else:
                t1 = "t1"
                self.loadword(name2, "t1")
        elif value.Global_var() != None:
            self.return_str += "\tla t1, " + value.Global_var().getText()[1:] + "\n"
            t1 = "t1"
        else:
            name = value.getText()
            if name == "null":
                name = "0"
            self.return_str += "\tli t1, " + name + "\n"
            t1 = "t1"
        var = ctx.var()
        if var.Privatevariable() != None:
            name2 = self.variable_map[var.Privatevariable().getText()]
            if isinstance(name2, str):
                t0 = name2
            else:
                t0 = "t0"
                self.loadword(name2)
            self.return_str += "\tsd " + t1 + ", 0(" + t0 + ")\n"
            return
        name = var.Global_var().getText()[1:]
        self.return_str += "\tlui t0, %hi(" + name + ")\n"
        self.return_str += "\tsd " + t1 + ", %lo(" + name + ")(t0)\n"

    def enterCompare(self, ctx: llvmParser.CompareContext):
        value1 = ctx.value(0)
        if value1.Privatevariable() != None:
            name2 = self.variable_map[value1.Privatevariable().getText()]
            if isinstance(name2, str):
                t1 = name2
            else:
                t1 = "t0"
                self.loadword(name2, "t0")
        elif value1.Global_var() != None:
            self.return_str += "\tla t0, " + value1.Global_var().getText()[1:] + "\n"
            t1 = "t0"
        else:
            name = value1.getText()
            if name == "null":
                name = "0"
            self.return_str += "\tli t0, " + name + "\n"
            t1 = "t0"
        value2 = ctx.value(1)
        if value2.Privatevariable() != None:
            name2 = self.variable_map[value2.Privatevariable().getText()]
            if isinstance(name2, str):
                t2 = name2
            else:
                t2 = "t2"
                self.loadword(name2, "t2")
        elif value2.Global_var() != None:
            self.return_str += "\tla t2, " + value2.Global_var().getText()[1:] + "\n"
            t2 = "t2"
        else:
            name = value2.getText()
            if name == "null":
                name = "0"
            self.return_str += "\tli t2, " + name + "\n"
            t2 = "t2"
        op = ctx.cond().getText()
        privatevariable = ctx.Privatevariable()
        name = self.variable_map[privatevariable.getText()]
        if not isinstance(name, str):
            t0 = "t0"
        else:
            t0 = name
        if op == "eq":
            self.return_str += "\txor t0, " + t1 + ", " + t2 + "\n"
            self.return_str += "\tseqz " + t0 + ", t0\n"
        elif op == "ne":
            self.return_str += "\txor t0, " + t1 + ", " + t2 + "\n"
            self.return_str += "\tsnez " + t0 + ", t0\n"
        elif op == "slt":
            self.return_str += "\tslt " + t0 + ", " + t1 + ", " + t2 + "\n"
        elif op == "sgt":
            self.return_str += "\tslt " + t0 + ", " + t2 + ", " + t1 + "\n"
        elif op == "sle":
            self.return_str += "\tslt t0, " + t2 + ", " + t1 + "\n"
            self.return_str += "\txori " + t0 + ", t0, 1\n"
        elif op == "sge":
            self.return_str += "\tslt t0, " + t1 + ", " + t2 + "\n"
            self.return_str += "\txori " + t0 + ", t0, 1\n"
        else:
            sys.exit(1)
        if t0 == "t0":
            self.saveword(name)

    def enterPhi(self, ctx: llvmParser.PhiContext):
        for i in range(len(ctx.Label())):
            label1 = (
                self.enter_function
                + ctx.Label(i).getText()
                + self.enter_label[len(self.enter_function) :]
            )
            value1 = ctx.value(i)
            moved = False
            to = self.variable_map[ctx.Privatevariable().getText()]
            if not isinstance(to, str):
                to = "t0"
            value1_str = ""
            if value1.Privatevariable() != None:
                index = self.variable_map[value1.Privatevariable().getText()]
                if isinstance(index, str):
                    t0 = index
                else:
                    if index > 2047 or index < -2048:
                        value1_str += "\tli ra, " + str(index) + "\n"
                        value1_str += "\tadd ra, sp, ra\n"
                        value1_str += "\tld " + to + ", 0(ra)\n"
                        if to != "t0":
                            moved = True
                    else:
                        value1_str += "\tld " + to + ", " + str(index) + "(sp)\n"
                        if to != "t0":
                            moved = True
                    t0 = "t0"
            elif value1.Global_var() != None:
                value1_str += (
                    "\tla " + to + ", " + value1.Global_var().getText()[1:] + "\n"
                )
                if to != "t0":
                    moved = True
                t0 = "t0"
            else:
                name = value1.getText()
                if name == "null":
                    name = "0"
                value1_str += "\tli " + to + ", " + name + "\n"
                if to != "t0":
                    moved = True
                t0 = "t0"
            index = self.variable_map[ctx.Privatevariable().getText()]
            str1 = value1_str
            if not moved:
                if isinstance(index, str):
                    str1 += "\tmv " + index + ", " + t0 + "\n"
                else:
                    if index > 2047 or index < -2048:
                        str1 += "\tli ra, " + str(index) + "\n"
                        str1 += "\tadd ra, sp, ra\n"
                        str1 += "\tsd " + t0 + ", 0(ra)\n"
                    else:
                        str1 += "\tsd " + t0 + ", " + str(index) + "(sp)\n"
            if label1 not in self.label_map:
                self.label_map[label1] = str1
            else:
                str_ = self.label_map[label1]
                lines = str_.splitlines()
                tmp_str = ""
                i = 0
                while i < len(lines):
                    if lines[i].startswith("\tj"):
                        break
                    tmp_str += lines[i] + "\n"
                    i += 1
                tmp_str += str1
                while i < len(lines):
                    tmp_str += lines[i] + "\n"
                    i += 1
                self.label_map[label1] = tmp_str

    def enterBasic_block(self, ctx: llvmParser.Basic_blockContext):
        name = ctx.Label().getText()
        self.enter_label = self.enter_function + name
        self.return_str += self.enter_label + ":\n"

    def conflict_graph(
        self,
        ctx: llvmParser.Basic_blockContext,
        list: list,
        define_map: dict,
        block_index: dict,
        danger_zone: list,
        phi_map: list,
    ):
        block_index.append((ctx.Label().getText(), len(list)))
        list.append(-1)
        for i in ctx.instruction():
            if i.call() != None:
                call = i.call()
                if call.params() != None:
                    for j in call.params().parameter():
                        if j.Privatevariable() != None:
                            list.append(j.Privatevariable().getText())
                if call.Privatevariable() != None:
                    list.append("-" + call.Privatevariable().getText())
                    define_map[call.Privatevariable().getText()] = len(list) - 1
                list.append("")
                danger_zone.append(len(list) - 1)
            elif i.ret() != None:
                ret = i.ret()
                if ret.value() != None:
                    value = ret.value()
                    if value.Privatevariable() != None:
                        list.append(value.Privatevariable().getText())
            elif i.binary_op() != None:
                binary_op = i.binary_op()
                for j in binary_op.value():
                    if j.Privatevariable() != None:
                        list.append(j.Privatevariable().getText())
                list.append("-" + binary_op.Privatevariable().getText())
                define_map[binary_op.Privatevariable().getText()] = len(list) - 1
            elif i.branch() != None:
                branch = i.branch()
                if branch.value() != None:
                    value = branch.value()
                    if value.Privatevariable() != None:
                        list.append(value.Privatevariable().getText())
            elif i.load() != None:
                load = i.load()
                var = load.var()
                if var.Privatevariable() != None:
                    list.append(var.Privatevariable().getText())
                list.append("-" + load.Privatevariable().getText())
                define_map[load.Privatevariable().getText()] = len(list) - 1
            elif i.store() != None:
                value = i.store().value()
                var = i.store().var()
                if var.Privatevariable() != None:
                    list.append(var.Privatevariable().getText())
                if value.Privatevariable() != None:
                    list.append(value.Privatevariable().getText())
            elif i.getelementptr() != None:
                value = i.getelementptr().value()
                var = i.getelementptr().var()
                if value.Privatevariable() != None:
                    list.append(value.Privatevariable().getText())
                if var.Privatevariable() != None:
                    list.append(var.Privatevariable().getText())
                list.append("-" + i.getelementptr().Privatevariable().getText())
                define_map[i.getelementptr().Privatevariable().getText()] = (
                    len(list) - 1
                )
            elif i.compare() != None:
                compare = i.compare()
                for j in compare.value():
                    if j.Privatevariable() != None:
                        list.append(j.Privatevariable().getText())
                list.append("-" + compare.Privatevariable().getText())
                define_map[compare.Privatevariable().getText()] = len(list) - 1
            elif i.phi() != None:
                phi = i.phi()
                for j in phi.value():
                    if j.Privatevariable() != None:
                        list.append(j.Privatevariable().getText())
                list.append("-" + phi.Privatevariable().getText())
                define_map[phi.Privatevariable().getText()] = len(list) - 1
                if ctx.Label().getText() not in phi_map:
                    phi_map[ctx.Label().getText()] = {}
                for i in range(len(phi.value())):
                    phi_map[ctx.Label().getText()][phi.value(i).getText()] = phi.Label(
                        i
                    ).getText()

    def _traverse_blocks(self, bm: dict, queue: list, from_: str, visited: list):
        visited.append(from_)
        for j in bm[from_][1]:
            if j not in visited:
                self._traverse_blocks(bm, queue, j, visited)
        queue.append(from_)

    def bfs(self, graph: dict, visited: list, start: str):
        queue = []
        queue.append(start)
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                for neighbor in graph[vertex][1]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    def merge_intervals(self, intervals):
        intervals.sort(key=lambda x: x.beg)

        merged = []
        for interval in intervals:
            if not merged or merged[-1].end < interval.beg:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged

    def has_intersection(self, list1, list2):
        list1.sort(key=lambda x: x.beg)
        list2.sort(key=lambda x: x.beg)

        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            a, b = list1[i], list2[j]
            if a.end >= b.beg and a.beg <= b.end:
                return True
            if a.end < b.end:
                i += 1
            else:
                j += 1

        return False

    def reverse_graph(self, bm: dict):
        reversed_bm = {}
        for node, (_, out_neighbors) in bm.items():
            if node not in reversed_bm:
                reversed_bm[node] = ([], [])
            for neighbor in out_neighbors:
                if neighbor not in reversed_bm:
                    reversed_bm[neighbor] = ([], [])
                reversed_bm[neighbor][1].append(node)
        return reversed_bm

    def dfs(self, node: str, graph: dict, visited: set):
        visited.add(node)

        for neighbor in graph[node][1]:
            if neighbor not in visited:
                self.dfs(neighbor, graph, visited)

    def search_circle(self, bm: dict, reversed_bm: dict, from_: str):
        visited_original = set()
        self.dfs(from_, bm, visited_original)

        visited_reversed = set()
        self.dfs(from_, reversed_bm, visited_reversed)

        common_nodes = visited_original.intersection(visited_reversed)

        return common_nodes

    def block_register(
        self,
        name: str,
        block_name: str,
        block_index: list,
        circle: list,
        regusemap: dict,
        block_index_map: dict,
        final_end: int,
        be=-1,
        en=-1,
    ):
        list2 = []
        for i in circle:
            if block_name in i:
                list2 = circle[i]
                break
        beg = -1
        end = -1
        p = block_index_map[block_name]
        beg = block_index[p][1]
        if p == len(block_index) - 1:
            end = final_end
        else:
            end = block_index[p + 1][1]
        if len(list2) == 0:
            if be != -1:
                beg = be
            if en != -1:
                end = en
        reguse = Interval(beg=beg, end=end)
        if name not in regusemap:
            regusemap[name] = []
        if reguse in regusemap[name]:
            return
        regusemap[name].append(reguse)
        for t in list2:
            beg = t.beg
            end = t.end
            reguse = Interval(beg=beg, end=end)
            if reguse not in regusemap[name]:
                regusemap[name].append(reguse)

    def update_block(
        self,
        name: str,
        block_map: dict,
        block_stream_map: dict,
        phi_map: map,
        phi_map2: map,
    ) -> bool:
        if name not in block_stream_map:
            return True
        me = block_stream_map[name]
        in_ = set()
        out = set()
        for i in block_map[name][1]:
            tmp = set()
            for j in block_stream_map[i].in_:
                if (
                    i in phi_map
                    and j in phi_map[i]
                    and phi_map[i][j] != name
                    and j not in block_stream_map[i].out
                ):
                    tmp.add(j)
            out = out | (block_stream_map[i].in_ - tmp)
        if name in phi_map2:
            for i in phi_map2[name]:
                j = phi_map2[name][i]
                for k in j:
                    if k in block_stream_map[i].def_:
                        out.add(k)
        in_ = (out | me.use) - me.def_
        if out == me.out and in_ == me.in_:
            return True
        me.out = out
        me.in_ = in_
        return False

    def enterFunction(self, ctx: llvmParser.FunctionContext):
        return_type = ctx.type_().getText()
        params = []
        for parameter in ctx.params().parameter():
            params.append(parameter.type_().getText())
        self.func_list.append((return_type, params))
        list = []
        visited = []
        define_map = {}
        block_map = {}
        danger_zone = []

        for i in ctx.basic_block():
            to_list = []
            for j in i.instruction():
                if j.branch() != None:
                    for k in j.branch().Label():
                        to_list.append(k.getText())
            block_map[i.Label().getText()] = [i, to_list]
        queue = []
        entry = ctx.basic_block(0).Label().getText()
        self._traverse_blocks(block_map, queue, entry, visited)
        queue = queue[::-1]
        # circle = {}
        for i in block_map:
            if len(block_map[i][1]) == 0:
                end = i
                break
        rbm = self.reverse_graph(block_map)
        bfs_queue = []
        self.bfs(rbm, bfs_queue, end)
        block_index = []
        phi_map = {}
        for i in queue:
            self.conflict_graph(
                block_map[i][0], list, define_map, block_index, danger_zone, phi_map
            )
        block_index_map = {}
        for i in range(len(block_index)):
            block_index_map[block_index[i][0]] = block_index[i][1]
        block_index_interval = {}
        block_stream_map = {}
        for i in block_index_map:
            use = set()
            def_ = set()
            flag = False
            for j in range(block_index_map[i] + 1, len(list)):
                if list[j] == -1:
                    block_index_interval[i] = Interval(block_index_map[i], j)
                    flag = True
                    break
                if list[j].startswith("-"):
                    def_.add(list[j][1:])
                if list[j].startswith("%"):
                    use.add(list[j])
            block_stream_map[i] = Block(i, set(), set(), def_, use)
            if not flag:
                block_index_interval[i] = Interval(block_index_map[i], len(list))
        # for i in block_map:
        #     flag = False
        #     for cir in circle:
        #         if i in cir:
        #             flag = True
        #             break
        #     if flag:
        #         continue
        #     cir = self.search_circle(block_map, rbm, i)
        #     if frozenset(cir) not in circle:
        #         relist = []
        #         for t in cir:
        #             if t not in block_index_map:
        #                 continue
        #             p = block_index_map[t]
        #             beg = block_index[p][1]
        #             if p == len(block_index) - 1:
        #                 end = len(list)
        #             else:
        #                 end = block_index[p + 1][1]
        #             reguse = Interval(beg=beg, end=end)
        #             relist.append(reguse)
        #         self.merge_intervals(relist)
        #         circle[frozenset(cir)] = relist

        if ctx.params() != None:
            for i in ctx.params().parameter():
                if i.Privatevariable() != None:
                    define_map[i.Privatevariable().getText()] = -1
                    block_stream_map[entry].def_.add(i.Privatevariable().getText())
        block_stream_map[end].in_ = (
            block_stream_map[end].use - block_stream_map[end].def_
        )
        regusemap = {}
        phi_map2 = {}
        for i in phi_map:
            j = phi_map[i]
            for k in j:
                if j[k] not in phi_map2:
                    phi_map2[j[k]] = {}
                if i not in phi_map2[j[k]]:
                    phi_map2[j[k]][i] = set()
                phi_map2[j[k]][i].add(k)
        while True:
            flag = True
            for i in bfs_queue:
                if not self.update_block(
                    i, block_map, block_stream_map, phi_map, phi_map2
                ):
                    flag = False
            if flag:
                break
        for i in block_stream_map:
            intersection = block_stream_map[i].def_.intersection(
                block_stream_map[i].use
            )
            for j in intersection:
                for k in range(block_index_interval[i].end - 1, define_map[j], -1):
                    if list[k] == j:
                        if j not in regusemap:
                            regusemap[j] = []
                        regusemap[j].append(Interval(define_map[j], k))
                        break
                for k in range(define_map[j] - 1, block_index_interval[i].beg, -1):
                    if list[k] == j:
                        if j not in regusemap:
                            regusemap[j] = []
                        regusemap[j].append(Interval(block_index_interval[i].beg, k))
                        regusemap[j].append(
                            Interval(define_map[j], block_index_interval[i].end)
                        )
                        break
        for i in block_stream_map:
            block = block_stream_map[i]
            intersection = block.in_.intersection(block.out)
            in_ = block.in_ - intersection
            out = block.out - intersection
            for j in intersection:
                if j not in regusemap:
                    regusemap[j] = []
                regusemap[j].append(block_index_interval[i])
            for j in out:
                if j not in regusemap:
                    regusemap[j] = []
                regusemap[j].append(
                    Interval(define_map[j], block_index_interval[i].end)
                )
            for j in in_:
                if j not in regusemap:
                    regusemap[j] = []
                for k in range(
                    block_index_interval[i].end - 1, block_index_interval[i].beg, -1
                ):
                    if list[k] == j:
                        regusemap[j].append(Interval(block_index_interval[i].beg, k))
                        break
        reguselist = []
        # for i in range(len(list)):
        #     name = list[i]
        #     if name != "" and name != -1:
        #         define = define_map[name]
        #         define_block = ".entry"
        #         for k in range(len(block_index)):
        #             if block_index[k][1] < define and (
        #                 k == len(block_index) - 1 or block_index[k + 1][1] > define
        #             ):
        #                 define_block = block_index[k][0]
        #                 break
        #         use_block = ""
        #         for k in range(len(block_index)):
        #             if block_index[k][1] < i and (
        #                 k == len(block_index) - 1 or block_index[k + 1][1] > i
        #             ):
        #                 use_block = block_index[k][0]
        #                 break
        #         final_end = len(list)
        #         if define < i:
        #             # reguselist.append(RegUse(name=name, beg=define, end=i))
        #             if name not in regusemap:
        #                 regusemap[name] = []
        #             regusemap[name].append(Interval(beg=define, end=i))
        #             if define_block != use_block:
        #                 interval = [Interval(beg=define, end=i)]
        #                 for k in circle:
        #                     m = circle[k]
        #                     if self.has_intersection(interval, m):
        #                         for t in m:
        #                             # reguselist.append(
        #                             #     RegUse(name=name, beg=t.beg, end=t.end)
        #                             # )
        #                             regusemap[name].append(
        #                                 Interval(beg=t.beg, end=t.end)
        #                             )
        #         else:
        #             self.block_register(
        #                 name,
        #                 define_block,
        #                 block_index,
        #                 circle,
        #                 regusemap,
        #                 block_index_map,
        #                 final_end,
        #             )
        for i in regusemap:
            use = self.merge_intervals(regusemap[i])
            reguselist.append(RegUseList(i, use))
        reguselist.sort()
        reg_map = copy.deepcopy(self.reg_map)
        danger_list = []
        for i in danger_zone:
            danger_list.append(Interval(i, i))
        danger_list = self.merge_intervals(danger_list)
        for i in self.danger_reg:
            reg_map[i] += danger_list
        for i in reguselist:
            list1 = i.reg_list
            reg_sort = []
            for j in reg_map:
                len_ = 0
                for k in reg_map[j]:
                    len_ += k.end - k.beg + 1
                reg_sort.append((j, -len_))
            reg_sort.sort(key=lambda x: x[1])
            for j in reg_sort:
                j = j[0]
                list2 = reg_map[j]
                if self.has_intersection(list1, list2) == False:
                    reg_map[j] += list1
                    self.variable_map[i.name] = j
                    break

        self.variable_cnt = 8
        self.enter_function = ctx.Global_var().getText()[1:]
        tmp_store = {}
        if self.enter_function != "main":
            for i in reg_map:
                if len(reg_map[i]) != 0 and i.startswith("s"):
                    tmp_store[i] = self.variable_cnt
                    self.variable_cnt += 8
        self.tmp_store = tmp_store
        extra_param_list = []
        if ctx.params() is not None:
            if len(ctx.params().parameter()) > 7:
                params = ctx.params().parameter()[7:]
                for i in params:
                    if i.Privatevariable() is not None:
                        self.variable_map[i.Privatevariable().getText()] = -1
                        extra_param_list.append(i.Privatevariable().getText())
        self._traverse_nodes(ctx)
        self.variable_cnt += 16 - (self.variable_cnt % 16)
        for i in range(len(extra_param_list)):
            self.variable_map[extra_param_list[i]] = self.variable_cnt + i * 8
        self.return_str += (
            ".globl " + self.enter_function + "\n" + self.enter_function + ":\n"
        )
        if self.variable_cnt > 2047:
            self.return_str += "\tli t0, -" + str(self.variable_cnt) + "\n"
            self.return_str += "\tadd sp, sp, t0\n"
        else:
            self.return_str += "\taddi sp, sp, -" + str(self.variable_cnt) + "\n"
        self.return_str += "\tsd ra, 0(sp)\n"
        for i in tmp_store:
            self.saveword(tmp_store[i], i)
        if ctx.params() is not None:
            params = ctx.params().parameter()
            mv_list = []
            for i in range(min(len(params), 7)):
                param = params[i]
                name = param.Privatevariable().getText()
                index = self.variable_map[name]
                # self.loadword(index, "a" + str(i))
                if index != "a" + str(i):
                    mv_list.append(["a" + str(i), index])
            while len(mv_list) > 0:
                while True:
                    flag = True
                    dele = []
                    for i in mv_list:
                        check = False
                        for j in mv_list:
                            if i[1] == j[0]:
                                check = True
                                break
                        if not check:
                            self.saveword(i[1], i[0])
                            dele.append(i)
                            flag = False
                    if flag:
                        break
                    for i in dele:
                        mv_list.remove(i)
                dele = []
                for i in mv_list:
                    self.loadword(i[1], "t0")
                    self.loadword(i[0], i[1])
                    conflict = []
                    for j in mv_list:
                        if i[1] == j[0]:
                            conflict = j
                            break
                    mv_list.append(["t0", conflict[1]])
                    dele.append(conflict)
                    dele.append(i)
                    break
                for i in dele:
                    mv_list.remove(i)

    def _traverse_nodes(self, node):
        if hasattr(node, "Privatevariable") and node.Privatevariable() is not None:
            var_name = node.Privatevariable().getText()
            if var_name not in self.variable_map:
                self.variable_map[var_name] = self.variable_cnt
                self.variable_cnt += 8
        else:
            for child in node.getChildren():
                if isinstance(child, antlr4.ParserRuleContext):
                    self._traverse_nodes(child)

    def exitFunction(self, ctx: llvmParser.FunctionContext):
        self.variable_map = {}
        self.variable_cnt = 0
        for i in self.label_map:
            self.return_str += i + ":\n" + self.label_map[i]
        self.label_map = {}

    def enterGlobalvariable(self, ctx: llvmParser.GlobalvariableContext):
        self.data += ".align 4\n"
        self.data += ctx.Global_var().getText()[1:] + ":\n"
        if ctx.string_constant() != None:
            val = ctx.string_constant().getText()[1:]
            self.data += "\t.word " + val + "\n"
            return
        val = ctx.constant().getText()
        if val == "null":
            val = "0"
        self.data += "\t.word " + val + "\n"

    def enterString_declare(self, ctx: llvmParser.String_declareContext):
        self.data += ctx.Global_var().getText()[1:] + ":\n"
        str = ctx.StringLiteral().getText()[1:-1]
        str = str.replace("\\22", '\\"')
        str = str.replace("\\0A", "\\n")
        str = str.replace("\\00", "")
        self.data += '\t.asciz "' + str + '"\n'


def main(code: str):
    input_stream = InputStream(code)
    lexer = llvmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = llvmParser(token_stream)

    tree = parser.module()
    walker = ParseTreeWalker()
    listener = Mylistener3()
    walker.walk(listener, tree)
    listener.return_str = listener.return_str.replace("newBoolArray", "newIntArray")
    # with open("asm.s", "w") as f:
    #     f.write(listener.return_str + listener.data)
    return_str = ""
    lines = listener.return_str.splitlines()
    i = 0
    replace_map = {}
    if len(lines) == 1:
        return ""
    while i < len(lines):
        if (
            not lines[i].startswith("\t")
            and not lines[i].startswith("tmp")
            and not (
                ":" in lines[i] and ".entry" in lines[i] and lines[i].count(".") == 1
            )
        ):
            if lines[i + 1].startswith("\tj"):
                label1 = lines[i][:-1]
                label2 = lines[i + 1][3:]
                replace_map[label1] = label2
                i += 2
                continue
        return_str += lines[i] + "\n"
        i += 1

    def recursive_replace(replace_map, key):
        if key in replace_map:
            return recursive_replace(replace_map, replace_map[key])
        else:
            return key

    new_replace_map = {
        k: recursive_replace(replace_map, v) for k, v in replace_map.items()
    }
    for i in new_replace_map:
        return_str = return_str.replace(
            "j " + i + "\n", "j " + new_replace_map[i] + "\n"
        )
    # with open("asm_optim.s", "w") as f:
    #     f.write(return_str + listener.data)
    return (return_str + listener.data, listener.func_list)


if __name__ == "__main__":
    code = sys.stdin.read()
    code2 = main(code)
    with open("test.s", "w") as f:
        f.write(code2)
    print(code2)
