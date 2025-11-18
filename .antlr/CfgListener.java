// Generated from c:/projects/PPL_chatbox/Cfg.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CfgParser}.
 */
public interface CfgListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CfgParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(CfgParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link CfgParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(CfgParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link CfgParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(CfgParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CfgParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(CfgParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CfgParser#time}.
	 * @param ctx the parse tree
	 */
	void enterTime(CfgParser.TimeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CfgParser#time}.
	 * @param ctx the parse tree
	 */
	void exitTime(CfgParser.TimeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CfgParser#date}.
	 * @param ctx the parse tree
	 */
	void enterDate(CfgParser.DateContext ctx);
	/**
	 * Exit a parse tree produced by {@link CfgParser#date}.
	 * @param ctx the parse tree
	 */
	void exitDate(CfgParser.DateContext ctx);
	/**
	 * Enter a parse tree produced by {@link CfgParser#today}.
	 * @param ctx the parse tree
	 */
	void enterToday(CfgParser.TodayContext ctx);
	/**
	 * Exit a parse tree produced by {@link CfgParser#today}.
	 * @param ctx the parse tree
	 */
	void exitToday(CfgParser.TodayContext ctx);
	/**
	 * Enter a parse tree produced by {@link CfgParser#query}.
	 * @param ctx the parse tree
	 */
	void enterQuery(CfgParser.QueryContext ctx);
	/**
	 * Exit a parse tree produced by {@link CfgParser#query}.
	 * @param ctx the parse tree
	 */
	void exitQuery(CfgParser.QueryContext ctx);
	/**
	 * Enter a parse tree produced by {@link CfgParser#start_time}.
	 * @param ctx the parse tree
	 */
	void enterStart_time(CfgParser.Start_timeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CfgParser#start_time}.
	 * @param ctx the parse tree
	 */
	void exitStart_time(CfgParser.Start_timeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CfgParser#end_time}.
	 * @param ctx the parse tree
	 */
	void enterEnd_time(CfgParser.End_timeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CfgParser#end_time}.
	 * @param ctx the parse tree
	 */
	void exitEnd_time(CfgParser.End_timeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CfgParser#duration}.
	 * @param ctx the parse tree
	 */
	void enterDuration(CfgParser.DurationContext ctx);
	/**
	 * Exit a parse tree produced by {@link CfgParser#duration}.
	 * @param ctx the parse tree
	 */
	void exitDuration(CfgParser.DurationContext ctx);
	/**
	 * Enter a parse tree produced by {@link CfgParser#objects}.
	 * @param ctx the parse tree
	 */
	void enterObjects(CfgParser.ObjectsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CfgParser#objects}.
	 * @param ctx the parse tree
	 */
	void exitObjects(CfgParser.ObjectsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CfgParser#verbs}.
	 * @param ctx the parse tree
	 */
	void enterVerbs(CfgParser.VerbsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CfgParser#verbs}.
	 * @param ctx the parse tree
	 */
	void exitVerbs(CfgParser.VerbsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CfgParser#location}.
	 * @param ctx the parse tree
	 */
	void enterLocation(CfgParser.LocationContext ctx);
	/**
	 * Exit a parse tree produced by {@link CfgParser#location}.
	 * @param ctx the parse tree
	 */
	void exitLocation(CfgParser.LocationContext ctx);
}