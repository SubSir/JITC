# Generated from llvm.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,55,325,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,1,0,1,0,1,0,1,0,1,0,5,0,65,8,0,10,0,12,0,
        68,9,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,2,77,8,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,3,3,3,86,8,3,1,3,1,3,1,3,4,3,91,8,3,11,3,12,3,92,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,3,4,102,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,
        3,5,112,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,5,8,138,8,8,10,8,12,
        8,141,9,8,1,9,1,9,1,9,5,9,146,8,9,10,9,12,9,149,9,9,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,160,8,10,1,11,1,11,1,11,4,
        11,165,8,11,11,11,12,11,166,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,3,12,178,8,12,1,13,1,13,1,13,3,13,183,8,13,1,14,1,14,1,14,
        1,14,1,14,3,14,190,8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,3,14,201,8,14,1,14,1,14,3,14,205,8,14,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,233,8,17,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
        21,1,21,3,21,277,8,21,1,22,1,22,3,22,281,8,22,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,4,25,
        312,8,25,11,25,12,25,313,1,26,1,26,1,26,3,26,319,8,26,1,27,1,27,
        1,28,1,28,1,28,0,0,29,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,48,50,52,54,56,0,5,1,0,1,4,1,0,24,33,1,0,
        52,53,1,0,41,46,1,0,48,49,329,0,66,1,0,0,0,2,69,1,0,0,0,4,71,1,0,
        0,0,6,80,1,0,0,0,8,96,1,0,0,0,10,105,1,0,0,0,12,113,1,0,0,0,14,124,
        1,0,0,0,16,134,1,0,0,0,18,142,1,0,0,0,20,159,1,0,0,0,22,161,1,0,
        0,0,24,177,1,0,0,0,26,179,1,0,0,0,28,204,1,0,0,0,30,206,1,0,0,0,
        32,214,1,0,0,0,34,232,1,0,0,0,36,234,1,0,0,0,38,242,1,0,0,0,40,244,
        1,0,0,0,42,276,1,0,0,0,44,280,1,0,0,0,46,282,1,0,0,0,48,291,1,0,
        0,0,50,293,1,0,0,0,52,318,1,0,0,0,54,320,1,0,0,0,56,322,1,0,0,0,
        58,65,3,6,3,0,59,65,3,4,2,0,60,65,3,10,5,0,61,65,3,12,6,0,62,65,
        3,8,4,0,63,65,3,14,7,0,64,58,1,0,0,0,64,59,1,0,0,0,64,60,1,0,0,0,
        64,61,1,0,0,0,64,62,1,0,0,0,64,63,1,0,0,0,65,68,1,0,0,0,66,64,1,
        0,0,0,66,67,1,0,0,0,67,1,1,0,0,0,68,66,1,0,0,0,69,70,7,0,0,0,70,
        3,1,0,0,0,71,72,5,5,0,0,72,73,3,2,1,0,73,74,5,53,0,0,74,76,5,6,0,
        0,75,77,3,18,9,0,76,75,1,0,0,0,76,77,1,0,0,0,77,78,1,0,0,0,78,79,
        5,7,0,0,79,5,1,0,0,0,80,81,5,8,0,0,81,82,3,2,1,0,82,83,5,53,0,0,
        83,85,5,6,0,0,84,86,3,16,8,0,85,84,1,0,0,0,85,86,1,0,0,0,86,87,1,
        0,0,0,87,88,5,7,0,0,88,90,5,9,0,0,89,91,3,22,11,0,90,89,1,0,0,0,
        91,92,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,94,1,0,0,0,94,95,5,
        10,0,0,95,7,1,0,0,0,96,97,5,52,0,0,97,98,5,11,0,0,98,99,5,12,0,0,
        99,101,5,9,0,0,100,102,3,18,9,0,101,100,1,0,0,0,101,102,1,0,0,0,
        102,103,1,0,0,0,103,104,5,10,0,0,104,9,1,0,0,0,105,106,5,53,0,0,
        106,107,5,11,0,0,107,108,5,13,0,0,108,111,3,2,1,0,109,112,3,54,27,
        0,110,112,3,56,28,0,111,109,1,0,0,0,111,110,1,0,0,0,112,11,1,0,0,
        0,113,114,5,53,0,0,114,115,5,11,0,0,115,116,5,13,0,0,116,117,5,14,
        0,0,117,118,5,49,0,0,118,119,5,15,0,0,119,120,5,16,0,0,120,121,5,
        17,0,0,121,122,5,18,0,0,122,123,5,54,0,0,123,13,1,0,0,0,124,125,
        5,53,0,0,125,126,5,11,0,0,126,127,5,13,0,0,127,128,5,14,0,0,128,
        129,5,49,0,0,129,130,5,15,0,0,130,131,3,2,1,0,131,132,5,17,0,0,132,
        133,5,19,0,0,133,15,1,0,0,0,134,139,3,20,10,0,135,136,5,20,0,0,136,
        138,3,20,10,0,137,135,1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,
        140,1,0,0,0,140,17,1,0,0,0,141,139,1,0,0,0,142,147,3,2,1,0,143,144,
        5,20,0,0,144,146,3,2,1,0,145,143,1,0,0,0,146,149,1,0,0,0,147,145,
        1,0,0,0,147,148,1,0,0,0,148,19,1,0,0,0,149,147,1,0,0,0,150,151,3,
        2,1,0,151,152,5,52,0,0,152,160,1,0,0,0,153,154,3,2,1,0,154,155,5,
        53,0,0,155,160,1,0,0,0,156,157,3,2,1,0,157,158,3,54,27,0,158,160,
        1,0,0,0,159,150,1,0,0,0,159,153,1,0,0,0,159,156,1,0,0,0,160,21,1,
        0,0,0,161,162,5,50,0,0,162,164,5,21,0,0,163,165,3,24,12,0,164,163,
        1,0,0,0,165,166,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,23,1,
        0,0,0,168,178,3,26,13,0,169,178,3,28,14,0,170,178,3,30,15,0,171,
        178,3,34,17,0,172,178,3,36,18,0,173,178,3,40,20,0,174,178,3,42,21,
        0,175,178,3,46,23,0,176,178,3,50,25,0,177,168,1,0,0,0,177,169,1,
        0,0,0,177,170,1,0,0,0,177,171,1,0,0,0,177,172,1,0,0,0,177,173,1,
        0,0,0,177,174,1,0,0,0,177,175,1,0,0,0,177,176,1,0,0,0,178,25,1,0,
        0,0,179,180,5,22,0,0,180,182,3,2,1,0,181,183,3,52,26,0,182,181,1,
        0,0,0,182,183,1,0,0,0,183,27,1,0,0,0,184,185,5,23,0,0,185,186,3,
        2,1,0,186,187,5,53,0,0,187,189,5,6,0,0,188,190,3,16,8,0,189,188,
        1,0,0,0,189,190,1,0,0,0,190,191,1,0,0,0,191,192,5,7,0,0,192,205,
        1,0,0,0,193,194,5,52,0,0,194,195,5,11,0,0,195,196,5,23,0,0,196,197,
        3,2,1,0,197,198,5,53,0,0,198,200,5,6,0,0,199,201,3,16,8,0,200,199,
        1,0,0,0,200,201,1,0,0,0,201,202,1,0,0,0,202,203,5,7,0,0,203,205,
        1,0,0,0,204,184,1,0,0,0,204,193,1,0,0,0,205,29,1,0,0,0,206,207,5,
        52,0,0,207,208,5,11,0,0,208,209,3,32,16,0,209,210,3,2,1,0,210,211,
        3,52,26,0,211,212,5,20,0,0,212,213,3,52,26,0,213,31,1,0,0,0,214,
        215,7,1,0,0,215,33,1,0,0,0,216,217,5,34,0,0,217,218,5,35,0,0,218,
        219,5,36,0,0,219,233,5,50,0,0,220,221,5,34,0,0,221,222,5,4,0,0,222,
        223,3,52,26,0,223,224,5,20,0,0,224,225,5,35,0,0,225,226,5,36,0,0,
        226,227,5,50,0,0,227,228,5,20,0,0,228,229,5,35,0,0,229,230,5,36,
        0,0,230,231,5,50,0,0,231,233,1,0,0,0,232,216,1,0,0,0,232,220,1,0,
        0,0,233,35,1,0,0,0,234,235,5,52,0,0,235,236,5,11,0,0,236,237,5,37,
        0,0,237,238,3,2,1,0,238,239,5,20,0,0,239,240,5,2,0,0,240,241,3,38,
        19,0,241,37,1,0,0,0,242,243,7,2,0,0,243,39,1,0,0,0,244,245,5,38,
        0,0,245,246,3,2,1,0,246,247,3,52,26,0,247,248,5,20,0,0,248,249,5,
        2,0,0,249,250,3,38,19,0,250,41,1,0,0,0,251,252,5,52,0,0,252,253,
        5,11,0,0,253,254,5,39,0,0,254,255,3,44,22,0,255,256,5,20,0,0,256,
        257,5,2,0,0,257,258,3,38,19,0,258,259,5,20,0,0,259,260,5,1,0,0,260,
        261,3,52,26,0,261,277,1,0,0,0,262,263,5,52,0,0,263,264,5,11,0,0,
        264,265,5,39,0,0,265,266,3,44,22,0,266,267,5,20,0,0,267,268,5,2,
        0,0,268,269,3,38,19,0,269,270,5,20,0,0,270,271,5,1,0,0,271,272,5,
        49,0,0,272,273,5,20,0,0,273,274,5,1,0,0,274,275,3,52,26,0,275,277,
        1,0,0,0,276,251,1,0,0,0,276,262,1,0,0,0,277,43,1,0,0,0,278,281,3,
        2,1,0,279,281,5,52,0,0,280,278,1,0,0,0,280,279,1,0,0,0,281,45,1,
        0,0,0,282,283,5,52,0,0,283,284,5,11,0,0,284,285,5,40,0,0,285,286,
        3,48,24,0,286,287,3,2,1,0,287,288,3,52,26,0,288,289,5,20,0,0,289,
        290,3,52,26,0,290,47,1,0,0,0,291,292,7,3,0,0,292,49,1,0,0,0,293,
        294,5,52,0,0,294,295,5,11,0,0,295,296,5,47,0,0,296,297,3,2,1,0,297,
        298,5,14,0,0,298,299,3,52,26,0,299,300,5,20,0,0,300,301,5,36,0,0,
        301,302,5,50,0,0,302,311,5,17,0,0,303,304,5,20,0,0,304,305,5,14,
        0,0,305,306,3,52,26,0,306,307,5,20,0,0,307,308,5,36,0,0,308,309,
        5,50,0,0,309,310,5,17,0,0,310,312,1,0,0,0,311,303,1,0,0,0,312,313,
        1,0,0,0,313,311,1,0,0,0,313,314,1,0,0,0,314,51,1,0,0,0,315,319,5,
        52,0,0,316,319,3,54,27,0,317,319,5,53,0,0,318,315,1,0,0,0,318,316,
        1,0,0,0,318,317,1,0,0,0,319,53,1,0,0,0,320,321,7,4,0,0,321,55,1,
        0,0,0,322,323,5,53,0,0,323,57,1,0,0,0,21,64,66,76,85,92,101,111,
        139,147,159,166,177,182,189,200,204,232,276,280,313,318
    ]

