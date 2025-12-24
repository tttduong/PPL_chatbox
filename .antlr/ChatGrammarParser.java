// Generated from c:/projects/PPL_chatbox/ChatGrammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ChatGrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, TITLE_STRING=28, STRING=29, INT=30, WS=31;
	public static final int
		RULE_program = 0, RULE_expression = 1, RULE_time = 2, RULE_date = 3, RULE_today = 4, 
		RULE_query = 5, RULE_status_filter = 6, RULE_start_time = 7, RULE_end_time = 8, 
		RULE_duration = 9, RULE_index_number = 10, RULE_objects = 11, RULE_verbs = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "expression", "time", "date", "today", "query", "status_filter", 
			"start_time", "end_time", "duration", "index_number", "objects", "verbs"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'/'", "'today'", "'sunny'", "'cloudy'", "'rainy'", "'windy'", 
			"'snowy'", "'clear'", "'foggy'", "'incompleted'", "'completed'", "'pending'", 
			"'done'", "':'", "'set'", "'show'", "'check'", "'tell'", "'start'", "'reset'", 
			"'complete'", "'finish'", "'undo'", "'unfinish'", "'delete'", "'remove'", 
			"'cancel'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, "TITLE_STRING", "STRING", "INT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ChatGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ChatGrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(26);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public VerbsContext verbs() {
			return getRuleContext(VerbsContext.class,0);
		}
		public Index_numberContext index_number() {
			return getRuleContext(Index_numberContext.class,0);
		}
		public ObjectsContext objects() {
			return getRuleContext(ObjectsContext.class,0);
		}
		public Status_filterContext status_filter() {
			return getRuleContext(Status_filterContext.class,0);
		}
		public TimeContext time() {
			return getRuleContext(TimeContext.class,0);
		}
		public QueryContext query() {
			return getRuleContext(QueryContext.class,0);
		}
		public TerminalNode TITLE_STRING() { return getToken(ChatGrammarParser.TITLE_STRING, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_expression);
		int _la;
		try {
			setState(43);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(28);
				verbs();
				setState(29);
				index_number();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(31);
				verbs();
				setState(33);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 15360L) != 0)) {
					{
					setState(32);
					status_filter();
					}
				}

				setState(35);
				objects();
				setState(37);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__1 || _la==INT) {
					{
					setState(36);
					time();
					}
				}

				setState(40);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1016L) != 0)) {
					{
					setState(39);
					query();
					}
				}

				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(42);
				match(TITLE_STRING);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TimeContext extends ParserRuleContext {
		public Start_timeContext start_time() {
			return getRuleContext(Start_timeContext.class,0);
		}
		public TodayContext today() {
			return getRuleContext(TodayContext.class,0);
		}
		public DateContext date() {
			return getRuleContext(DateContext.class,0);
		}
		public End_timeContext end_time() {
			return getRuleContext(End_timeContext.class,0);
		}
		public DurationContext duration() {
			return getRuleContext(DurationContext.class,0);
		}
		public TimeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_time; }
	}

	public final TimeContext time() throws RecognitionException {
		TimeContext _localctx = new TimeContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_time);
		try {
			setState(56);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(45);
				start_time();
				setState(47);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
				case 1:
					{
					setState(46);
					end_time();
					}
					break;
				}
				setState(51);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__1:
					{
					setState(49);
					today();
					}
					break;
				case INT:
					{
					setState(50);
					date();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(53);
				today();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(54);
				date();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(55);
				duration();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DateContext extends ParserRuleContext {
		public List<TerminalNode> INT() { return getTokens(ChatGrammarParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(ChatGrammarParser.INT, i);
		}
		public DateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_date; }
	}

	public final DateContext date() throws RecognitionException {
		DateContext _localctx = new DateContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_date);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			match(INT);
			setState(59);
			match(T__0);
			setState(60);
			match(INT);
			setState(61);
			match(T__0);
			setState(62);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TodayContext extends ParserRuleContext {
		public TodayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_today; }
	}

	public final TodayContext today() throws RecognitionException {
		TodayContext _localctx = new TodayContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_today);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QueryContext extends ParserRuleContext {
		public QueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_query; }
	}

	public final QueryContext query() throws RecognitionException {
		QueryContext _localctx = new QueryContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_query);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1016L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Status_filterContext extends ParserRuleContext {
		public Status_filterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_status_filter; }
	}

	public final Status_filterContext status_filter() throws RecognitionException {
		Status_filterContext _localctx = new Status_filterContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_status_filter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 15360L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Start_timeContext extends ParserRuleContext {
		public List<TerminalNode> INT() { return getTokens(ChatGrammarParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(ChatGrammarParser.INT, i);
		}
		public Start_timeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start_time; }
	}

	public final Start_timeContext start_time() throws RecognitionException {
		Start_timeContext _localctx = new Start_timeContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_start_time);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(INT);
			setState(71);
			match(T__13);
			setState(72);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class End_timeContext extends ParserRuleContext {
		public List<TerminalNode> INT() { return getTokens(ChatGrammarParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(ChatGrammarParser.INT, i);
		}
		public End_timeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_end_time; }
	}

	public final End_timeContext end_time() throws RecognitionException {
		End_timeContext _localctx = new End_timeContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_end_time);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			match(INT);
			setState(75);
			match(T__13);
			setState(76);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DurationContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(ChatGrammarParser.INT, 0); }
		public DurationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_duration; }
	}

	public final DurationContext duration() throws RecognitionException {
		DurationContext _localctx = new DurationContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_duration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Index_numberContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(ChatGrammarParser.INT, 0); }
		public Index_numberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_index_number; }
	}

	public final Index_numberContext index_number() throws RecognitionException {
		Index_numberContext _localctx = new Index_numberContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_index_number);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ObjectsContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(ChatGrammarParser.STRING, 0); }
		public ObjectsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_objects; }
	}

	public final ObjectsContext objects() throws RecognitionException {
		ObjectsContext _localctx = new ObjectsContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_objects);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			match(STRING);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VerbsContext extends ParserRuleContext {
		public VerbsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_verbs; }
	}

	public final VerbsContext verbs() throws RecognitionException {
		VerbsContext _localctx = new VerbsContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_verbs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 268402688L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001fW\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0003\u0001\"\b\u0001\u0001\u0001\u0001\u0001"+
		"\u0003\u0001&\b\u0001\u0001\u0001\u0003\u0001)\b\u0001\u0001\u0001\u0003"+
		"\u0001,\b\u0001\u0001\u0002\u0001\u0002\u0003\u00020\b\u0002\u0001\u0002"+
		"\u0001\u0002\u0003\u00024\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0003\u00029\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0000\u0000\r\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u0000\u0003\u0001\u0000"+
		"\u0003\t\u0001\u0000\n\r\u0001\u0000\u000f\u001bS\u0000\u001a\u0001\u0000"+
		"\u0000\u0000\u0002+\u0001\u0000\u0000\u0000\u00048\u0001\u0000\u0000\u0000"+
		"\u0006:\u0001\u0000\u0000\u0000\b@\u0001\u0000\u0000\u0000\nB\u0001\u0000"+
		"\u0000\u0000\fD\u0001\u0000\u0000\u0000\u000eF\u0001\u0000\u0000\u0000"+
		"\u0010J\u0001\u0000\u0000\u0000\u0012N\u0001\u0000\u0000\u0000\u0014P"+
		"\u0001\u0000\u0000\u0000\u0016R\u0001\u0000\u0000\u0000\u0018T\u0001\u0000"+
		"\u0000\u0000\u001a\u001b\u0003\u0002\u0001\u0000\u001b\u0001\u0001\u0000"+
		"\u0000\u0000\u001c\u001d\u0003\u0018\f\u0000\u001d\u001e\u0003\u0014\n"+
		"\u0000\u001e,\u0001\u0000\u0000\u0000\u001f!\u0003\u0018\f\u0000 \"\u0003"+
		"\f\u0006\u0000! \u0001\u0000\u0000\u0000!\"\u0001\u0000\u0000\u0000\""+
		"#\u0001\u0000\u0000\u0000#%\u0003\u0016\u000b\u0000$&\u0003\u0004\u0002"+
		"\u0000%$\u0001\u0000\u0000\u0000%&\u0001\u0000\u0000\u0000&(\u0001\u0000"+
		"\u0000\u0000\')\u0003\n\u0005\u0000(\'\u0001\u0000\u0000\u0000()\u0001"+
		"\u0000\u0000\u0000),\u0001\u0000\u0000\u0000*,\u0005\u001c\u0000\u0000"+
		"+\u001c\u0001\u0000\u0000\u0000+\u001f\u0001\u0000\u0000\u0000+*\u0001"+
		"\u0000\u0000\u0000,\u0003\u0001\u0000\u0000\u0000-/\u0003\u000e\u0007"+
		"\u0000.0\u0003\u0010\b\u0000/.\u0001\u0000\u0000\u0000/0\u0001\u0000\u0000"+
		"\u000003\u0001\u0000\u0000\u000014\u0003\b\u0004\u000024\u0003\u0006\u0003"+
		"\u000031\u0001\u0000\u0000\u000032\u0001\u0000\u0000\u000049\u0001\u0000"+
		"\u0000\u000059\u0003\b\u0004\u000069\u0003\u0006\u0003\u000079\u0003\u0012"+
		"\t\u00008-\u0001\u0000\u0000\u000085\u0001\u0000\u0000\u000086\u0001\u0000"+
		"\u0000\u000087\u0001\u0000\u0000\u00009\u0005\u0001\u0000\u0000\u0000"+
		":;\u0005\u001e\u0000\u0000;<\u0005\u0001\u0000\u0000<=\u0005\u001e\u0000"+
		"\u0000=>\u0005\u0001\u0000\u0000>?\u0005\u001e\u0000\u0000?\u0007\u0001"+
		"\u0000\u0000\u0000@A\u0005\u0002\u0000\u0000A\t\u0001\u0000\u0000\u0000"+
		"BC\u0007\u0000\u0000\u0000C\u000b\u0001\u0000\u0000\u0000DE\u0007\u0001"+
		"\u0000\u0000E\r\u0001\u0000\u0000\u0000FG\u0005\u001e\u0000\u0000GH\u0005"+
		"\u000e\u0000\u0000HI\u0005\u001e\u0000\u0000I\u000f\u0001\u0000\u0000"+
		"\u0000JK\u0005\u001e\u0000\u0000KL\u0005\u000e\u0000\u0000LM\u0005\u001e"+
		"\u0000\u0000M\u0011\u0001\u0000\u0000\u0000NO\u0005\u001e\u0000\u0000"+
		"O\u0013\u0001\u0000\u0000\u0000PQ\u0005\u001e\u0000\u0000Q\u0015\u0001"+
		"\u0000\u0000\u0000RS\u0005\u001d\u0000\u0000S\u0017\u0001\u0000\u0000"+
		"\u0000TU\u0007\u0002\u0000\u0000U\u0019\u0001\u0000\u0000\u0000\u0007"+
		"!%(+/38";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}