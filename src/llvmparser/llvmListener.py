# Generated from llvm.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .llvmParser import llvmParser
else:
    from llvmParser import llvmParser

# This class defines a complete listener for a parse tree produced by llvmParser.
class llvmListener(ParseTreeListener):

    # Enter a parse tree produced by llvmParser#module.
    def enterModule(self, ctx:llvmParser.ModuleContext):
        pass

    # Exit a parse tree produced by llvmParser#module.
    def exitModule(self, ctx:llvmParser.ModuleContext):
        pass


    # Enter a parse tree produced by llvmParser#type.
    def enterType(self, ctx:llvmParser.TypeContext):
        pass

    # Exit a parse tree produced by llvmParser#type.
    def exitType(self, ctx:llvmParser.TypeContext):
        pass


    # Enter a parse tree produced by llvmParser#function_declare.
    def enterFunction_declare(self, ctx:llvmParser.Function_declareContext):
        pass

    # Exit a parse tree produced by llvmParser#function_declare.
    def exitFunction_declare(self, ctx:llvmParser.Function_declareContext):
        pass


    # Enter a parse tree produced by llvmParser#function.
    def enterFunction(self, ctx:llvmParser.FunctionContext):
        pass

    # Exit a parse tree produced by llvmParser#function.
    def exitFunction(self, ctx:llvmParser.FunctionContext):
        pass


    # Enter a parse tree produced by llvmParser#typedelcare.
    def enterTypedelcare(self, ctx:llvmParser.TypedelcareContext):
        pass

    # Exit a parse tree produced by llvmParser#typedelcare.
    def exitTypedelcare(self, ctx:llvmParser.TypedelcareContext):
        pass


    # Enter a parse tree produced by llvmParser#globalvariable.
    def enterGlobalvariable(self, ctx:llvmParser.GlobalvariableContext):
        pass

    # Exit a parse tree produced by llvmParser#globalvariable.
    def exitGlobalvariable(self, ctx:llvmParser.GlobalvariableContext):
        pass


    # Enter a parse tree produced by llvmParser#string_declare.
    def enterString_declare(self, ctx:llvmParser.String_declareContext):
        pass

    # Exit a parse tree produced by llvmParser#string_declare.
    def exitString_declare(self, ctx:llvmParser.String_declareContext):
        pass


    # Enter a parse tree produced by llvmParser#globalarray.
    def enterGlobalarray(self, ctx:llvmParser.GlobalarrayContext):
        pass

    # Exit a parse tree produced by llvmParser#globalarray.
    def exitGlobalarray(self, ctx:llvmParser.GlobalarrayContext):
        pass


    # Enter a parse tree produced by llvmParser#params.
    def enterParams(self, ctx:llvmParser.ParamsContext):
        pass

    # Exit a parse tree produced by llvmParser#params.
    def exitParams(self, ctx:llvmParser.ParamsContext):
        pass


    # Enter a parse tree produced by llvmParser#types.
    def enterTypes(self, ctx:llvmParser.TypesContext):
        pass

    # Exit a parse tree produced by llvmParser#types.
    def exitTypes(self, ctx:llvmParser.TypesContext):
        pass


    # Enter a parse tree produced by llvmParser#parameter.
    def enterParameter(self, ctx:llvmParser.ParameterContext):
        pass

    # Exit a parse tree produced by llvmParser#parameter.
    def exitParameter(self, ctx:llvmParser.ParameterContext):
        pass


    # Enter a parse tree produced by llvmParser#basic_block.
    def enterBasic_block(self, ctx:llvmParser.Basic_blockContext):
        pass

    # Exit a parse tree produced by llvmParser#basic_block.
    def exitBasic_block(self, ctx:llvmParser.Basic_blockContext):
        pass


    # Enter a parse tree produced by llvmParser#instruction.
    def enterInstruction(self, ctx:llvmParser.InstructionContext):
        pass

    # Exit a parse tree produced by llvmParser#instruction.
    def exitInstruction(self, ctx:llvmParser.InstructionContext):
        pass


    # Enter a parse tree produced by llvmParser#ret.
    def enterRet(self, ctx:llvmParser.RetContext):
        pass

    # Exit a parse tree produced by llvmParser#ret.
    def exitRet(self, ctx:llvmParser.RetContext):
        pass


    # Enter a parse tree produced by llvmParser#call.
    def enterCall(self, ctx:llvmParser.CallContext):
        pass

    # Exit a parse tree produced by llvmParser#call.
    def exitCall(self, ctx:llvmParser.CallContext):
        pass


    # Enter a parse tree produced by llvmParser#binary_op.
    def enterBinary_op(self, ctx:llvmParser.Binary_opContext):
        pass

    # Exit a parse tree produced by llvmParser#binary_op.
    def exitBinary_op(self, ctx:llvmParser.Binary_opContext):
        pass


    # Enter a parse tree produced by llvmParser#bin_op.
    def enterBin_op(self, ctx:llvmParser.Bin_opContext):
        pass

    # Exit a parse tree produced by llvmParser#bin_op.
    def exitBin_op(self, ctx:llvmParser.Bin_opContext):
        pass


    # Enter a parse tree produced by llvmParser#branch.
    def enterBranch(self, ctx:llvmParser.BranchContext):
        pass

    # Exit a parse tree produced by llvmParser#branch.
    def exitBranch(self, ctx:llvmParser.BranchContext):
        pass


    # Enter a parse tree produced by llvmParser#load.
    def enterLoad(self, ctx:llvmParser.LoadContext):
        pass

    # Exit a parse tree produced by llvmParser#load.
    def exitLoad(self, ctx:llvmParser.LoadContext):
        pass


    # Enter a parse tree produced by llvmParser#var.
    def enterVar(self, ctx:llvmParser.VarContext):
        pass

    # Exit a parse tree produced by llvmParser#var.
    def exitVar(self, ctx:llvmParser.VarContext):
        pass


    # Enter a parse tree produced by llvmParser#store.
    def enterStore(self, ctx:llvmParser.StoreContext):
        pass

    # Exit a parse tree produced by llvmParser#store.
    def exitStore(self, ctx:llvmParser.StoreContext):
        pass


    # Enter a parse tree produced by llvmParser#getelementptr.
    def enterGetelementptr(self, ctx:llvmParser.GetelementptrContext):
        pass

    # Exit a parse tree produced by llvmParser#getelementptr.
    def exitGetelementptr(self, ctx:llvmParser.GetelementptrContext):
        pass


    # Enter a parse tree produced by llvmParser#ptrtype.
    def enterPtrtype(self, ctx:llvmParser.PtrtypeContext):
        pass

    # Exit a parse tree produced by llvmParser#ptrtype.
    def exitPtrtype(self, ctx:llvmParser.PtrtypeContext):
        pass


    # Enter a parse tree produced by llvmParser#compare.
    def enterCompare(self, ctx:llvmParser.CompareContext):
        pass

    # Exit a parse tree produced by llvmParser#compare.
    def exitCompare(self, ctx:llvmParser.CompareContext):
        pass


    # Enter a parse tree produced by llvmParser#cond.
    def enterCond(self, ctx:llvmParser.CondContext):
        pass

    # Exit a parse tree produced by llvmParser#cond.
    def exitCond(self, ctx:llvmParser.CondContext):
        pass


    # Enter a parse tree produced by llvmParser#phi.
    def enterPhi(self, ctx:llvmParser.PhiContext):
        pass

    # Exit a parse tree produced by llvmParser#phi.
    def exitPhi(self, ctx:llvmParser.PhiContext):
        pass


    # Enter a parse tree produced by llvmParser#value.
    def enterValue(self, ctx:llvmParser.ValueContext):
        pass

    # Exit a parse tree produced by llvmParser#value.
    def exitValue(self, ctx:llvmParser.ValueContext):
        pass


    # Enter a parse tree produced by llvmParser#constant.
    def enterConstant(self, ctx:llvmParser.ConstantContext):
        pass

    # Exit a parse tree produced by llvmParser#constant.
    def exitConstant(self, ctx:llvmParser.ConstantContext):
        pass


    # Enter a parse tree produced by llvmParser#string_constant.
    def enterString_constant(self, ctx:llvmParser.String_constantContext):
        pass

    # Exit a parse tree produced by llvmParser#string_constant.
    def exitString_constant(self, ctx:llvmParser.String_constantContext):
        pass



del llvmParser