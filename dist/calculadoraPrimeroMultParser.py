# Generated from calculadoraPrimeroMult.g4 by ANTLR 4.13.1
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
        4,1,45,249,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,1,1,1,1,1,1,1,3,1,22,8,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,4,2,33,8,2,11,2,12,2,34,1,2,1,2,1,2,4,2,40,8,
        2,11,2,12,2,41,1,2,1,2,1,2,4,2,47,8,2,11,2,12,2,48,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,98,8,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,109,8,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,157,8,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,171,8,2,10,2,12,2,174,9,2,1,3,1,
        3,1,3,1,3,1,3,5,3,181,8,3,10,3,12,3,184,9,3,1,3,5,3,187,8,3,10,3,
        12,3,190,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,3,4,225,8,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,233,8,4,
        10,4,12,4,236,9,4,1,5,1,5,1,5,1,5,5,5,242,8,5,10,5,12,5,245,9,5,
        1,5,1,5,1,5,0,2,4,8,6,0,2,4,6,8,10,0,2,1,0,32,33,1,0,34,35,287,0,
        13,1,0,0,0,2,21,1,0,0,0,4,156,1,0,0,0,6,175,1,0,0,0,8,224,1,0,0,
        0,10,237,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,15,1,0,0,0,15,13,
        1,0,0,0,15,16,1,0,0,0,16,1,1,0,0,0,17,18,3,4,2,0,18,19,5,44,0,0,
        19,22,1,0,0,0,20,22,5,44,0,0,21,17,1,0,0,0,21,20,1,0,0,0,22,3,1,
        0,0,0,23,24,6,2,-1,0,24,25,5,23,0,0,25,26,5,1,0,0,26,27,3,4,2,0,
        27,28,5,2,0,0,28,157,1,0,0,0,29,32,3,10,5,0,30,31,5,34,0,0,31,33,
        3,10,5,0,32,30,1,0,0,0,33,34,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,
        35,157,1,0,0,0,36,39,3,10,5,0,37,38,5,35,0,0,38,40,3,10,5,0,39,37,
        1,0,0,0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,157,1,0,0,0,
        43,46,3,10,5,0,44,45,5,32,0,0,45,47,3,10,5,0,46,44,1,0,0,0,47,48,
        1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,157,1,0,0,0,50,51,5,30,0,
        0,51,52,5,1,0,0,52,53,3,10,5,0,53,54,5,2,0,0,54,157,1,0,0,0,55,56,
        5,31,0,0,56,57,5,1,0,0,57,58,3,10,5,0,58,59,5,2,0,0,59,157,1,0,0,
        0,60,157,3,10,5,0,61,157,5,43,0,0,62,157,5,42,0,0,63,157,5,41,0,
        0,64,65,5,41,0,0,65,66,5,4,0,0,66,157,3,4,2,14,67,68,5,1,0,0,68,
        69,3,4,2,0,69,70,5,2,0,0,70,157,1,0,0,0,71,72,5,36,0,0,72,73,5,1,
        0,0,73,74,3,4,2,0,74,75,5,2,0,0,75,157,1,0,0,0,76,77,5,37,0,0,77,
        78,5,1,0,0,78,79,3,4,2,0,79,80,5,2,0,0,80,157,1,0,0,0,81,82,5,38,
        0,0,82,83,5,1,0,0,83,84,3,4,2,0,84,85,5,2,0,0,85,157,1,0,0,0,86,
        97,5,40,0,0,87,88,5,1,0,0,88,89,3,4,2,0,89,90,5,2,0,0,90,98,1,0,
        0,0,91,92,5,1,0,0,92,93,3,4,2,0,93,94,5,5,0,0,94,95,3,4,2,0,95,96,
        5,2,0,0,96,98,1,0,0,0,97,87,1,0,0,0,97,91,1,0,0,0,98,157,1,0,0,0,
        99,100,5,21,0,0,100,101,5,1,0,0,101,102,3,8,4,0,102,103,5,2,0,0,
        103,104,5,6,0,0,104,108,3,6,3,0,105,106,5,22,0,0,106,107,5,6,0,0,
        107,109,3,6,3,0,108,105,1,0,0,0,108,109,1,0,0,0,109,157,1,0,0,0,
        110,111,5,24,0,0,111,112,5,1,0,0,112,113,5,41,0,0,113,114,5,4,0,
        0,114,115,3,4,2,0,115,116,5,7,0,0,116,117,5,41,0,0,117,118,5,4,0,
        0,118,119,3,4,2,0,119,120,5,2,0,0,120,121,5,6,0,0,121,122,3,6,3,
        0,122,157,1,0,0,0,123,124,5,25,0,0,124,125,5,1,0,0,125,126,3,8,4,
        0,126,127,5,2,0,0,127,128,5,6,0,0,128,129,3,6,3,0,129,157,1,0,0,
        0,130,131,5,26,0,0,131,132,5,1,0,0,132,133,3,4,2,0,133,134,5,5,0,
        0,134,135,3,4,2,0,135,136,5,2,0,0,136,157,1,0,0,0,137,138,5,27,0,
        0,138,139,5,1,0,0,139,140,3,4,2,0,140,141,5,5,0,0,141,142,3,4,2,
        0,142,143,5,2,0,0,143,157,1,0,0,0,144,145,5,28,0,0,145,146,5,1,0,
        0,146,147,3,4,2,0,147,148,5,5,0,0,148,149,3,4,2,0,149,150,5,2,0,
        0,150,157,1,0,0,0,151,152,5,29,0,0,152,153,5,1,0,0,153,154,3,4,2,
        0,154,155,5,2,0,0,155,157,1,0,0,0,156,23,1,0,0,0,156,29,1,0,0,0,
        156,36,1,0,0,0,156,43,1,0,0,0,156,50,1,0,0,0,156,55,1,0,0,0,156,
        60,1,0,0,0,156,61,1,0,0,0,156,62,1,0,0,0,156,63,1,0,0,0,156,64,1,
        0,0,0,156,67,1,0,0,0,156,71,1,0,0,0,156,76,1,0,0,0,156,81,1,0,0,
        0,156,86,1,0,0,0,156,99,1,0,0,0,156,110,1,0,0,0,156,123,1,0,0,0,
        156,130,1,0,0,0,156,137,1,0,0,0,156,144,1,0,0,0,156,151,1,0,0,0,
        157,172,1,0,0,0,158,159,10,26,0,0,159,160,7,0,0,0,160,171,3,4,2,
        27,161,162,10,25,0,0,162,163,7,1,0,0,163,171,3,4,2,26,164,165,10,
        24,0,0,165,166,5,3,0,0,166,171,3,4,2,25,167,168,10,9,0,0,168,169,
        5,39,0,0,169,171,3,4,2,10,170,158,1,0,0,0,170,161,1,0,0,0,170,164,
        1,0,0,0,170,167,1,0,0,0,171,174,1,0,0,0,172,170,1,0,0,0,172,173,
        1,0,0,0,173,5,1,0,0,0,174,172,1,0,0,0,175,176,5,8,0,0,176,182,5,
        44,0,0,177,178,3,4,2,0,178,179,5,44,0,0,179,181,1,0,0,0,180,177,
        1,0,0,0,181,184,1,0,0,0,182,180,1,0,0,0,182,183,1,0,0,0,183,188,
        1,0,0,0,184,182,1,0,0,0,185,187,5,44,0,0,186,185,1,0,0,0,187,190,
        1,0,0,0,188,186,1,0,0,0,188,189,1,0,0,0,189,191,1,0,0,0,190,188,
        1,0,0,0,191,192,5,9,0,0,192,7,1,0,0,0,193,194,6,4,-1,0,194,195,3,
        4,2,0,195,196,5,10,0,0,196,197,3,4,2,0,197,225,1,0,0,0,198,199,3,
        4,2,0,199,200,5,11,0,0,200,201,3,4,2,0,201,225,1,0,0,0,202,203,3,
        4,2,0,203,204,5,12,0,0,204,205,3,4,2,0,205,225,1,0,0,0,206,207,3,
        4,2,0,207,208,5,13,0,0,208,209,3,4,2,0,209,225,1,0,0,0,210,211,3,
        4,2,0,211,212,5,14,0,0,212,213,3,4,2,0,213,225,1,0,0,0,214,215,3,
        4,2,0,215,216,5,15,0,0,216,217,3,4,2,0,217,225,1,0,0,0,218,219,5,
        18,0,0,219,225,3,8,4,2,220,221,5,1,0,0,221,222,3,8,4,0,222,223,5,
        2,0,0,223,225,1,0,0,0,224,193,1,0,0,0,224,198,1,0,0,0,224,202,1,
        0,0,0,224,206,1,0,0,0,224,210,1,0,0,0,224,214,1,0,0,0,224,218,1,
        0,0,0,224,220,1,0,0,0,225,234,1,0,0,0,226,227,10,4,0,0,227,228,5,
        16,0,0,228,233,3,8,4,5,229,230,10,3,0,0,230,231,5,17,0,0,231,233,
        3,8,4,4,232,226,1,0,0,0,232,229,1,0,0,0,233,236,1,0,0,0,234,232,
        1,0,0,0,234,235,1,0,0,0,235,9,1,0,0,0,236,234,1,0,0,0,237,238,5,
        19,0,0,238,243,3,4,2,0,239,240,5,5,0,0,240,242,3,4,2,0,241,239,1,
        0,0,0,242,245,1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,246,1,
        0,0,0,245,243,1,0,0,0,246,247,5,20,0,0,247,11,1,0,0,0,16,15,21,34,
        41,48,97,108,156,170,172,182,188,224,232,234,243
    ]

