// Generated from d:/GitHub/PPL_chatbox/ChatGrammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ChatGrammarParser}.
 */
public interface ChatGrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ChatGrammarParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(ChatGrammarParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatGrammarParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(ChatGrammarParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChatGrammarParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(ChatGrammarParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatGrammarParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(ChatGrammarParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChatGrammarParser#time}.
	 * @param ctx the parse tree
	 */
	void enterTime(ChatGrammarParser.TimeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatGrammarParser#time}.
	 * @param ctx the parse tree
	 */
	void exitTime(ChatGrammarParser.TimeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChatGrammarParser#date}.
	 * @param ctx the parse tree
	 */
	void enterDate(ChatGrammarParser.DateContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatGrammarParser#date}.
	 * @param ctx the parse tree
	 */
	void exitDate(ChatGrammarParser.DateContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChatGrammarParser#today}.
	 * @param ctx the parse tree
	 */
	void enterToday(ChatGrammarParser.TodayContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatGrammarParser#today}.
	 * @param ctx the parse tree
	 */
	void exitToday(ChatGrammarParser.TodayContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChatGrammarParser#status_filter}.
	 * @param ctx the parse tree
	 */
	void enterStatus_filter(ChatGrammarParser.Status_filterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatGrammarParser#status_filter}.
	 * @param ctx the parse tree
	 */
	void exitStatus_filter(ChatGrammarParser.Status_filterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChatGrammarParser#start_time}.
	 * @param ctx the parse tree
	 */
	void enterStart_time(ChatGrammarParser.Start_timeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatGrammarParser#start_time}.
	 * @param ctx the parse tree
	 */
	void exitStart_time(ChatGrammarParser.Start_timeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChatGrammarParser#end_time}.
	 * @param ctx the parse tree
	 */
	void enterEnd_time(ChatGrammarParser.End_timeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatGrammarParser#end_time}.
	 * @param ctx the parse tree
	 */
	void exitEnd_time(ChatGrammarParser.End_timeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChatGrammarParser#duration}.
	 * @param ctx the parse tree
	 */
	void enterDuration(ChatGrammarParser.DurationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatGrammarParser#duration}.
	 * @param ctx the parse tree
	 */
	void exitDuration(ChatGrammarParser.DurationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChatGrammarParser#index_number}.
	 * @param ctx the parse tree
	 */
	void enterIndex_number(ChatGrammarParser.Index_numberContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatGrammarParser#index_number}.
	 * @param ctx the parse tree
	 */
	void exitIndex_number(ChatGrammarParser.Index_numberContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChatGrammarParser#objects}.
	 * @param ctx the parse tree
	 */
	void enterObjects(ChatGrammarParser.ObjectsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatGrammarParser#objects}.
	 * @param ctx the parse tree
	 */
	void exitObjects(ChatGrammarParser.ObjectsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChatGrammarParser#verbs}.
	 * @param ctx the parse tree
	 */
	void enterVerbs(ChatGrammarParser.VerbsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatGrammarParser#verbs}.
	 * @param ctx the parse tree
	 */
	void exitVerbs(ChatGrammarParser.VerbsContext ctx);
}