class llvmParser ( Parser ):

    grammarFileName = "llvm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'i32'", "'ptr'", "'void'", "'i1'", "'declare'", 
                     "'('", "')'", "'define'", "'{'", "'}'", "'='", "'type'", 
                     "'global'", "'['", "'x'", "'i8'", "']'", "'c'", "'zeroinitializer'", 
                     "','", "':'", "'ret'", "'call'", "'add'", "'sub'", 
                     "'mul'", "'sdiv'", "'srem'", "'shl'", "'ashr'", "'and'", 
                     "'or'", "'xor'", "'br'", "'label'", "'%'", "'load'", 
                     "'store'", "'getelementptr'", "'icmp'", "'eq'", "'ne'", 
                     "'slt'", "'sgt'", "'sle'", "'sge'", "'phi'", "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INTEGER", "Label", "Identifier", "Privatevariable", 
                      "Global_var", "StringLiteral", "WS" ]

    RULE_module = 0
    RULE_type = 1
    RULE_function_declare = 2
    RULE_function = 3
    RULE_typedelcare = 4
    RULE_globalvariable = 5
    RULE_string_declare = 6
    RULE_globalarray = 7
    RULE_params = 8
    RULE_types = 9
    RULE_parameter = 10
    RULE_basic_block = 11
    RULE_instruction = 12
    RULE_ret = 13
    RULE_call = 14
    RULE_binary_op = 15
    RULE_bin_op = 16
    RULE_branch = 17
    RULE_load = 18
    RULE_var = 19
    RULE_store = 20
    RULE_getelementptr = 21
    RULE_ptrtype = 22
    RULE_compare = 23
    RULE_cond = 24
    RULE_phi = 25
    RULE_value = 26
    RULE_constant = 27
    RULE_string_constant = 28

    ruleNames =  [ "module", "type", "function_declare", "function", "typedelcare", 
                   "globalvariable", "string_declare", "globalarray", "params", 
                   "types", "parameter", "basic_block", "instruction", "ret", 
                   "call", "binary_op", "bin_op", "branch", "load", "var", 
                   "store", "getelementptr", "ptrtype", "compare", "cond", 
                   "phi", "value", "constant", "string_constant" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    INTEGER=49
    Label=50
    Identifier=51
    Privatevariable=52
    Global_var=53
    StringLiteral=54
    WS=55

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ModuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.FunctionContext)
            else:
                return self.getTypedRuleContext(llvmParser.FunctionContext,i)


        def function_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.Function_declareContext)
            else:
                return self.getTypedRuleContext(llvmParser.Function_declareContext,i)


        def globalvariable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.GlobalvariableContext)
            else:
                return self.getTypedRuleContext(llvmParser.GlobalvariableContext,i)


        def string_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.String_declareContext)
            else:
                return self.getTypedRuleContext(llvmParser.String_declareContext,i)


        def typedelcare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.TypedelcareContext)
            else:
                return self.getTypedRuleContext(llvmParser.TypedelcareContext,i)


        def globalarray(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.GlobalarrayContext)
            else:
                return self.getTypedRuleContext(llvmParser.GlobalarrayContext,i)


        def getRuleIndex(self):
            return llvmParser.RULE_module

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModule" ):
                listener.enterModule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModule" ):
                listener.exitModule(self)




    def module(self):

        localctx = llvmParser.ModuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13510798882111776) != 0):
                self.state = 64
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 58
                    self.function()
                    pass

                elif la_ == 2:
                    self.state = 59
                    self.function_declare()
                    pass

                elif la_ == 3:
                    self.state = 60
                    self.globalvariable()
                    pass

                elif la_ == 4:
                    self.state = 61
                    self.string_declare()
                    pass

                elif la_ == 5:
                    self.state = 62
                    self.typedelcare()
                    pass

                elif la_ == 6:
                    self.state = 63
                    self.globalarray()
                    pass


                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return llvmParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = llvmParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def Global_var(self):
            return self.getToken(llvmParser.Global_var, 0)

        def types(self):
            return self.getTypedRuleContext(llvmParser.TypesContext,0)


        def getRuleIndex(self):
            return llvmParser.RULE_function_declare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declare" ):
                listener.enterFunction_declare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declare" ):
                listener.exitFunction_declare(self)




    def function_declare(self):

        localctx = llvmParser.Function_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(llvmParser.T__4)
            self.state = 72
            self.type_()
            self.state = 73
            self.match(llvmParser.Global_var)
            self.state = 74
            self.match(llvmParser.T__5)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                self.state = 75
                self.types()


            self.state = 78
            self.match(llvmParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def Global_var(self):
            return self.getToken(llvmParser.Global_var, 0)

        def params(self):
            return self.getTypedRuleContext(llvmParser.ParamsContext,0)


        def basic_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.Basic_blockContext)
            else:
                return self.getTypedRuleContext(llvmParser.Basic_blockContext,i)


        def getRuleIndex(self):
            return llvmParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = llvmParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(llvmParser.T__7)
            self.state = 81
            self.type_()
            self.state = 82
            self.match(llvmParser.Global_var)
            self.state = 83
            self.match(llvmParser.T__5)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                self.state = 84
                self.params()


            self.state = 87
            self.match(llvmParser.T__6)
            self.state = 88
            self.match(llvmParser.T__8)
            self.state = 90 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 89
                self.basic_block()
                self.state = 92 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==50):
                    break

            self.state = 94
            self.match(llvmParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedelcareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Privatevariable(self):
            return self.getToken(llvmParser.Privatevariable, 0)

        def types(self):
            return self.getTypedRuleContext(llvmParser.TypesContext,0)


        def getRuleIndex(self):
            return llvmParser.RULE_typedelcare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedelcare" ):
                listener.enterTypedelcare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedelcare" ):
                listener.exitTypedelcare(self)




    def typedelcare(self):

        localctx = llvmParser.TypedelcareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_typedelcare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(llvmParser.Privatevariable)
            self.state = 97
            self.match(llvmParser.T__10)
            self.state = 98
            self.match(llvmParser.T__11)
            self.state = 99
            self.match(llvmParser.T__8)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                self.state = 100
                self.types()


            self.state = 103
            self.match(llvmParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalvariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Global_var(self):
            return self.getToken(llvmParser.Global_var, 0)

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def constant(self):
            return self.getTypedRuleContext(llvmParser.ConstantContext,0)


        def string_constant(self):
            return self.getTypedRuleContext(llvmParser.String_constantContext,0)


        def getRuleIndex(self):
            return llvmParser.RULE_globalvariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalvariable" ):
                listener.enterGlobalvariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalvariable" ):
                listener.exitGlobalvariable(self)




    def globalvariable(self):

        localctx = llvmParser.GlobalvariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_globalvariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(llvmParser.Global_var)
            self.state = 106
            self.match(llvmParser.T__10)
            self.state = 107
            self.match(llvmParser.T__12)
            self.state = 108
            self.type_()
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48, 49]:
                self.state = 109
                self.constant()
                pass
            elif token in [53]:
                self.state = 110
                self.string_constant()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Global_var(self):
            return self.getToken(llvmParser.Global_var, 0)

        def INTEGER(self):
            return self.getToken(llvmParser.INTEGER, 0)

        def StringLiteral(self):
            return self.getToken(llvmParser.StringLiteral, 0)

        def getRuleIndex(self):
            return llvmParser.RULE_string_declare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_declare" ):
                listener.enterString_declare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_declare" ):
                listener.exitString_declare(self)




    def string_declare(self):

        localctx = llvmParser.String_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_string_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(llvmParser.Global_var)
            self.state = 114
            self.match(llvmParser.T__10)
            self.state = 115
            self.match(llvmParser.T__12)
            self.state = 116
            self.match(llvmParser.T__13)
            self.state = 117
            self.match(llvmParser.INTEGER)
            self.state = 118
            self.match(llvmParser.T__14)
            self.state = 119
            self.match(llvmParser.T__15)
            self.state = 120
            self.match(llvmParser.T__16)
            self.state = 121
            self.match(llvmParser.T__17)
            self.state = 122
            self.match(llvmParser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalarrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Global_var(self):
            return self.getToken(llvmParser.Global_var, 0)

        def INTEGER(self):
            return self.getToken(llvmParser.INTEGER, 0)

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def getRuleIndex(self):
            return llvmParser.RULE_globalarray

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalarray" ):
                listener.enterGlobalarray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalarray" ):
                listener.exitGlobalarray(self)




    def globalarray(self):

        localctx = llvmParser.GlobalarrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_globalarray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(llvmParser.Global_var)
            self.state = 125
            self.match(llvmParser.T__10)
            self.state = 126
            self.match(llvmParser.T__12)
            self.state = 127
            self.match(llvmParser.T__13)
            self.state = 128
            self.match(llvmParser.INTEGER)
            self.state = 129
            self.match(llvmParser.T__14)
            self.state = 130
            self.type_()
            self.state = 131
            self.match(llvmParser.T__16)
            self.state = 132
            self.match(llvmParser.T__18)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.ParameterContext)
            else:
                return self.getTypedRuleContext(llvmParser.ParameterContext,i)


        def getRuleIndex(self):
            return llvmParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = llvmParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.parameter()
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 135
                self.match(llvmParser.T__19)
                self.state = 136
                self.parameter()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.TypeContext)
            else:
                return self.getTypedRuleContext(llvmParser.TypeContext,i)


        def getRuleIndex(self):
            return llvmParser.RULE_types

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypes" ):
                listener.enterTypes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypes" ):
                listener.exitTypes(self)




    def types(self):

        localctx = llvmParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.type_()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 143
                self.match(llvmParser.T__19)
                self.state = 144
                self.type_()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def Privatevariable(self):
            return self.getToken(llvmParser.Privatevariable, 0)

        def Global_var(self):
            return self.getToken(llvmParser.Global_var, 0)

        def constant(self):
            return self.getTypedRuleContext(llvmParser.ConstantContext,0)


        def getRuleIndex(self):
            return llvmParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = llvmParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameter)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.type_()
                self.state = 151
                self.match(llvmParser.Privatevariable)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.type_()
                self.state = 154
                self.match(llvmParser.Global_var)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.type_()
                self.state = 157
                self.constant()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Label(self):
            return self.getToken(llvmParser.Label, 0)

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.InstructionContext)
            else:
                return self.getTypedRuleContext(llvmParser.InstructionContext,i)


        def getRuleIndex(self):
            return llvmParser.RULE_basic_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasic_block" ):
                listener.enterBasic_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasic_block" ):
                listener.exitBasic_block(self)




    def basic_block(self):

        localctx = llvmParser.Basic_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_basic_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(llvmParser.Label)
            self.state = 162
            self.match(llvmParser.T__20)
            self.state = 164 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 163
                self.instruction()
                self.state = 166 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4503891697729536) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ret(self):
            return self.getTypedRuleContext(llvmParser.RetContext,0)


        def call(self):
            return self.getTypedRuleContext(llvmParser.CallContext,0)


        def binary_op(self):
            return self.getTypedRuleContext(llvmParser.Binary_opContext,0)


        def branch(self):
            return self.getTypedRuleContext(llvmParser.BranchContext,0)


        def load(self):
            return self.getTypedRuleContext(llvmParser.LoadContext,0)


        def store(self):
            return self.getTypedRuleContext(llvmParser.StoreContext,0)


        def getelementptr(self):
            return self.getTypedRuleContext(llvmParser.GetelementptrContext,0)


        def compare(self):
            return self.getTypedRuleContext(llvmParser.CompareContext,0)


        def phi(self):
            return self.getTypedRuleContext(llvmParser.PhiContext,0)


        def getRuleIndex(self):
            return llvmParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)




    def instruction(self):

        localctx = llvmParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_instruction)
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.ret()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 170
                self.binary_op()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 171
                self.branch()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 172
                self.load()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 173
                self.store()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 174
                self.getelementptr()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 175
                self.compare()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 176
                self.phi()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def value(self):
            return self.getTypedRuleContext(llvmParser.ValueContext,0)


        def getRuleIndex(self):
            return llvmParser.RULE_ret

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRet" ):
                listener.enterRet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRet" ):
                listener.exitRet(self)




    def ret(self):

        localctx = llvmParser.RetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ret)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(llvmParser.T__21)
            self.state = 180
            self.type_()
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 181
                self.value()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def Global_var(self):
            return self.getToken(llvmParser.Global_var, 0)

        def params(self):
            return self.getTypedRuleContext(llvmParser.ParamsContext,0)


        def Privatevariable(self):
            return self.getToken(llvmParser.Privatevariable, 0)

        def getRuleIndex(self):
            return llvmParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = llvmParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(llvmParser.T__22)
                self.state = 185
                self.type_()
                self.state = 186
                self.match(llvmParser.Global_var)
                self.state = 187
                self.match(llvmParser.T__5)
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                    self.state = 188
                    self.params()


                self.state = 191
                self.match(llvmParser.T__6)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(llvmParser.Privatevariable)
                self.state = 194
                self.match(llvmParser.T__10)
                self.state = 195
                self.match(llvmParser.T__22)
                self.state = 196
                self.type_()
                self.state = 197
                self.match(llvmParser.Global_var)
                self.state = 198
                self.match(llvmParser.T__5)
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                    self.state = 199
                    self.params()


                self.state = 202
                self.match(llvmParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Binary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Privatevariable(self):
            return self.getToken(llvmParser.Privatevariable, 0)

        def bin_op(self):
            return self.getTypedRuleContext(llvmParser.Bin_opContext,0)


        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.ValueContext)
            else:
                return self.getTypedRuleContext(llvmParser.ValueContext,i)


        def getRuleIndex(self):
            return llvmParser.RULE_binary_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_op" ):
                listener.enterBinary_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_op" ):
                listener.exitBinary_op(self)




    def binary_op(self):

        localctx = llvmParser.Binary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_binary_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(llvmParser.Privatevariable)
            self.state = 207
            self.match(llvmParser.T__10)
            self.state = 208
            self.bin_op()
            self.state = 209
            self.type_()
            self.state = 210
            self.value()
            self.state = 211
            self.match(llvmParser.T__19)
            self.state = 212
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bin_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return llvmParser.RULE_bin_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBin_op" ):
                listener.enterBin_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBin_op" ):
                listener.exitBin_op(self)




    def bin_op(self):

        localctx = llvmParser.Bin_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_bin_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17163091968) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BranchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Label(self, i:int=None):
            if i is None:
                return self.getTokens(llvmParser.Label)
            else:
                return self.getToken(llvmParser.Label, i)

        def value(self):
            return self.getTypedRuleContext(llvmParser.ValueContext,0)


        def getRuleIndex(self):
            return llvmParser.RULE_branch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBranch" ):
                listener.enterBranch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBranch" ):
                listener.exitBranch(self)




    def branch(self):

        localctx = llvmParser.BranchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_branch)
        try:
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.match(llvmParser.T__33)
                self.state = 217
                self.match(llvmParser.T__34)
                self.state = 218
                self.match(llvmParser.T__35)
                self.state = 219
                self.match(llvmParser.Label)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.match(llvmParser.T__33)
                self.state = 221
                self.match(llvmParser.T__3)
                self.state = 222
                self.value()
                self.state = 223
                self.match(llvmParser.T__19)
                self.state = 224
                self.match(llvmParser.T__34)
                self.state = 225
                self.match(llvmParser.T__35)
                self.state = 226
                self.match(llvmParser.Label)
                self.state = 227
                self.match(llvmParser.T__19)
                self.state = 228
                self.match(llvmParser.T__34)
                self.state = 229
                self.match(llvmParser.T__35)
                self.state = 230
                self.match(llvmParser.Label)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Privatevariable(self):
            return self.getToken(llvmParser.Privatevariable, 0)

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def var(self):
            return self.getTypedRuleContext(llvmParser.VarContext,0)


        def getRuleIndex(self):
            return llvmParser.RULE_load

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoad" ):
                listener.enterLoad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoad" ):
                listener.exitLoad(self)




    def load(self):

        localctx = llvmParser.LoadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_load)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(llvmParser.Privatevariable)
            self.state = 235
            self.match(llvmParser.T__10)
            self.state = 236
            self.match(llvmParser.T__36)
            self.state = 237
            self.type_()
            self.state = 238
            self.match(llvmParser.T__19)
            self.state = 239
            self.match(llvmParser.T__1)
            self.state = 240
            self.var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Privatevariable(self):
            return self.getToken(llvmParser.Privatevariable, 0)

        def Global_var(self):
            return self.getToken(llvmParser.Global_var, 0)

        def getRuleIndex(self):
            return llvmParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)




    def var(self):

        localctx = llvmParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            _la = self._input.LA(1)
            if not(_la==52 or _la==53):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def value(self):
            return self.getTypedRuleContext(llvmParser.ValueContext,0)


        def var(self):
            return self.getTypedRuleContext(llvmParser.VarContext,0)


        def getRuleIndex(self):
            return llvmParser.RULE_store

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStore" ):
                listener.enterStore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStore" ):
                listener.exitStore(self)




    def store(self):

        localctx = llvmParser.StoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_store)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(llvmParser.T__37)
            self.state = 245
            self.type_()
            self.state = 246
            self.value()
            self.state = 247
            self.match(llvmParser.T__19)
            self.state = 248
            self.match(llvmParser.T__1)
            self.state = 249
            self.var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GetelementptrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Privatevariable(self):
            return self.getToken(llvmParser.Privatevariable, 0)

        def ptrtype(self):
            return self.getTypedRuleContext(llvmParser.PtrtypeContext,0)


        def var(self):
            return self.getTypedRuleContext(llvmParser.VarContext,0)


        def value(self):
            return self.getTypedRuleContext(llvmParser.ValueContext,0)


        def INTEGER(self):
            return self.getToken(llvmParser.INTEGER, 0)

        def getRuleIndex(self):
            return llvmParser.RULE_getelementptr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetelementptr" ):
                listener.enterGetelementptr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetelementptr" ):
                listener.exitGetelementptr(self)




    def getelementptr(self):

        localctx = llvmParser.GetelementptrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_getelementptr)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.match(llvmParser.Privatevariable)
                self.state = 252
                self.match(llvmParser.T__10)
                self.state = 253
                self.match(llvmParser.T__38)
                self.state = 254
                self.ptrtype()
                self.state = 255
                self.match(llvmParser.T__19)
                self.state = 256
                self.match(llvmParser.T__1)
                self.state = 257
                self.var()
                self.state = 258
                self.match(llvmParser.T__19)
                self.state = 259
                self.match(llvmParser.T__0)
                self.state = 260
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.match(llvmParser.Privatevariable)
                self.state = 263
                self.match(llvmParser.T__10)
                self.state = 264
                self.match(llvmParser.T__38)
                self.state = 265
                self.ptrtype()
                self.state = 266
                self.match(llvmParser.T__19)
                self.state = 267
                self.match(llvmParser.T__1)
                self.state = 268
                self.var()
                self.state = 269
                self.match(llvmParser.T__19)
                self.state = 270
                self.match(llvmParser.T__0)
                self.state = 271
                self.match(llvmParser.INTEGER)
                self.state = 272
                self.match(llvmParser.T__19)
                self.state = 273
                self.match(llvmParser.T__0)
                self.state = 274
                self.value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PtrtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def Privatevariable(self):
            return self.getToken(llvmParser.Privatevariable, 0)

        def getRuleIndex(self):
            return llvmParser.RULE_ptrtype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPtrtype" ):
                listener.enterPtrtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPtrtype" ):
                listener.exitPtrtype(self)




    def ptrtype(self):

        localctx = llvmParser.PtrtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_ptrtype)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.type_()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.match(llvmParser.Privatevariable)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Privatevariable(self):
            return self.getToken(llvmParser.Privatevariable, 0)

        def cond(self):
            return self.getTypedRuleContext(llvmParser.CondContext,0)


        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.ValueContext)
            else:
                return self.getTypedRuleContext(llvmParser.ValueContext,i)


        def getRuleIndex(self):
            return llvmParser.RULE_compare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompare" ):
                listener.enterCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompare" ):
                listener.exitCompare(self)




    def compare(self):

        localctx = llvmParser.CompareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_compare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(llvmParser.Privatevariable)
            self.state = 283
            self.match(llvmParser.T__10)
            self.state = 284
            self.match(llvmParser.T__39)
            self.state = 285
            self.cond()
            self.state = 286
            self.type_()
            self.state = 287
            self.value()
            self.state = 288
            self.match(llvmParser.T__19)
            self.state = 289
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return llvmParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)




    def cond(self):

        localctx = llvmParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_cond)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 138538465099776) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PhiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Privatevariable(self):
            return self.getToken(llvmParser.Privatevariable, 0)

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.ValueContext)
            else:
                return self.getTypedRuleContext(llvmParser.ValueContext,i)


        def Label(self, i:int=None):
            if i is None:
                return self.getTokens(llvmParser.Label)
            else:
                return self.getToken(llvmParser.Label, i)

        def getRuleIndex(self):
            return llvmParser.RULE_phi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPhi" ):
                listener.enterPhi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPhi" ):
                listener.exitPhi(self)




    def phi(self):

        localctx = llvmParser.PhiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_phi)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(llvmParser.Privatevariable)
            self.state = 294
            self.match(llvmParser.T__10)
            self.state = 295
            self.match(llvmParser.T__46)
            self.state = 296
            self.type_()
            self.state = 297
            self.match(llvmParser.T__13)
            self.state = 298
            self.value()
            self.state = 299
            self.match(llvmParser.T__19)
            self.state = 300
            self.match(llvmParser.T__35)
            self.state = 301
            self.match(llvmParser.Label)
            self.state = 302
            self.match(llvmParser.T__16)
            self.state = 311 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 303
                self.match(llvmParser.T__19)
                self.state = 304
                self.match(llvmParser.T__13)
                self.state = 305
                self.value()
                self.state = 306
                self.match(llvmParser.T__19)
                self.state = 307
                self.match(llvmParser.T__35)
                self.state = 308
                self.match(llvmParser.Label)
                self.state = 309
                self.match(llvmParser.T__16)
                self.state = 313 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==20):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Privatevariable(self):
            return self.getToken(llvmParser.Privatevariable, 0)

        def constant(self):
            return self.getTypedRuleContext(llvmParser.ConstantContext,0)


        def Global_var(self):
            return self.getToken(llvmParser.Global_var, 0)

        def getRuleIndex(self):
            return llvmParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = llvmParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_value)
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.match(llvmParser.Privatevariable)
                pass
            elif token in [48, 49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.constant()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 3)
                self.state = 317
                self.match(llvmParser.Global_var)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(llvmParser.INTEGER, 0)

        def getRuleIndex(self):
            return llvmParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = llvmParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            _la = self._input.LA(1)
            if not(_la==48 or _la==49):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_constantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Global_var(self):
            return self.getToken(llvmParser.Global_var, 0)

        def getRuleIndex(self):
            return llvmParser.RULE_string_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_constant" ):
                listener.enterString_constant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_constant" ):
                listener.exitString_constant(self)




    def string_constant(self):

        localctx = llvmParser.String_constantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_string_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(llvmParser.Global_var)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





