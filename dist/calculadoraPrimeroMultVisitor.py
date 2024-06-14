# Generated from calculadoraPrimeroMult.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .calculadoraPrimeroMultParser import calculadoraPrimeroMultParser
else:
    from calculadoraPrimeroMultParser import calculadoraPrimeroMultParser

# This class defines a complete generic visitor for a parse tree produced by calculadoraPrimeroMultParser.

class calculadoraPrimeroMultVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by calculadoraPrimeroMultParser#prog.
    def visitProg(self, ctx:calculadoraPrimeroMultParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#Expression.
    def visitExpression(self, ctx:calculadoraPrimeroMultParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#blank.
    def visitBlank(self, ctx:calculadoraPrimeroMultParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#MatrixAdd.
    def visitMatrixAdd(self, ctx:calculadoraPrimeroMultParser.MatrixAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#idMatrix.
    def visitIdMatrix(self, ctx:calculadoraPrimeroMultParser.IdMatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#parens.
    def visitParens(self, ctx:calculadoraPrimeroMultParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#MulDiv.
    def visitMulDiv(self, ctx:calculadoraPrimeroMultParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#cos.
    def visitCos(self, ctx:calculadoraPrimeroMultParser.CosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#for.
    def visitFor(self, ctx:calculadoraPrimeroMultParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#paint.
    def visitPaint(self, ctx:calculadoraPrimeroMultParser.PaintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#float.
    def visitFloat(self, ctx:calculadoraPrimeroMultParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#while.
    def visitWhile(self, ctx:calculadoraPrimeroMultParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#leer.
    def visitLeer(self, ctx:calculadoraPrimeroMultParser.LeerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#MatrixTransposed.
    def visitMatrixTransposed(self, ctx:calculadoraPrimeroMultParser.MatrixTransposedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#raiz.
    def visitRaiz(self, ctx:calculadoraPrimeroMultParser.RaizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#paintBall.
    def visitPaintBall(self, ctx:calculadoraPrimeroMultParser.PaintBallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#conditionalIf.
    def visitConditionalIf(self, ctx:calculadoraPrimeroMultParser.ConditionalIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#paintBars.
    def visitPaintBars(self, ctx:calculadoraPrimeroMultParser.PaintBarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#sin.
    def visitSin(self, ctx:calculadoraPrimeroMultParser.SinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#id.
    def visitId(self, ctx:calculadoraPrimeroMultParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#MatrixMultiply.
    def visitMatrixMultiply(self, ctx:calculadoraPrimeroMultParser.MatrixMultiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#printExpr.
    def visitPrintExpr(self, ctx:calculadoraPrimeroMultParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#tan.
    def visitTan(self, ctx:calculadoraPrimeroMultParser.TanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#Mod.
    def visitMod(self, ctx:calculadoraPrimeroMultParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#AddSub.
    def visitAddSub(self, ctx:calculadoraPrimeroMultParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#MatrixSubtract.
    def visitMatrixSubtract(self, ctx:calculadoraPrimeroMultParser.MatrixSubtractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#cadena.
    def visitCadena(self, ctx:calculadoraPrimeroMultParser.CadenaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#int.
    def visitInt(self, ctx:calculadoraPrimeroMultParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#paintBrownie.
    def visitPaintBrownie(self, ctx:calculadoraPrimeroMultParser.PaintBrownieContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#escribir.
    def visitEscribir(self, ctx:calculadoraPrimeroMultParser.EscribirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#MatrixInverse.
    def visitMatrixInverse(self, ctx:calculadoraPrimeroMultParser.MatrixInverseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#Pow.
    def visitPow(self, ctx:calculadoraPrimeroMultParser.PowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#assign.
    def visitAssign(self, ctx:calculadoraPrimeroMultParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#block.
    def visitBlock(self, ctx:calculadoraPrimeroMultParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#equal.
    def visitEqual(self, ctx:calculadoraPrimeroMultParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#not.
    def visitNot(self, ctx:calculadoraPrimeroMultParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#greaterEqualThan.
    def visitGreaterEqualThan(self, ctx:calculadoraPrimeroMultParser.GreaterEqualThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#or.
    def visitOr(self, ctx:calculadoraPrimeroMultParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#and.
    def visitAnd(self, ctx:calculadoraPrimeroMultParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#lessThan.
    def visitLessThan(self, ctx:calculadoraPrimeroMultParser.LessThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#notEqual.
    def visitNotEqual(self, ctx:calculadoraPrimeroMultParser.NotEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#lessEqualThan.
    def visitLessEqualThan(self, ctx:calculadoraPrimeroMultParser.LessEqualThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#greaterThan.
    def visitGreaterThan(self, ctx:calculadoraPrimeroMultParser.GreaterThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#parensCond.
    def visitParensCond(self, ctx:calculadoraPrimeroMultParser.ParensCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#matrix.
    def visitMatrix(self, ctx:calculadoraPrimeroMultParser.MatrixContext):
        return self.visitChildren(ctx)



del calculadoraPrimeroMultParser