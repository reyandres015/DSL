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
        4,1,18,75,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,57,8,2,3,2,
        59,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,70,8,2,10,2,12,2,
        73,9,2,1,2,0,1,4,3,0,2,4,0,2,1,0,5,6,1,0,7,8,85,0,7,1,0,0,0,2,20,
        1,0,0,0,4,58,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,
        0,0,9,10,1,0,0,0,10,1,1,0,0,0,11,12,3,4,2,0,12,13,5,17,0,0,13,21,
        1,0,0,0,14,15,5,14,0,0,15,16,5,1,0,0,16,17,3,4,2,0,17,18,5,17,0,
        0,18,21,1,0,0,0,19,21,5,17,0,0,20,11,1,0,0,0,20,14,1,0,0,0,20,19,
        1,0,0,0,21,3,1,0,0,0,22,23,6,2,-1,0,23,59,5,16,0,0,24,59,5,15,0,
        0,25,59,5,14,0,0,26,27,5,2,0,0,27,28,3,4,2,0,28,29,5,3,0,0,29,59,
        1,0,0,0,30,31,5,9,0,0,31,32,5,2,0,0,32,33,3,4,2,0,33,34,5,3,0,0,
        34,59,1,0,0,0,35,36,5,10,0,0,36,37,5,2,0,0,37,38,3,4,2,0,38,39,5,
        3,0,0,39,59,1,0,0,0,40,41,5,11,0,0,41,42,5,2,0,0,42,43,3,4,2,0,43,
        44,5,3,0,0,44,59,1,0,0,0,45,56,5,13,0,0,46,47,5,2,0,0,47,48,3,4,
        2,0,48,49,5,3,0,0,49,57,1,0,0,0,50,51,5,2,0,0,51,52,3,4,2,0,52,53,
        5,4,0,0,53,54,3,4,2,0,54,55,5,3,0,0,55,57,1,0,0,0,56,46,1,0,0,0,
        56,50,1,0,0,0,57,59,1,0,0,0,58,22,1,0,0,0,58,24,1,0,0,0,58,25,1,
        0,0,0,58,26,1,0,0,0,58,30,1,0,0,0,58,35,1,0,0,0,58,40,1,0,0,0,58,
        45,1,0,0,0,59,71,1,0,0,0,60,61,10,11,0,0,61,62,7,0,0,0,62,70,3,4,
        2,12,63,64,10,10,0,0,64,65,7,1,0,0,65,70,3,4,2,11,66,67,10,2,0,0,
        67,68,5,12,0,0,68,70,3,4,2,3,69,60,1,0,0,0,69,63,1,0,0,0,69,66,1,
        0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,5,1,0,0,0,73,
        71,1,0,0,0,6,9,20,56,58,69,71
    ]

class calculadoraPrimeroMultParser ( Parser ):

    grammarFileName = "calculadoraPrimeroMult.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "','", "'*'", "'/'", 
                     "'+'", "'-'", "'sin'", "'cos'", "'tan'", "'%'", "'root'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "MUL", "DIV", "ADD", "SUB", "SIN", "COS", 
                      "TAN", "MOD", "RAIZ", "ID", "INT", "FLOAT", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stat", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    MUL=5
    DIV=6
    ADD=7
    SUB=8
    SIN=9
    COS=10
    TAN=11
    MOD=12
    RAIZ=13
    ID=14
    INT=15
    FLOAT=16
    NEWLINE=17
    WS=18

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
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stat()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 257540) != 0)):
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
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = calculadoraPrimeroMultParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.expr(0)
                self.state = 12
                self.match(calculadoraPrimeroMultParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = calculadoraPrimeroMultParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(calculadoraPrimeroMultParser.ID)
                self.state = 15
                self.match(calculadoraPrimeroMultParser.T__0)
                self.state = 16
                self.expr(0)
                self.state = 17
                self.match(calculadoraPrimeroMultParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = calculadoraPrimeroMultParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 19
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


    class ModhContext(ExprContext):

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
            if hasattr( listener, "enterModh" ):
                listener.enterModh(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModh" ):
                listener.exitModh(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModh" ):
                return visitor.visitModh(self)
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
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                localctx = calculadoraPrimeroMultParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 23
                self.match(calculadoraPrimeroMultParser.FLOAT)
                pass
            elif token in [15]:
                localctx = calculadoraPrimeroMultParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(calculadoraPrimeroMultParser.INT)
                pass
            elif token in [14]:
                localctx = calculadoraPrimeroMultParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(calculadoraPrimeroMultParser.ID)
                pass
            elif token in [2]:
                localctx = calculadoraPrimeroMultParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(calculadoraPrimeroMultParser.T__1)
                self.state = 27
                self.expr(0)
                self.state = 28
                self.match(calculadoraPrimeroMultParser.T__2)
                pass
            elif token in [9]:
                localctx = calculadoraPrimeroMultParser.SinContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.match(calculadoraPrimeroMultParser.SIN)
                self.state = 31
                self.match(calculadoraPrimeroMultParser.T__1)
                self.state = 32
                self.expr(0)
                self.state = 33
                self.match(calculadoraPrimeroMultParser.T__2)
                pass
            elif token in [10]:
                localctx = calculadoraPrimeroMultParser.CosContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 35
                self.match(calculadoraPrimeroMultParser.COS)
                self.state = 36
                self.match(calculadoraPrimeroMultParser.T__1)
                self.state = 37
                self.expr(0)
                self.state = 38
                self.match(calculadoraPrimeroMultParser.T__2)
                pass
            elif token in [11]:
                localctx = calculadoraPrimeroMultParser.TanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.match(calculadoraPrimeroMultParser.TAN)
                self.state = 41
                self.match(calculadoraPrimeroMultParser.T__1)
                self.state = 42
                self.expr(0)
                self.state = 43
                self.match(calculadoraPrimeroMultParser.T__2)
                pass
            elif token in [13]:
                localctx = calculadoraPrimeroMultParser.RaizContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.match(calculadoraPrimeroMultParser.RAIZ)
                self.state = 56
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 46
                    self.match(calculadoraPrimeroMultParser.T__1)
                    self.state = 47
                    self.expr(0)
                    self.state = 48
                    self.match(calculadoraPrimeroMultParser.T__2)
                    pass

                elif la_ == 2:
                    self.state = 50
                    self.match(calculadoraPrimeroMultParser.T__1)
                    self.state = 51
                    self.expr(0)
                    self.state = 52
                    self.match(calculadoraPrimeroMultParser.T__3)
                    self.state = 53
                    self.expr(0)
                    self.state = 54
                    self.match(calculadoraPrimeroMultParser.T__2)
                    pass


                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 69
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = calculadoraPrimeroMultParser.MulDivContext(self, calculadoraPrimeroMultParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 60
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 61
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 62
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = calculadoraPrimeroMultParser.AddSubContext(self, calculadoraPrimeroMultParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 63
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 64
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 65
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = calculadoraPrimeroMultParser.ModhContext(self, calculadoraPrimeroMultParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 66
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 67
                        self.match(calculadoraPrimeroMultParser.MOD)
                        self.state = 68
                        self.expr(3)
                        pass

             
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




