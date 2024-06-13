// Generated from /home/reyandres015/universidad/5to Semestre/lenguajes/3erCorte/project/PrimeroMultiplicacion/calculadoraPrimeroMult.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link calculadoraPrimeroMultParser}.
 */
public interface calculadoraPrimeroMultListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link calculadoraPrimeroMultParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(calculadoraPrimeroMultParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link calculadoraPrimeroMultParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(calculadoraPrimeroMultParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by the {@code printExpr}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterPrintExpr(calculadoraPrimeroMultParser.PrintExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code printExpr}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitPrintExpr(calculadoraPrimeroMultParser.PrintExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code assign}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterAssign(calculadoraPrimeroMultParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assign}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitAssign(calculadoraPrimeroMultParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by the {@code blank}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterBlank(calculadoraPrimeroMultParser.BlankContext ctx);
	/**
	 * Exit a parse tree produced by the {@code blank}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitBlank(calculadoraPrimeroMultParser.BlankContext ctx);
	/**
	 * Enter a parse tree produced by the {@code parens}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterParens(calculadoraPrimeroMultParser.ParensContext ctx);
	/**
	 * Exit a parse tree produced by the {@code parens}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitParens(calculadoraPrimeroMultParser.ParensContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMulDiv(calculadoraPrimeroMultParser.MulDivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMulDiv(calculadoraPrimeroMultParser.MulDivContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAddSub(calculadoraPrimeroMultParser.AddSubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAddSub(calculadoraPrimeroMultParser.AddSubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code decrement}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterDecrement(calculadoraPrimeroMultParser.DecrementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code decrement}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitDecrement(calculadoraPrimeroMultParser.DecrementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code increment}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIncrement(calculadoraPrimeroMultParser.IncrementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code increment}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIncrement(calculadoraPrimeroMultParser.IncrementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code unary}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterUnary(calculadoraPrimeroMultParser.UnaryContext ctx);
	/**
	 * Exit a parse tree produced by the {@code unary}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitUnary(calculadoraPrimeroMultParser.UnaryContext ctx);
	/**
	 * Enter a parse tree produced by the {@code id}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterId(calculadoraPrimeroMultParser.IdContext ctx);
	/**
	 * Exit a parse tree produced by the {@code id}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitId(calculadoraPrimeroMultParser.IdContext ctx);
	/**
	 * Enter a parse tree produced by the {@code float}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterFloat(calculadoraPrimeroMultParser.FloatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code float}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitFloat(calculadoraPrimeroMultParser.FloatContext ctx);
	/**
	 * Enter a parse tree produced by the {@code int}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterInt(calculadoraPrimeroMultParser.IntContext ctx);
	/**
	 * Exit a parse tree produced by the {@code int}
	 * labeled alternative in {@link calculadoraPrimeroMultParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitInt(calculadoraPrimeroMultParser.IntContext ctx);
}