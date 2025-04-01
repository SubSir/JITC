# Generated from llvm.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .llvmParser import llvmParser
else:
    from llvmParser import llvmParser

# This class defines a complete generic visitor for a parse tree produced by llvmParser.


class llvmVisitor(ParseTreeVisitor):
    # Visit a parse tree produced by llvmParser#module.
    def visitModule(self, ctx: llvmParser.ModuleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#type.
    def visitType(self, ctx: llvmParser.TypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#function_declare.
    def visitFunction_declare(self, ctx: llvmParser.Function_declareContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#function.
    def visitFunction(self, ctx: llvmParser.FunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#typedelcare.
    def visitTypedelcare(self, ctx: llvmParser.TypedelcareContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#globalvariable.
    def visitGlobalvariable(self, ctx: llvmParser.GlobalvariableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#string_declare.
    def visitString_declare(self, ctx: llvmParser.String_declareContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#globalarray.
    def visitGlobalarray(self, ctx: llvmParser.GlobalarrayContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#params.
    def visitParams(self, ctx: llvmParser.ParamsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#types.
    def visitTypes(self, ctx: llvmParser.TypesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#parameter.
    def visitParameter(self, ctx: llvmParser.ParameterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#basic_block.
    def visitBasic_block(self, ctx: llvmParser.Basic_blockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#instruction.
    def visitInstruction(self, ctx: llvmParser.InstructionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#ret.
    def visitRet(self, ctx: llvmParser.RetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#call.
    def visitCall(self, ctx: llvmParser.CallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#binary_op.
    def visitBinary_op(self, ctx: llvmParser.Binary_opContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#bin_op.
    def visitBin_op(self, ctx: llvmParser.Bin_opContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#branch.
    def visitBranch(self, ctx: llvmParser.BranchContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#load.
    def visitLoad(self, ctx: llvmParser.LoadContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#var.
    def visitVar(self, ctx: llvmParser.VarContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#store.
    def visitStore(self, ctx: llvmParser.StoreContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#getelementptr.
    def visitGetelementptr(self, ctx: llvmParser.GetelementptrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#ptrtype.
    def visitPtrtype(self, ctx: llvmParser.PtrtypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#compare.
    def visitCompare(self, ctx: llvmParser.CompareContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#cond.
    def visitCond(self, ctx: llvmParser.CondContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#phi.
    def visitPhi(self, ctx: llvmParser.PhiContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#value.
    def visitValue(self, ctx: llvmParser.ValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#constant.
    def visitConstant(self, ctx: llvmParser.ConstantContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llvmParser#string_constant.
    def visitString_constant(self, ctx: llvmParser.String_constantContext):
        return self.visitChildren(ctx)


del llvmParser
