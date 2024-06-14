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
        4,1,23,130,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,
        1,2,4,2,29,8,2,11,2,12,2,30,1,2,1,2,1,2,4,2,36,8,2,11,2,12,2,37,
        1,2,1,2,1,2,4,2,43,8,2,11,2,12,2,44,1,2,1,2,1,2,4,2,50,8,2,11,2,
        12,2,51,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,98,8,
        2,3,2,100,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,
        2,114,8,2,10,2,12,2,117,9,2,1,3,1,3,1,3,1,3,5,3,123,8,3,10,3,12,
        3,126,9,3,1,3,1,3,1,3,0,1,4,4,0,2,4,6,0,2,1,0,10,11,1,0,12,13,152,
        0,9,1,0,0,0,2,22,1,0,0,0,4,99,1,0,0,0,6,118,1,0,0,0,8,10,3,2,1,0,
        9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,1,1,0,0,
        0,13,14,3,4,2,0,14,15,5,22,0,0,15,23,1,0,0,0,16,17,5,19,0,0,17,18,
        5,1,0,0,18,19,3,4,2,0,19,20,5,22,0,0,20,23,1,0,0,0,21,23,5,22,0,
        0,22,13,1,0,0,0,22,16,1,0,0,0,22,21,1,0,0,0,23,3,1,0,0,0,24,25,6,
        2,-1,0,25,28,3,6,3,0,26,27,5,12,0,0,27,29,3,6,3,0,28,26,1,0,0,0,
        29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,100,1,0,0,0,32,35,3,
        6,3,0,33,34,5,13,0,0,34,36,3,6,3,0,35,33,1,0,0,0,36,37,1,0,0,0,37,
        35,1,0,0,0,37,38,1,0,0,0,38,100,1,0,0,0,39,42,3,6,3,0,40,41,5,10,
        0,0,41,43,3,6,3,0,42,40,1,0,0,0,43,44,1,0,0,0,44,42,1,0,0,0,44,45,
        1,0,0,0,45,100,1,0,0,0,46,49,3,6,3,0,47,48,5,10,0,0,48,50,3,6,3,
        0,49,47,1,0,0,0,50,51,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,100,
        1,0,0,0,53,54,5,8,0,0,54,55,5,3,0,0,55,56,3,6,3,0,56,57,5,4,0,0,
        57,100,1,0,0,0,58,59,5,9,0,0,59,60,5,3,0,0,60,61,3,6,3,0,61,62,5,
        4,0,0,62,100,1,0,0,0,63,100,3,6,3,0,64,100,5,21,0,0,65,100,5,20,
        0,0,66,100,5,19,0,0,67,68,5,3,0,0,68,69,3,4,2,0,69,70,5,4,0,0,70,
        100,1,0,0,0,71,72,5,14,0,0,72,73,5,3,0,0,73,74,3,4,2,0,74,75,5,4,
        0,0,75,100,1,0,0,0,76,77,5,15,0,0,77,78,5,3,0,0,78,79,3,4,2,0,79,
        80,5,4,0,0,80,100,1,0,0,0,81,82,5,16,0,0,82,83,5,3,0,0,83,84,3,4,
        2,0,84,85,5,4,0,0,85,100,1,0,0,0,86,97,5,18,0,0,87,88,5,3,0,0,88,
        89,3,4,2,0,89,90,5,4,0,0,90,98,1,0,0,0,91,92,5,3,0,0,92,93,3,4,2,
        0,93,94,5,5,0,0,94,95,3,4,2,0,95,96,5,4,0,0,96,98,1,0,0,0,97,87,
        1,0,0,0,97,91,1,0,0,0,98,100,1,0,0,0,99,24,1,0,0,0,99,32,1,0,0,0,
        99,39,1,0,0,0,99,46,1,0,0,0,99,53,1,0,0,0,99,58,1,0,0,0,99,63,1,
        0,0,0,99,64,1,0,0,0,99,65,1,0,0,0,99,66,1,0,0,0,99,67,1,0,0,0,99,
        71,1,0,0,0,99,76,1,0,0,0,99,81,1,0,0,0,99,86,1,0,0,0,100,115,1,0,
        0,0,101,102,10,19,0,0,102,103,7,0,0,0,103,114,3,4,2,20,104,105,10,
        18,0,0,105,106,7,1,0,0,106,114,3,4,2,19,107,108,10,17,0,0,108,109,
        5,2,0,0,109,114,3,4,2,18,110,111,10,2,0,0,111,112,5,17,0,0,112,114,
        3,4,2,3,113,101,1,0,0,0,113,104,1,0,0,0,113,107,1,0,0,0,113,110,
        1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,5,1,
        0,0,0,117,115,1,0,0,0,118,119,5,6,0,0,119,124,3,4,2,0,120,121,5,
        5,0,0,121,123,3,4,2,0,122,120,1,0,0,0,123,126,1,0,0,0,124,122,1,
        0,0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,124,1,0,0,0,127,128,5,
        7,0,0,128,7,1,0,0,0,11,11,22,30,37,44,51,97,99,113,115,124
    ]

