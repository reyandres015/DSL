# Generated from lenguaje.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .lenguajeParser import lenguajeParser
else:
    from lenguajeParser import lenguajeParser

# This class defines a complete listener for a parse tree produced by lenguajeParser.
class lenguajeListener(ParseTreeListener):

    # Enter a parse tree produced by lenguajeParser#prog.
    def enterProg(self, ctx:lenguajeParser.ProgContext):
        pass

    # Exit a parse tree produced by lenguajeParser#prog.
    def exitProg(self, ctx:lenguajeParser.ProgContext):
        pass


    # Enter a parse tree produced by lenguajeParser#Expression.
    def enterExpression(self, ctx:lenguajeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by lenguajeParser#Expression.
    def exitExpression(self, ctx:lenguajeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by lenguajeParser#blank.
    def enterBlank(self, ctx:lenguajeParser.BlankContext):
        pass

    # Exit a parse tree produced by lenguajeParser#blank.
    def exitBlank(self, ctx:lenguajeParser.BlankContext):
        pass


    # Enter a parse tree produced by lenguajeParser#MatrixAdd.
    def enterMatrixAdd(self, ctx:lenguajeParser.MatrixAddContext):
        pass

    # Exit a parse tree produced by lenguajeParser#MatrixAdd.
    def exitMatrixAdd(self, ctx:lenguajeParser.MatrixAddContext):
        pass


    # Enter a parse tree produced by lenguajeParser#idMatrix.
    def enterIdMatrix(self, ctx:lenguajeParser.IdMatrixContext):
        pass

    # Exit a parse tree produced by lenguajeParser#idMatrix.
    def exitIdMatrix(self, ctx:lenguajeParser.IdMatrixContext):
        pass


    # Enter a parse tree produced by lenguajeParser#parens.
    def enterParens(self, ctx:lenguajeParser.ParensContext):
        pass

    # Exit a parse tree produced by lenguajeParser#parens.
    def exitParens(self, ctx:lenguajeParser.ParensContext):
        pass


    # Enter a parse tree produced by lenguajeParser#MulDiv.
    def enterMulDiv(self, ctx:lenguajeParser.MulDivContext):
        pass

    # Exit a parse tree produced by lenguajeParser#MulDiv.
    def exitMulDiv(self, ctx:lenguajeParser.MulDivContext):
        pass


    # Enter a parse tree produced by lenguajeParser#cos.
    def enterCos(self, ctx:lenguajeParser.CosContext):
        pass

    # Exit a parse tree produced by lenguajeParser#cos.
    def exitCos(self, ctx:lenguajeParser.CosContext):
        pass


    # Enter a parse tree produced by lenguajeParser#for.
    def enterFor(self, ctx:lenguajeParser.ForContext):
        pass

    # Exit a parse tree produced by lenguajeParser#for.
    def exitFor(self, ctx:lenguajeParser.ForContext):
        pass


    # Enter a parse tree produced by lenguajeParser#paint.
    def enterPaint(self, ctx:lenguajeParser.PaintContext):
        pass

    # Exit a parse tree produced by lenguajeParser#paint.
    def exitPaint(self, ctx:lenguajeParser.PaintContext):
        pass


    # Enter a parse tree produced by lenguajeParser#float.
    def enterFloat(self, ctx:lenguajeParser.FloatContext):
        pass

    # Exit a parse tree produced by lenguajeParser#float.
    def exitFloat(self, ctx:lenguajeParser.FloatContext):
        pass


    # Enter a parse tree produced by lenguajeParser#while.
    def enterWhile(self, ctx:lenguajeParser.WhileContext):
        pass

    # Exit a parse tree produced by lenguajeParser#while.
    def exitWhile(self, ctx:lenguajeParser.WhileContext):
        pass


    # Enter a parse tree produced by lenguajeParser#leer.
    def enterLeer(self, ctx:lenguajeParser.LeerContext):
        pass

    # Exit a parse tree produced by lenguajeParser#leer.
    def exitLeer(self, ctx:lenguajeParser.LeerContext):
        pass


    # Enter a parse tree produced by lenguajeParser#MatrixTransposed.
    def enterMatrixTransposed(self, ctx:lenguajeParser.MatrixTransposedContext):
        pass

    # Exit a parse tree produced by lenguajeParser#MatrixTransposed.
    def exitMatrixTransposed(self, ctx:lenguajeParser.MatrixTransposedContext):
        pass


    # Enter a parse tree produced by lenguajeParser#raiz.
    def enterRaiz(self, ctx:lenguajeParser.RaizContext):
        pass

    # Exit a parse tree produced by lenguajeParser#raiz.
    def exitRaiz(self, ctx:lenguajeParser.RaizContext):
        pass


    # Enter a parse tree produced by lenguajeParser#paintBall.
    def enterPaintBall(self, ctx:lenguajeParser.PaintBallContext):
        pass

    # Exit a parse tree produced by lenguajeParser#paintBall.
    def exitPaintBall(self, ctx:lenguajeParser.PaintBallContext):
        pass


    # Enter a parse tree produced by lenguajeParser#conditionalIf.
    def enterConditionalIf(self, ctx:lenguajeParser.ConditionalIfContext):
        pass

    # Exit a parse tree produced by lenguajeParser#conditionalIf.
    def exitConditionalIf(self, ctx:lenguajeParser.ConditionalIfContext):
        pass


    # Enter a parse tree produced by lenguajeParser#paintBars.
    def enterPaintBars(self, ctx:lenguajeParser.PaintBarsContext):
        pass

    # Exit a parse tree produced by lenguajeParser#paintBars.
    def exitPaintBars(self, ctx:lenguajeParser.PaintBarsContext):
        pass


    # Enter a parse tree produced by lenguajeParser#sin.
    def enterSin(self, ctx:lenguajeParser.SinContext):
        pass

    # Exit a parse tree produced by lenguajeParser#sin.
    def exitSin(self, ctx:lenguajeParser.SinContext):
        pass


    # Enter a parse tree produced by lenguajeParser#id.
    def enterId(self, ctx:lenguajeParser.IdContext):
        pass

    # Exit a parse tree produced by lenguajeParser#id.
    def exitId(self, ctx:lenguajeParser.IdContext):
        pass


    # Enter a parse tree produced by lenguajeParser#MatrixMultiply.
    def enterMatrixMultiply(self, ctx:lenguajeParser.MatrixMultiplyContext):
        pass

    # Exit a parse tree produced by lenguajeParser#MatrixMultiply.
    def exitMatrixMultiply(self, ctx:lenguajeParser.MatrixMultiplyContext):
        pass


    # Enter a parse tree produced by lenguajeParser#printExpr.
    def enterPrintExpr(self, ctx:lenguajeParser.PrintExprContext):
        pass

    # Exit a parse tree produced by lenguajeParser#printExpr.
    def exitPrintExpr(self, ctx:lenguajeParser.PrintExprContext):
        pass


    # Enter a parse tree produced by lenguajeParser#tan.
    def enterTan(self, ctx:lenguajeParser.TanContext):
        pass

    # Exit a parse tree produced by lenguajeParser#tan.
    def exitTan(self, ctx:lenguajeParser.TanContext):
        pass


    # Enter a parse tree produced by lenguajeParser#Mod.
    def enterMod(self, ctx:lenguajeParser.ModContext):
        pass

    # Exit a parse tree produced by lenguajeParser#Mod.
    def exitMod(self, ctx:lenguajeParser.ModContext):
        pass


    # Enter a parse tree produced by lenguajeParser#AddSub.
    def enterAddSub(self, ctx:lenguajeParser.AddSubContext):
        pass

    # Exit a parse tree produced by lenguajeParser#AddSub.
    def exitAddSub(self, ctx:lenguajeParser.AddSubContext):
        pass


    # Enter a parse tree produced by lenguajeParser#MatrixSubtract.
    def enterMatrixSubtract(self, ctx:lenguajeParser.MatrixSubtractContext):
        pass

    # Exit a parse tree produced by lenguajeParser#MatrixSubtract.
    def exitMatrixSubtract(self, ctx:lenguajeParser.MatrixSubtractContext):
        pass


    # Enter a parse tree produced by lenguajeParser#cadena.
    def enterCadena(self, ctx:lenguajeParser.CadenaContext):
        pass

    # Exit a parse tree produced by lenguajeParser#cadena.
    def exitCadena(self, ctx:lenguajeParser.CadenaContext):
        pass


    # Enter a parse tree produced by lenguajeParser#int.
    def enterInt(self, ctx:lenguajeParser.IntContext):
        pass

    # Exit a parse tree produced by lenguajeParser#int.
    def exitInt(self, ctx:lenguajeParser.IntContext):
        pass


    # Enter a parse tree produced by lenguajeParser#paintBrownie.
    def enterPaintBrownie(self, ctx:lenguajeParser.PaintBrownieContext):
        pass

    # Exit a parse tree produced by lenguajeParser#paintBrownie.
    def exitPaintBrownie(self, ctx:lenguajeParser.PaintBrownieContext):
        pass


    # Enter a parse tree produced by lenguajeParser#escribir.
    def enterEscribir(self, ctx:lenguajeParser.EscribirContext):
        pass

    # Exit a parse tree produced by lenguajeParser#escribir.
    def exitEscribir(self, ctx:lenguajeParser.EscribirContext):
        pass


    # Enter a parse tree produced by lenguajeParser#MatrixInverse.
    def enterMatrixInverse(self, ctx:lenguajeParser.MatrixInverseContext):
        pass

    # Exit a parse tree produced by lenguajeParser#MatrixInverse.
    def exitMatrixInverse(self, ctx:lenguajeParser.MatrixInverseContext):
        pass


    # Enter a parse tree produced by lenguajeParser#Pow.
    def enterPow(self, ctx:lenguajeParser.PowContext):
        pass

    # Exit a parse tree produced by lenguajeParser#Pow.
    def exitPow(self, ctx:lenguajeParser.PowContext):
        pass


    # Enter a parse tree produced by lenguajeParser#assign.
    def enterAssign(self, ctx:lenguajeParser.AssignContext):
        pass

    # Exit a parse tree produced by lenguajeParser#assign.
    def exitAssign(self, ctx:lenguajeParser.AssignContext):
        pass


    # Enter a parse tree produced by lenguajeParser#block.
    def enterBlock(self, ctx:lenguajeParser.BlockContext):
        pass

    # Exit a parse tree produced by lenguajeParser#block.
    def exitBlock(self, ctx:lenguajeParser.BlockContext):
        pass


    # Enter a parse tree produced by lenguajeParser#equal.
    def enterEqual(self, ctx:lenguajeParser.EqualContext):
        pass

    # Exit a parse tree produced by lenguajeParser#equal.
    def exitEqual(self, ctx:lenguajeParser.EqualContext):
        pass


    # Enter a parse tree produced by lenguajeParser#not.
    def enterNot(self, ctx:lenguajeParser.NotContext):
        pass

    # Exit a parse tree produced by lenguajeParser#not.
    def exitNot(self, ctx:lenguajeParser.NotContext):
        pass


    # Enter a parse tree produced by lenguajeParser#greaterEqualThan.
    def enterGreaterEqualThan(self, ctx:lenguajeParser.GreaterEqualThanContext):
        pass

    # Exit a parse tree produced by lenguajeParser#greaterEqualThan.
    def exitGreaterEqualThan(self, ctx:lenguajeParser.GreaterEqualThanContext):
        pass


    # Enter a parse tree produced by lenguajeParser#or.
    def enterOr(self, ctx:lenguajeParser.OrContext):
        pass

    # Exit a parse tree produced by lenguajeParser#or.
    def exitOr(self, ctx:lenguajeParser.OrContext):
        pass


    # Enter a parse tree produced by lenguajeParser#and.
    def enterAnd(self, ctx:lenguajeParser.AndContext):
        pass

    # Exit a parse tree produced by lenguajeParser#and.
    def exitAnd(self, ctx:lenguajeParser.AndContext):
        pass


    # Enter a parse tree produced by lenguajeParser#lessThan.
    def enterLessThan(self, ctx:lenguajeParser.LessThanContext):
        pass

    # Exit a parse tree produced by lenguajeParser#lessThan.
    def exitLessThan(self, ctx:lenguajeParser.LessThanContext):
        pass


    # Enter a parse tree produced by lenguajeParser#notEqual.
    def enterNotEqual(self, ctx:lenguajeParser.NotEqualContext):
        pass

    # Exit a parse tree produced by lenguajeParser#notEqual.
    def exitNotEqual(self, ctx:lenguajeParser.NotEqualContext):
        pass


    # Enter a parse tree produced by lenguajeParser#lessEqualThan.
    def enterLessEqualThan(self, ctx:lenguajeParser.LessEqualThanContext):
        pass

    # Exit a parse tree produced by lenguajeParser#lessEqualThan.
    def exitLessEqualThan(self, ctx:lenguajeParser.LessEqualThanContext):
        pass


    # Enter a parse tree produced by lenguajeParser#greaterThan.
    def enterGreaterThan(self, ctx:lenguajeParser.GreaterThanContext):
        pass

    # Exit a parse tree produced by lenguajeParser#greaterThan.
    def exitGreaterThan(self, ctx:lenguajeParser.GreaterThanContext):
        pass


    # Enter a parse tree produced by lenguajeParser#parensCond.
    def enterParensCond(self, ctx:lenguajeParser.ParensCondContext):
        pass

    # Exit a parse tree produced by lenguajeParser#parensCond.
    def exitParensCond(self, ctx:lenguajeParser.ParensCondContext):
        pass


    # Enter a parse tree produced by lenguajeParser#matrix.
    def enterMatrix(self, ctx:lenguajeParser.MatrixContext):
        pass

    # Exit a parse tree produced by lenguajeParser#matrix.
    def exitMatrix(self, ctx:lenguajeParser.MatrixContext):
        pass



del lenguajeParser