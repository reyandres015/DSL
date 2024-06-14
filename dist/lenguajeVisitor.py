# Generated from lenguaje.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .lenguajeParser import lenguajeParser
else:
    from lenguajeParser import lenguajeParser

# This class defines a complete generic visitor for a parse tree produced by lenguajeParser.

class lenguajeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lenguajeParser#prog.
    def visitProg(self, ctx:lenguajeParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#Expression.
    def visitExpression(self, ctx:lenguajeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#blank.
    def visitBlank(self, ctx:lenguajeParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#MatrixAdd.
    def visitMatrixAdd(self, ctx:lenguajeParser.MatrixAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#idMatrix.
    def visitIdMatrix(self, ctx:lenguajeParser.IdMatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#parens.
    def visitParens(self, ctx:lenguajeParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#MulDiv.
    def visitMulDiv(self, ctx:lenguajeParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#cos.
    def visitCos(self, ctx:lenguajeParser.CosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#for.
    def visitFor(self, ctx:lenguajeParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#paint.
    def visitPaint(self, ctx:lenguajeParser.PaintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#float.
    def visitFloat(self, ctx:lenguajeParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#while.
    def visitWhile(self, ctx:lenguajeParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#leer.
    def visitLeer(self, ctx:lenguajeParser.LeerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#MatrixTransposed.
    def visitMatrixTransposed(self, ctx:lenguajeParser.MatrixTransposedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#raiz.
    def visitRaiz(self, ctx:lenguajeParser.RaizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#paintBall.
    def visitPaintBall(self, ctx:lenguajeParser.PaintBallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#conditionalIf.
    def visitConditionalIf(self, ctx:lenguajeParser.ConditionalIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#paintBars.
    def visitPaintBars(self, ctx:lenguajeParser.PaintBarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#sin.
    def visitSin(self, ctx:lenguajeParser.SinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#id.
    def visitId(self, ctx:lenguajeParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#MatrixMultiply.
    def visitMatrixMultiply(self, ctx:lenguajeParser.MatrixMultiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#printExpr.
    def visitPrintExpr(self, ctx:lenguajeParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#tan.
    def visitTan(self, ctx:lenguajeParser.TanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#Mod.
    def visitMod(self, ctx:lenguajeParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#AddSub.
    def visitAddSub(self, ctx:lenguajeParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#MatrixSubtract.
    def visitMatrixSubtract(self, ctx:lenguajeParser.MatrixSubtractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#cadena.
    def visitCadena(self, ctx:lenguajeParser.CadenaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#int.
    def visitInt(self, ctx:lenguajeParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#paintBrownie.
    def visitPaintBrownie(self, ctx:lenguajeParser.PaintBrownieContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#escribir.
    def visitEscribir(self, ctx:lenguajeParser.EscribirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#MatrixInverse.
    def visitMatrixInverse(self, ctx:lenguajeParser.MatrixInverseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#Pow.
    def visitPow(self, ctx:lenguajeParser.PowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#assign.
    def visitAssign(self, ctx:lenguajeParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#block.
    def visitBlock(self, ctx:lenguajeParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#equal.
    def visitEqual(self, ctx:lenguajeParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#not.
    def visitNot(self, ctx:lenguajeParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#greaterEqualThan.
    def visitGreaterEqualThan(self, ctx:lenguajeParser.GreaterEqualThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#or.
    def visitOr(self, ctx:lenguajeParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#and.
    def visitAnd(self, ctx:lenguajeParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#lessThan.
    def visitLessThan(self, ctx:lenguajeParser.LessThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#notEqual.
    def visitNotEqual(self, ctx:lenguajeParser.NotEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#lessEqualThan.
    def visitLessEqualThan(self, ctx:lenguajeParser.LessEqualThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#greaterThan.
    def visitGreaterThan(self, ctx:lenguajeParser.GreaterThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#parensCond.
    def visitParensCond(self, ctx:lenguajeParser.ParensCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeParser#matrix.
    def visitMatrix(self, ctx:lenguajeParser.MatrixContext):
        return self.visitChildren(ctx)



del lenguajeParser