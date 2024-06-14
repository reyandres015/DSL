from antlr4 import *
from dist.lenguajeLexer import lenguajeLexer
from dist.lenguajeParser import lenguajeParser
from dist.lenguajeVisitor import lenguajeVisitor

import math
import numpy as np
from ast import literal_eval
import matplotlib.pyplot as plt


class EvalVisitor(lenguajeVisitor):
    def __init__(self):
        self.memory = {}

    # Métodos visit
    def visitExpression(self, ctx):
        value = self.visit(ctx.expr())
        return value

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return value

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitAssign(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        return value

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == lenguajeParser.MUL:
            return left * right
        else:
            return left / right

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == lenguajeParser.ADD:
            return left + right
        else:
            return left - right

    def visitPow(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left ** right

    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitCadena(self, ctx):
        return str(ctx.CADENA().getText())

    def visitFloat(self, ctx):
        return float(ctx.FLOAT().getText())

    def visitId(self, ctx):
        var_name = ctx.ID().getText()
        if var_name in self.memory:
            return self.memory[var_name]
        return 0

    def visitBool(self, ctx):
        if ctx.getText() == 'true':
            return True
        else:
            return False

    def visitSin(self, ctx):
        return math.sin(math.radians(self.visit(ctx.expr())))

    def visitCos(self, ctx):
        return math.cos(math.radians(self.visit(ctx.expr())))

    def visitTan(self, ctx):
        return math.tan(math.radians(self.visit(ctx.expr())))

    def visitMod(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left % right

    def visitRaiz(self, ctx):
        left = self.visit(ctx.expr(0))
        if ctx.expr(1) is None:
            right = 2
        else:
            right = self.visit(ctx.expr(1))
        return left ** (1/right)

    def visitMatrix(self, ctx):
        text = ctx.getText()
        matrix = literal_eval(text)
        return matrix

    def visitMatrixAdd(self, ctx):
        num_matrices = ctx.getChildCount() // 2 + 1

        result_matrix = self.visit(ctx.matrix(0))
        for i in range(1, num_matrices):
            result_matrix = self.sumar_matrices(
                result_matrix, self.visit(ctx.matrix(i)))
        return result_matrix

    def sumar_matrices(self, matrix1, matrix2):
        return [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]

    def visitMatrixSubtract(self, ctx):
        num_matrices = ctx.getChildCount() // 2 + 1

        result_matrix = self.visit(ctx.matrix(0))
        for i in range(1, num_matrices):
            result_matrix = self.restar_matrices(
                result_matrix, self.visit(ctx.matrix(i)))

        return result_matrix

    def restar_matrices(self, matrix1, matrix2):
        # Sumar las matrices
        return [[a - b for a, b in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]

    def visitMatrixMultiply(self, ctx):
        matrix1 = self.visit(ctx.matrix(0))
        matrix2 = self.visit(ctx.matrix(1))
        return np.array(matrix1) @ np.array(matrix2)

    def visitMatrixInverse(self, ctx):
        matrix1 = self.visit(ctx.matrix())
        return np.linalg.inv(np.array(matrix1))

    def visitMatrixTransposed(self, ctx):
        matrix1 = self.visit(ctx.matrix())
        return np.transpose(np.array(matrix1))

    def visitLessThan(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left < right

    def visitGreaterThan(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left > right

    def visitLessEqualThan(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left <= right

    def visitEqual(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left == right

    def visitNotEqual(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left != right

    def visitAnd(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left and right

    def visitOr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left or right

    def visitNot(self, ctx):
        return not self.visit(ctx.expr())

    def visitConditionalIf(self, ctx):
        if self.visit(ctx.cond()):
            return self.visit(ctx.block(0))
        else:
            return self.visit(ctx.block(1))

    def visitFor(self, ctx):
        print(ctx.expr(0).getText(), ctx.expr(1).getText())
        for _ in range(int(ctx.expr(0).getText()), int(ctx.expr(1).getText())):
            self.visit(ctx.block())

    def visitWhile(self, ctx):
        while self.visit(ctx.cond()):
            self.visit(ctx.block())

    def visitPaint(self, ctx):
        x = self.visit(ctx.expr(0))
        y = self.visit(ctx.expr(1))
        plt.plot(x, y)
        plt.show()

    def visitPaintBall(self, ctx):
        x = self.visit(ctx.expr(0))
        y = self.visit(ctx.expr(1))
        plt.scatter(x, y)
        plt.show()

    def visitPaintBars(self, ctx):
        x = self.visit(ctx.expr(0))
        y = self.visit(ctx.expr(1))
        plt.bar(x, y)
        plt.show()

    def visitPaintBrownie(self, ctx):
        x = self.visit(ctx.expr())
        plt.pie(x)
        plt.show()

    def visitLeer(self, ctx):
        archiveName = self.visit(ctx.expr())
        archiveName = archiveName.replace('"', '')
        try:
            with open(archiveName, 'r') as archivo:
                contenido = archivo.read()
                print(f"Contenido del archivo {archiveName}:\n{contenido}")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def visitEscribir(self, ctx):
        archiveName = self.visit(ctx.expr(0))
        archiveName = archiveName.replace('"', '')
        archiveContent = str(self.visit(ctx.expr(1)))
        archiveContent = archiveContent.replace('"', '')
        archiveContent += '\n'
        try:
            with open(archiveName, 'a', encoding='utf-8') as archivo:
                archivo.write(archiveContent)
                print(
                    f"Se ha escrito el contenido en el archivo {archiveName}")
        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")


def main():
    option = input("Enter '1' to read from file or '2' to read from console: ")
    if option == '1':
        file_name = input("Enter the file name: ")
        try:
            with open(file_name, 'r') as file:
                input_stream = InputStream(file.read())
                lexer = lenguajeLexer(input_stream)
                token_stream = CommonTokenStream(lexer)
                parser = lenguajeParser(token_stream)
                tree = parser.prog()

                eval_visitor = EvalVisitor()
                eval_visitor.visit(tree)
        except Exception as e:
            print(f"Error reading file: {e}")
    elif option == '2':
        input_text = ""
        print('Ingrese su codigo:')
        while True:
            line = input("Enter a line of input (or press Enter to finish): ")
            if line == "":
                break
            input_text += line + "\n"
        input_stream = InputStream(input_text)
        lexer = lenguajeLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = lenguajeParser(token_stream)
        tree = parser.prog()

        eval_visitor = EvalVisitor()
        eval_visitor.visit(tree)
    else:
        print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
