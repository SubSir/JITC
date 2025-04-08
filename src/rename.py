from antlr4 import *
from llvmparser.llvmLexer import llvmLexer
from llvmparser.llvmParser import llvmParser
from llvmparser.llvmListener import llvmListener
from antlr4.tree.Tree import TerminalNodeImpl
import sys


class Renamer(llvmListener):
    def __init__(self):
        self.enterfunction = ""
        self.ans = ""

    def enterFunction(self, ctx: llvmParser.FunctionContext):
        self.enterfunction = ctx.Global_var().getText()[1:]

    def visitTerminal(self, node: TerminalNodeImpl):
        text = node.getText()

        token_type = node.getSymbol().type

        if token_type == 52:
            text += "_" + self.enterfunction
        self.ans += text + " "
        if text == ";":
            self.ans += "\n"


def main(code):
    input_stream = InputStream(code)
    lexer = llvmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = llvmParser(token_stream)

    tree = parser.module()
    walker = ParseTreeWalker()
    listener = Renamer()
    walker.walk(listener, tree)
    return listener.ans


if __name__ == "__main__":
    code = sys.stdin.read()
    print(main(code))