class calculadoraPrimeroMultParser ( Parser ):

    grammarFileName = "calculadoraPrimeroMult.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'^'", "'('", "')'", "','", "'['", 
                     "']'", "'inverse'", "'transposed'", "'*'", "'/'", "'+'", 
                     "'-'", "'sin'", "'cos'", "'tan'", "'%'", "'root'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INVERSE", "TRANSPOSED", "MUL", "DIV", "ADD", "SUB", 
                      "SIN", "COS", "TAN", "MOD", "RAIZ", "ID", "INT", "FLOAT", 
                      "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_matrix = 3

    ruleNames =  [ "prog", "stat", "expr", "matrix" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    INVERSE=8
    TRANSPOSED=9
    MUL=10
    DIV=11
    ADD=12
    SUB=13
    SIN=14
    COS=15
    TAN=16
    MOD=17
    RAIZ=18
    ID=19
    INT=20
    FLOAT=21
    NEWLINE=22
    WS=23

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
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.stat()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8241992) != 0)):
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


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(calculadoraPrimeroMultParser.NEWLINE, 0)

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


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraPrimeroMultParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(calculadoraPrimeroMultParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(calculadoraPrimeroMultParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(calculadoraPrimeroMultParser.NEWLINE, 0)

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



    def stat(self):

        localctx = calculadoraPrimeroMultParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = calculadoraPrimeroMultParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.expr(0)
                self.state = 14
                self.match(calculadoraPrimeroMultParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = calculadoraPrimeroMultParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(calculadoraPrimeroMultParser.ID)
                self.state = 17
                self.match(calculadoraPrimeroMultParser.T__0)
                self.state = 18
                self.expr(0)
                self.state = 19
                self.match(calculadoraPrimeroMultParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = calculadoraPrimeroMultParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.match(calculadoraPrimeroMultParser.NEWLINE)
                pass


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
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = calculadoraPrimeroMultParser.MatrixAddContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 25
                self.matrix()
                self.state = 28 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 26
                        self.match(calculadoraPrimeroMultParser.ADD)
                        self.state = 27
                        self.matrix()

                    else:
                        raise NoViableAltException(self)
                    self.state = 30 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass

            elif la_ == 2:
                localctx = calculadoraPrimeroMultParser.MatrixSubtractContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 32
                self.matrix()
                self.state = 35 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 33
                        self.match(calculadoraPrimeroMultParser.SUB)
                        self.state = 34
                        self.matrix()

                    else:
                        raise NoViableAltException(self)
                    self.state = 37 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass

            elif la_ == 3:
                localctx = calculadoraPrimeroMultParser.MatrixMultiplyContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                self.matrix()
                self.state = 42 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 40
                        self.match(calculadoraPrimeroMultParser.MUL)
                        self.state = 41
                        self.matrix()

                    else:
                        raise NoViableAltException(self)
                    self.state = 44 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass

            elif la_ == 4:
                localctx = calculadoraPrimeroMultParser.MatrixMultiplyContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 46
                self.matrix()
                self.state = 49 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 47
                        self.match(calculadoraPrimeroMultParser.MUL)
                        self.state = 48
                        self.matrix()

                    else:
                        raise NoViableAltException(self)
                    self.state = 51 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass

            elif la_ == 5:
                localctx = calculadoraPrimeroMultParser.MatrixInverseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 53
                self.match(calculadoraPrimeroMultParser.INVERSE)
                self.state = 54
                self.match(calculadoraPrimeroMultParser.T__2)
                self.state = 55
                self.matrix()
                self.state = 56
                self.match(calculadoraPrimeroMultParser.T__3)
                pass

            elif la_ == 6:
                localctx = calculadoraPrimeroMultParser.MatrixTransposedContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 58
                self.match(calculadoraPrimeroMultParser.TRANSPOSED)
                self.state = 59
                self.match(calculadoraPrimeroMultParser.T__2)
                self.state = 60
                self.matrix()
                self.state = 61
                self.match(calculadoraPrimeroMultParser.T__3)
                pass

            elif la_ == 7:
                localctx = calculadoraPrimeroMultParser.IdMatrixContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self.matrix()
                pass

            elif la_ == 8:
                localctx = calculadoraPrimeroMultParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                self.match(calculadoraPrimeroMultParser.FLOAT)
                pass

            elif la_ == 9:
                localctx = calculadoraPrimeroMultParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 65
                self.match(calculadoraPrimeroMultParser.INT)
                pass

            elif la_ == 10:
                localctx = calculadoraPrimeroMultParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 66
                self.match(calculadoraPrimeroMultParser.ID)
                pass

            elif la_ == 11:
                localctx = calculadoraPrimeroMultParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 67
                self.match(calculadoraPrimeroMultParser.T__2)
                self.state = 68
                self.expr(0)
                self.state = 69
                self.match(calculadoraPrimeroMultParser.T__3)
                pass

            elif la_ == 12:
                localctx = calculadoraPrimeroMultParser.SinContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 71
                self.match(calculadoraPrimeroMultParser.SIN)
                self.state = 72
                self.match(calculadoraPrimeroMultParser.T__2)
                self.state = 73
                self.expr(0)
                self.state = 74
                self.match(calculadoraPrimeroMultParser.T__3)
                pass

            elif la_ == 13:
                localctx = calculadoraPrimeroMultParser.CosContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 76
                self.match(calculadoraPrimeroMultParser.COS)
                self.state = 77
                self.match(calculadoraPrimeroMultParser.T__2)
                self.state = 78
                self.expr(0)
                self.state = 79
                self.match(calculadoraPrimeroMultParser.T__3)
                pass

            elif la_ == 14:
                localctx = calculadoraPrimeroMultParser.TanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 81
                self.match(calculadoraPrimeroMultParser.TAN)
                self.state = 82
                self.match(calculadoraPrimeroMultParser.T__2)
                self.state = 83
                self.expr(0)
                self.state = 84
                self.match(calculadoraPrimeroMultParser.T__3)
                pass

            elif la_ == 15:
                localctx = calculadoraPrimeroMultParser.RaizContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 86
                self.match(calculadoraPrimeroMultParser.RAIZ)
                self.state = 97
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 87
                    self.match(calculadoraPrimeroMultParser.T__2)
                    self.state = 88
                    self.expr(0)
                    self.state = 89
                    self.match(calculadoraPrimeroMultParser.T__3)
                    pass

                elif la_ == 2:
                    self.state = 91
                    self.match(calculadoraPrimeroMultParser.T__2)
                    self.state = 92
                    self.expr(0)
                    self.state = 93
                    self.match(calculadoraPrimeroMultParser.T__4)
                    self.state = 94
                    self.expr(0)
                    self.state = 95
                    self.match(calculadoraPrimeroMultParser.T__3)
                    pass


                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 115
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 113
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = calculadoraPrimeroMultParser.MulDivContext(self, calculadoraPrimeroMultParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 101
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 102
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 103
                        self.expr(20)
                        pass

                    elif la_ == 2:
                        localctx = calculadoraPrimeroMultParser.AddSubContext(self, calculadoraPrimeroMultParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 104
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 105
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 106
                        self.expr(19)
                        pass

                    elif la_ == 3:
                        localctx = calculadoraPrimeroMultParser.PowContext(self, calculadoraPrimeroMultParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 107
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 108
                        self.match(calculadoraPrimeroMultParser.T__1)
                        self.state = 109
                        self.expr(18)
                        pass

                    elif la_ == 4:
                        localctx = calculadoraPrimeroMultParser.ModContext(self, calculadoraPrimeroMultParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 110
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 111
                        self.match(calculadoraPrimeroMultParser.MOD)
                        self.state = 112
                        self.expr(3)
                        pass

             
                self.state = 117
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
        self.enterRule(localctx, 6, self.RULE_matrix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(calculadoraPrimeroMultParser.T__5)
            self.state = 119
            self.expr(0)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 120
                self.match(calculadoraPrimeroMultParser.T__4)
                self.state = 121
                self.expr(0)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
            self.match(calculadoraPrimeroMultParser.T__6)
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
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




