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


    # Visit a parse tree produced by calculadoraPrimeroMultParser#printExpr.
    def visitPrintExpr(self, ctx:calculadoraPrimeroMultParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#assign.
    def visitAssign(self, ctx:calculadoraPrimeroMultParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#blank.
    def visitBlank(self, ctx:calculadoraPrimeroMultParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#tan.
    def visitTan(self, ctx:calculadoraPrimeroMultParser.TanContext):
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


    # Visit a parse tree produced by calculadoraPrimeroMultParser#Mod.
    def visitMod(self, ctx:calculadoraPrimeroMultParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#MulDiv.
    def visitMulDiv(self, ctx:calculadoraPrimeroMultParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#AddSub.
    def visitAddSub(self, ctx:calculadoraPrimeroMultParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#cos.
    def visitCos(self, ctx:calculadoraPrimeroMultParser.CosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#MatrixSubtract.
    def visitMatrixSubtract(self, ctx:calculadoraPrimeroMultParser.MatrixSubtractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#float.
    def visitFloat(self, ctx:calculadoraPrimeroMultParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#int.
    def visitInt(self, ctx:calculadoraPrimeroMultParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#MatrixTransposed.
    def visitMatrixTransposed(self, ctx:calculadoraPrimeroMultParser.MatrixTransposedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#raiz.
    def visitRaiz(self, ctx:calculadoraPrimeroMultParser.RaizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#MatrixInverse.
    def visitMatrixInverse(self, ctx:calculadoraPrimeroMultParser.MatrixInverseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#sin.
    def visitSin(self, ctx:calculadoraPrimeroMultParser.SinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#Pow.
    def visitPow(self, ctx:calculadoraPrimeroMultParser.PowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#id.
    def visitId(self, ctx:calculadoraPrimeroMultParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#MatrixMultiply.
    def visitMatrixMultiply(self, ctx:calculadoraPrimeroMultParser.MatrixMultiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#matrix.
    def visitMatrix(self, ctx:calculadoraPrimeroMultParser.MatrixContext):
        return self.visitChildren(ctx)



del calculadoraPrimeroMultParser