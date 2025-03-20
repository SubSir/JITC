import antlr4
from antlr4 import InputStream, CommonTokenStream
from llvmparser.llvmListener import llvmListener
from llvmparser.llvmLexer import llvmLexer
from llvmparser.llvmParser import llvmParser
from antlr4.tree.Tree import ParseTreeWalker

import sys

import asm


class Mylistener(llvmListener):
    def __init__(self) -> None:
        self.func_map = {}
        self.variable_map = {}

    def _traverse_nodes(self, node, func_name):
        if hasattr(node, "Global_var") and node.Global_var() is not None:
            var_name = node.Global_var().getText()
            self.func_map[func_name].add(var_name)
        for child in node.getChildren():
            if isinstance(child, antlr4.ParserRuleContext):
                self._traverse_nodes(child, func_name)

    def enterModule(self, ctx: llvmParser.ModuleContext):
        for i in ctx.getChildren():
            if isinstance(i, llvmParser.GlobalvariableContext):
                if i.constant() != None:
                    val = i.constant().getText()
                else:
                    val = i.string_constant().getText()
                self.variable_map[i.Global_var().getText()] = [i.type_().getText(), val]
            elif isinstance(i, llvmParser.FunctionContext):
                func_name = i.Global_var().getText()
                self.func_map[func_name] = set()
                for j in i.basic_block():
                    self._traverse_nodes(j, func_name)
                self.exeFunc(i)
            elif isinstance(i, llvmParser.String_declareContext):
                self.variable_map[i.Global_var().getText()] = [
                    "ptr",
                    i.StringLiteral().getText(),
                ]

    def getTextWithSpaces(self, ctx):
        """
        遍历 ctx 所有子节点，将节点文本拼接起来，每个节点后加一个空格。
        """
        result = []
        for i in range(ctx.getChildCount()):  # 遍历所有子节点
            child = ctx.getChild(i)
            if child.getChildCount() == 0:  # 如果是叶子节点
                result.append(child.getText())
            else:  # 如果是非叶子节点，递归处理
                result.append(self.getTextWithSpaces(child))
        return " ".join(result)  # 用空格拼接所有节点文本

    def exeFunc(self, ctx: llvmParser.FunctionContext):
        func_name = ctx.Global_var().getText()
        if len(self.func_map[func_name]) == 0:
            # 调用 getTextWithSpaces 获取带空格的文本
            text = self.getTextWithSpaces(ctx)
            asm_code = asm.main(text)
            with open("test.s", "w") as f:
                f.write(asm_code)


def main(code: str):
    input_stream = InputStream(code)
    lexer = llvmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = llvmParser(token_stream)

    tree = parser.module()
    walker = ParseTreeWalker()
    listener = Mylistener()
    walker.walk(listener, tree)


if __name__ == "__main__":
    code = sys.stdin.read()
    main(code)