class calculadoraPrimeroMultParser ( Parser ):

    grammarFileName = "calculadoraPrimeroMult.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'^'", "'='", "','", "'->'", 
                     "';'", "'{'", "'}'", "'<'", "'>'", "'<='", "'>='", 
                     "'=='", "'!='", "'&&'", "'||'", "'!'", "'['", "']'", 
                     "'if'", "'else'", "'show'", "'for'", "'while'", "'paint'", 
                     "'paintball'", "'paintbars'", "'brownie'", "'inverse'", 
                     "'transposed'", "'*'", "'/'", "'+'", "'-'", "'sin'", 
                     "'cos'", "'tan'", "'%'", "'root'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IF", "ELSE", "SHOW", "FOR", "WHILE", 
                      "PAINT", "PAINTBALL", "PAINTBARS", "BROWNIE", "INVERSE", 
                      "TRANSPOSED", "MUL", "DIV", "ADD", "SUB", "SIN", "COS", 
                      "TAN", "MOD", "RAIZ", "ID", "INT", "FLOAT", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_block = 3
    RULE_cond = 4
    RULE_matrix = 5

    ruleNames =  [ "prog", "stat", "expr", "block", "cond", "matrix" ]

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
    IF=21
    ELSE=22
    SHOW=23
    FOR=24
    WHILE=25
    PAINT=26
    PAINTBALL=27
    PAINTBARS=28
    BROWNIE=29
    INVERSE=30
    TRANSPOSED=31
    MUL=32
    DIV=33
    ADD=34
    SUB=35
    SIN=36
    COS=37
    TAN=38
    MOD=39
    RAIZ=40
    ID=41
    INT=42
    FLOAT=43
    NEWLINE=44
    WS=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.StatContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.StatContext,i)


        def getRuleIndex(self):
            return calculadoraPrimeroMultParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = calculadoraPrimeroMultParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.stat()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 34570185998338) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return calculadoraPrimeroMultParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(calculadoraPrimeroMultParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(calculadoraPrimeroMultParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = calculadoraPrimeroMultParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 19, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 36, 37, 38, 40, 41, 42, 43]:
                localctx = calculadoraPrimeroMultParser.ExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.expr(0)
                self.state = 18
                self.match(calculadoraPrimeroMultParser.NEWLINE)
                pass
            elif token in [44]:
                localctx = calculadoraPrimeroMultParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(calculadoraPrimeroMultParser.NEWLINE)
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return calculadoraPrimeroMultParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MatrixAddContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def matrix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.MatrixContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.MatrixContext,i)

        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(calculadoraPrimeroMultParser.ADD)
            else:
                return self.getToken(calculadoraPrimeroMultParser.ADD, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixAdd" ):
                listener.enterMatrixAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixAdd" ):
                listener.exitMatrixAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixAdd" ):
                return visitor.visitMatrixAdd(self)
            else:
                return visitor.visitChildren(self)


    class IdMatrixContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def matrix(self):
            return self.getTypedRuleContext(calculadoraPrimeroMultParser.MatrixContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdMatrix" ):
                listener.enterIdMatrix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdMatrix" ):
                listener.exitIdMatrix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdMatrix" ):
                return visitor.visitIdMatrix(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,i)

        def MUL(self):
            return self.getToken(calculadoraPrimeroMultParser.MUL, 0)
        def DIV(self):
            return self.getToken(calculadoraPrimeroMultParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class CosContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COS(self):
            return self.getToken(calculadoraPrimeroMultParser.COS, 0)
        def expr(self):
            return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCos" ):
                listener.enterCos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCos" ):
                listener.exitCos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCos" ):
                return visitor.visitCos(self)
            else:
                return visitor.visitChildren(self)


    class ForContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(calculadoraPrimeroMultParser.FOR, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(calculadoraPrimeroMultParser.ID)
            else:
                return self.getToken(calculadoraPrimeroMultParser.ID, i)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,i)

        def block(self):
            return self.getTypedRuleContext(calculadoraPrimeroMultParser.BlockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor" ):
                listener.enterFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor" ):
                listener.exitFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor" ):
                return visitor.visitFor(self)
            else:
                return visitor.visitChildren(self)


    class PaintContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PAINT(self):
            return self.getToken(calculadoraPrimeroMultParser.PAINT, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPaint" ):
                listener.enterPaint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPaint" ):
                listener.exitPaint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPaint" ):
                return visitor.visitPaint(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(calculadoraPrimeroMultParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(calculadoraPrimeroMultParser.WHILE, 0)
        def cond(self):
            return self.getTypedRuleContext(calculadoraPrimeroMultParser.CondContext,0)

        def block(self):
            return self.getTypedRuleContext(calculadoraPrimeroMultParser.BlockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class MatrixTransposedContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRANSPOSED(self):
            return self.getToken(calculadoraPrimeroMultParser.TRANSPOSED, 0)
        def matrix(self):
            return self.getTypedRuleContext(calculadoraPrimeroMultParser.MatrixContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixTransposed" ):
                listener.enterMatrixTransposed(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixTransposed" ):
                listener.exitMatrixTransposed(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixTransposed" ):
                return visitor.visitMatrixTransposed(self)
            else:
                return visitor.visitChildren(self)


    class RaizContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RAIZ(self):
            return self.getToken(calculadoraPrimeroMultParser.RAIZ, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaiz" ):
                listener.enterRaiz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaiz" ):
                listener.exitRaiz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaiz" ):
                return visitor.visitRaiz(self)
            else:
                return visitor.visitChildren(self)


    class PaintBallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PAINTBALL(self):
            return self.getToken(calculadoraPrimeroMultParser.PAINTBALL, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPaintBall" ):
                listener.enterPaintBall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPaintBall" ):
                listener.exitPaintBall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPaintBall" ):
                return visitor.visitPaintBall(self)
            else:
                return visitor.visitChildren(self)


    class ConditionalIfContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(calculadoraPrimeroMultParser.IF, 0)
        def cond(self):
            return self.getTypedRuleContext(calculadoraPrimeroMultParser.CondContext,0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.BlockContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.BlockContext,i)

        def ELSE(self):
            return self.getToken(calculadoraPrimeroMultParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalIf" ):
                listener.enterConditionalIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalIf" ):
                listener.exitConditionalIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalIf" ):
                return visitor.visitConditionalIf(self)
            else:
                return visitor.visitChildren(self)


    class PaintBarsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PAINTBARS(self):
            return self.getToken(calculadoraPrimeroMultParser.PAINTBARS, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPaintBars" ):
                listener.enterPaintBars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPaintBars" ):
                listener.exitPaintBars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPaintBars" ):
                return visitor.visitPaintBars(self)
            else:
                return visitor.visitChildren(self)


    class SinContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIN(self):
            return self.getToken(calculadoraPrimeroMultParser.SIN, 0)
        def expr(self):
            return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSin" ):
                listener.enterSin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSin" ):
                listener.exitSin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSin" ):
                return visitor.visitSin(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(calculadoraPrimeroMultParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class MatrixMultiplyContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def matrix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.MatrixContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.MatrixContext,i)

        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(calculadoraPrimeroMultParser.MUL)
            else:
                return self.getToken(calculadoraPrimeroMultParser.MUL, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixMultiply" ):
                listener.enterMatrixMultiply(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixMultiply" ):
                listener.exitMatrixMultiply(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixMultiply" ):
                return visitor.visitMatrixMultiply(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SHOW(self):
            return self.getToken(calculadoraPrimeroMultParser.SHOW, 0)
        def expr(self):
            return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)


    class TanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TAN(self):
            return self.getToken(calculadoraPrimeroMultParser.TAN, 0)
        def expr(self):
            return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTan" ):
                listener.enterTan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTan" ):
                listener.exitTan(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTan" ):
                return visitor.visitTan(self)
            else:
                return visitor.visitChildren(self)


    class ModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,i)

        def MOD(self):
            return self.getToken(calculadoraPrimeroMultParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMod" ):
                listener.enterMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMod" ):
                listener.exitMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMod" ):
                return visitor.visitMod(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,i)

        def ADD(self):
            return self.getToken(calculadoraPrimeroMultParser.ADD, 0)
        def SUB(self):
            return self.getToken(calculadoraPrimeroMultParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class MatrixSubtractContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def matrix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.MatrixContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.MatrixContext,i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(calculadoraPrimeroMultParser.SUB)
            else:
                return self.getToken(calculadoraPrimeroMultParser.SUB, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixSubtract" ):
                listener.enterMatrixSubtract(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixSubtract" ):
                listener.exitMatrixSubtract(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixSubtract" ):
                return visitor.visitMatrixSubtract(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(calculadoraPrimeroMultParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class PaintBrownieContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BROWNIE(self):
            return self.getToken(calculadoraPrimeroMultParser.BROWNIE, 0)
        def expr(self):
            return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPaintBrownie" ):
                listener.enterPaintBrownie(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPaintBrownie" ):
                listener.exitPaintBrownie(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPaintBrownie" ):
                return visitor.visitPaintBrownie(self)
            else:
                return visitor.visitChildren(self)


    class MatrixInverseContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INVERSE(self):
            return self.getToken(calculadoraPrimeroMultParser.INVERSE, 0)
        def matrix(self):
            return self.getTypedRuleContext(calculadoraPrimeroMultParser.MatrixContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixInverse" ):
                listener.enterMatrixInverse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixInverse" ):
                listener.exitMatrixInverse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixInverse" ):
                return visitor.visitMatrixInverse(self)
            else:
                return visitor.visitChildren(self)


    class PowContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPow" ):
                listener.enterPow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPow" ):
                listener.exitPow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPow" ):
                return visitor.visitPow(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(calculadoraPrimeroMultParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = calculadoraPrimeroMultParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = calculadoraPrimeroMultParser.PrintExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 24
                self.match(calculadoraPrimeroMultParser.SHOW)
                self.state = 25
                self.match(calculadoraPrimeroMultParser.T__0)
                self.state = 26
                self.expr(0)
                self.state = 27
                self.match(calculadoraPrimeroMultParser.T__1)
                pass

            elif la_ == 2:
                localctx = calculadoraPrimeroMultParser.MatrixAddContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self.matrix()
                self.state = 32 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 30
                        self.match(calculadoraPrimeroMultParser.ADD)
                        self.state = 31
                        self.matrix()

                    else:
                        raise NoViableAltException(self)
                    self.state = 34 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass

            elif la_ == 3:
                localctx = calculadoraPrimeroMultParser.MatrixSubtractContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 36
                self.matrix()
                self.state = 39 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 37
                        self.match(calculadoraPrimeroMultParser.SUB)
                        self.state = 38
                        self.matrix()

                    else:
                        raise NoViableAltException(self)
                    self.state = 41 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass

            elif la_ == 4:
                localctx = calculadoraPrimeroMultParser.MatrixMultiplyContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                self.matrix()
                self.state = 46 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 44
                        self.match(calculadoraPrimeroMultParser.MUL)
                        self.state = 45
                        self.matrix()

                    else:
                        raise NoViableAltException(self)
                    self.state = 48 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass

            elif la_ == 5:
                localctx = calculadoraPrimeroMultParser.MatrixInverseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 50
                self.match(calculadoraPrimeroMultParser.INVERSE)
                self.state = 51
                self.match(calculadoraPrimeroMultParser.T__0)
                self.state = 52
                self.matrix()
                self.state = 53
                self.match(calculadoraPrimeroMultParser.T__1)
                pass

            elif la_ == 6:
                localctx = calculadoraPrimeroMultParser.MatrixTransposedContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 55
                self.match(calculadoraPrimeroMultParser.TRANSPOSED)
                self.state = 56
                self.match(calculadoraPrimeroMultParser.T__0)
                self.state = 57
                self.matrix()
                self.state = 58
                self.match(calculadoraPrimeroMultParser.T__1)
                pass

            elif la_ == 7:
                localctx = calculadoraPrimeroMultParser.IdMatrixContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 60
                self.matrix()
                pass

            elif la_ == 8:
                localctx = calculadoraPrimeroMultParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 61
                self.match(calculadoraPrimeroMultParser.FLOAT)
                pass

            elif la_ == 9:
                localctx = calculadoraPrimeroMultParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 62
                self.match(calculadoraPrimeroMultParser.INT)
                pass

            elif la_ == 10:
                localctx = calculadoraPrimeroMultParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self.match(calculadoraPrimeroMultParser.ID)
                pass

            elif la_ == 11:
                localctx = calculadoraPrimeroMultParser.AssignContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                self.match(calculadoraPrimeroMultParser.ID)
                self.state = 65
                self.match(calculadoraPrimeroMultParser.T__3)
                self.state = 66
                self.expr(14)
                pass

            elif la_ == 12:
                localctx = calculadoraPrimeroMultParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 67
                self.match(calculadoraPrimeroMultParser.T__0)
                self.state = 68
                self.expr(0)
                self.state = 69
                self.match(calculadoraPrimeroMultParser.T__1)
                pass

            elif la_ == 13:
                localctx = calculadoraPrimeroMultParser.SinContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 71
                self.match(calculadoraPrimeroMultParser.SIN)
                self.state = 72
                self.match(calculadoraPrimeroMultParser.T__0)
                self.state = 73
                self.expr(0)
                self.state = 74
                self.match(calculadoraPrimeroMultParser.T__1)
                pass

            elif la_ == 14:
                localctx = calculadoraPrimeroMultParser.CosContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 76
                self.match(calculadoraPrimeroMultParser.COS)
                self.state = 77
                self.match(calculadoraPrimeroMultParser.T__0)
                self.state = 78
                self.expr(0)
                self.state = 79
                self.match(calculadoraPrimeroMultParser.T__1)
                pass

            elif la_ == 15:
                localctx = calculadoraPrimeroMultParser.TanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 81
                self.match(calculadoraPrimeroMultParser.TAN)
                self.state = 82
                self.match(calculadoraPrimeroMultParser.T__0)
                self.state = 83
                self.expr(0)
                self.state = 84
                self.match(calculadoraPrimeroMultParser.T__1)
                pass

            elif la_ == 16:
                localctx = calculadoraPrimeroMultParser.RaizContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 86
                self.match(calculadoraPrimeroMultParser.RAIZ)
                self.state = 97
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 87
                    self.match(calculadoraPrimeroMultParser.T__0)
                    self.state = 88
                    self.expr(0)
                    self.state = 89
                    self.match(calculadoraPrimeroMultParser.T__1)
                    pass

                elif la_ == 2:
                    self.state = 91
                    self.match(calculadoraPrimeroMultParser.T__0)
                    self.state = 92
                    self.expr(0)
                    self.state = 93
                    self.match(calculadoraPrimeroMultParser.T__4)
                    self.state = 94
                    self.expr(0)
                    self.state = 95
                    self.match(calculadoraPrimeroMultParser.T__1)
                    pass


                pass

            elif la_ == 17:
                localctx = calculadoraPrimeroMultParser.ConditionalIfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 99
                self.match(calculadoraPrimeroMultParser.IF)
                self.state = 100
                self.match(calculadoraPrimeroMultParser.T__0)
                self.state = 101
                self.cond(0)
                self.state = 102
                self.match(calculadoraPrimeroMultParser.T__1)
                self.state = 103
                self.match(calculadoraPrimeroMultParser.T__5)
                self.state = 104
                self.block()
                self.state = 108
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 105
                    self.match(calculadoraPrimeroMultParser.ELSE)
                    self.state = 106
                    self.match(calculadoraPrimeroMultParser.T__5)
                    self.state = 107
                    self.block()


                pass

            elif la_ == 18:
                localctx = calculadoraPrimeroMultParser.ForContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 110
                self.match(calculadoraPrimeroMultParser.FOR)
                self.state = 111
                self.match(calculadoraPrimeroMultParser.T__0)
                self.state = 112
                self.match(calculadoraPrimeroMultParser.ID)
                self.state = 113
                self.match(calculadoraPrimeroMultParser.T__3)
                self.state = 114
                self.expr(0)
                self.state = 115
                self.match(calculadoraPrimeroMultParser.T__6)
                self.state = 116
                self.match(calculadoraPrimeroMultParser.ID)
                self.state = 117
                self.match(calculadoraPrimeroMultParser.T__3)
                self.state = 118
                self.expr(0)
                self.state = 119
                self.match(calculadoraPrimeroMultParser.T__1)
                self.state = 120
                self.match(calculadoraPrimeroMultParser.T__5)
                self.state = 121
                self.block()
                pass

            elif la_ == 19:
                localctx = calculadoraPrimeroMultParser.WhileContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 123
                self.match(calculadoraPrimeroMultParser.WHILE)
                self.state = 124
                self.match(calculadoraPrimeroMultParser.T__0)
                self.state = 125
                self.cond(0)
                self.state = 126
                self.match(calculadoraPrimeroMultParser.T__1)
                self.state = 127
                self.match(calculadoraPrimeroMultParser.T__5)
                self.state = 128
                self.block()
                pass

            elif la_ == 20:
                localctx = calculadoraPrimeroMultParser.PaintContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 130
                self.match(calculadoraPrimeroMultParser.PAINT)
                self.state = 131
                self.match(calculadoraPrimeroMultParser.T__0)
                self.state = 132
                self.expr(0)
                self.state = 133
                self.match(calculadoraPrimeroMultParser.T__4)
                self.state = 134
                self.expr(0)
                self.state = 135
                self.match(calculadoraPrimeroMultParser.T__1)
                pass

            elif la_ == 21:
                localctx = calculadoraPrimeroMultParser.PaintBallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 137
                self.match(calculadoraPrimeroMultParser.PAINTBALL)
                self.state = 138
                self.match(calculadoraPrimeroMultParser.T__0)
                self.state = 139
                self.expr(0)
                self.state = 140
                self.match(calculadoraPrimeroMultParser.T__4)
                self.state = 141
                self.expr(0)
                self.state = 142
                self.match(calculadoraPrimeroMultParser.T__1)
                pass

            elif la_ == 22:
                localctx = calculadoraPrimeroMultParser.PaintBarsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 144
                self.match(calculadoraPrimeroMultParser.PAINTBARS)
                self.state = 145
                self.match(calculadoraPrimeroMultParser.T__0)
                self.state = 146
                self.expr(0)
                self.state = 147
                self.match(calculadoraPrimeroMultParser.T__4)
                self.state = 148
                self.expr(0)
                self.state = 149
                self.match(calculadoraPrimeroMultParser.T__1)
                pass

            elif la_ == 23:
                localctx = calculadoraPrimeroMultParser.PaintBrownieContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 151
                self.match(calculadoraPrimeroMultParser.BROWNIE)
                self.state = 152
                self.match(calculadoraPrimeroMultParser.T__0)
                self.state = 153
                self.expr(0)
                self.state = 154
                self.match(calculadoraPrimeroMultParser.T__1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 172
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 170
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = calculadoraPrimeroMultParser.MulDivContext(self, calculadoraPrimeroMultParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 158
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 159
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==32 or _la==33):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 160
                        self.expr(27)
                        pass

                    elif la_ == 2:
                        localctx = calculadoraPrimeroMultParser.AddSubContext(self, calculadoraPrimeroMultParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 161
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 162
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==34 or _la==35):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 163
                        self.expr(26)
                        pass

                    elif la_ == 3:
                        localctx = calculadoraPrimeroMultParser.PowContext(self, calculadoraPrimeroMultParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 164
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 165
                        self.match(calculadoraPrimeroMultParser.T__2)
                        self.state = 166
                        self.expr(25)
                        pass

                    elif la_ == 4:
                        localctx = calculadoraPrimeroMultParser.ModContext(self, calculadoraPrimeroMultParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 167
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 168
                        self.match(calculadoraPrimeroMultParser.MOD)
                        self.state = 169
                        self.expr(10)
                        pass

             
                self.state = 174
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(calculadoraPrimeroMultParser.NEWLINE)
            else:
                return self.getToken(calculadoraPrimeroMultParser.NEWLINE, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,i)


        def getRuleIndex(self):
            return calculadoraPrimeroMultParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = calculadoraPrimeroMultParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(calculadoraPrimeroMultParser.T__7)
            self.state = 176
            self.match(calculadoraPrimeroMultParser.NEWLINE)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16977999953922) != 0):
                self.state = 177
                self.expr(0)
                self.state = 178
                self.match(calculadoraPrimeroMultParser.NEWLINE)
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 185
                self.match(calculadoraPrimeroMultParser.NEWLINE)
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 191
            self.match(calculadoraPrimeroMultParser.T__8)
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
            return calculadoraPrimeroMultParser.RULE_cond

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class EqualContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqual" ):
                listener.enterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqual" ):
                listener.exitEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqual" ):
                return visitor.visitEqual(self)
            else:
                return visitor.visitChildren(self)


    class NotContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def cond(self):
            return self.getTypedRuleContext(calculadoraPrimeroMultParser.CondContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot" ):
                listener.enterNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot" ):
                listener.exitNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot" ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class GreaterEqualThanContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterEqualThan" ):
                listener.enterGreaterEqualThan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterEqualThan" ):
                listener.exitGreaterEqualThan(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterEqualThan" ):
                return visitor.visitGreaterEqualThan(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def cond(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.CondContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.CondContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def cond(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.CondContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.CondContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class LessThanContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessThan" ):
                listener.enterLessThan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessThan" ):
                listener.exitLessThan(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessThan" ):
                return visitor.visitLessThan(self)
            else:
                return visitor.visitChildren(self)


    class NotEqualContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotEqual" ):
                listener.enterNotEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotEqual" ):
                listener.exitNotEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotEqual" ):
                return visitor.visitNotEqual(self)
            else:
                return visitor.visitChildren(self)


    class LessEqualThanContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessEqualThan" ):
                listener.enterLessEqualThan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessEqualThan" ):
                listener.exitLessEqualThan(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessEqualThan" ):
                return visitor.visitLessEqualThan(self)
            else:
                return visitor.visitChildren(self)


    class GreaterThanContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterThan" ):
                listener.enterGreaterThan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterThan" ):
                listener.exitGreaterThan(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterThan" ):
                return visitor.visitGreaterThan(self)
            else:
                return visitor.visitChildren(self)


    class ParensCondContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def cond(self):
            return self.getTypedRuleContext(calculadoraPrimeroMultParser.CondContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensCond" ):
                listener.enterParensCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensCond" ):
                listener.exitParensCond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensCond" ):
                return visitor.visitParensCond(self)
            else:
                return visitor.visitChildren(self)



    def cond(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = calculadoraPrimeroMultParser.CondContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_cond, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = calculadoraPrimeroMultParser.LessThanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 194
                self.expr(0)
                self.state = 195
                self.match(calculadoraPrimeroMultParser.T__9)
                self.state = 196
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = calculadoraPrimeroMultParser.GreaterThanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 198
                self.expr(0)
                self.state = 199
                self.match(calculadoraPrimeroMultParser.T__10)
                self.state = 200
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = calculadoraPrimeroMultParser.LessEqualThanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 202
                self.expr(0)
                self.state = 203
                self.match(calculadoraPrimeroMultParser.T__11)
                self.state = 204
                self.expr(0)
                pass

            elif la_ == 4:
                localctx = calculadoraPrimeroMultParser.GreaterEqualThanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 206
                self.expr(0)
                self.state = 207
                self.match(calculadoraPrimeroMultParser.T__12)
                self.state = 208
                self.expr(0)
                pass

            elif la_ == 5:
                localctx = calculadoraPrimeroMultParser.EqualContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 210
                self.expr(0)
                self.state = 211
                self.match(calculadoraPrimeroMultParser.T__13)
                self.state = 212
                self.expr(0)
                pass

            elif la_ == 6:
                localctx = calculadoraPrimeroMultParser.NotEqualContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 214
                self.expr(0)
                self.state = 215
                self.match(calculadoraPrimeroMultParser.T__14)
                self.state = 216
                self.expr(0)
                pass

            elif la_ == 7:
                localctx = calculadoraPrimeroMultParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 218
                self.match(calculadoraPrimeroMultParser.T__17)
                self.state = 219
                self.cond(2)
                pass

            elif la_ == 8:
                localctx = calculadoraPrimeroMultParser.ParensCondContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 220
                self.match(calculadoraPrimeroMultParser.T__0)
                self.state = 221
                self.cond(0)
                self.state = 222
                self.match(calculadoraPrimeroMultParser.T__1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 234
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 232
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = calculadoraPrimeroMultParser.AndContext(self, calculadoraPrimeroMultParser.CondContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_cond)
                        self.state = 226
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 227
                        self.match(calculadoraPrimeroMultParser.T__15)
                        self.state = 228
                        self.cond(5)
                        pass

                    elif la_ == 2:
                        localctx = calculadoraPrimeroMultParser.OrContext(self, calculadoraPrimeroMultParser.CondContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_cond)
                        self.state = 229
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 230
                        self.match(calculadoraPrimeroMultParser.T__16)
                        self.state = 231
                        self.cond(4)
                        pass

             
                self.state = 236
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MatrixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraPrimeroMultParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,i)


        def getRuleIndex(self):
            return calculadoraPrimeroMultParser.RULE_matrix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrix" ):
                listener.enterMatrix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrix" ):
                listener.exitMatrix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrix" ):
                return visitor.visitMatrix(self)
            else:
                return visitor.visitChildren(self)




    def matrix(self):

        localctx = calculadoraPrimeroMultParser.MatrixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_matrix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(calculadoraPrimeroMultParser.T__18)
            self.state = 238
            self.expr(0)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 239
                self.match(calculadoraPrimeroMultParser.T__4)
                self.state = 240
                self.expr(0)
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 246
            self.match(calculadoraPrimeroMultParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        self._predicates[4] = self.cond_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

    def cond_sempred(self, localctx:CondContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         




