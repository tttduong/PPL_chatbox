// Generated from d:/GitHub/PPL_chatbox/ChatGrammar.g4 by ANTLR 4.13.1
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
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, TITLE_STRING=16, 
		STRING=17, INT=18, WS=19;
	public static final int
		RULE_program = 0, RULE_expression = 1, RULE_time = 2, RULE_date = 3, RULE_today = 4, 
		RULE_status_filter = 5, RULE_start_time = 6, RULE_end_time = 7, RULE_duration = 8, 
		RULE_index_number = 9, RULE_objects = 10, RULE_verbs = 11;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "expression", "time", "date", "today", "status_filter", "start_time", 
			"end_time", "duration", "index_number", "objects", "verbs"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'/'", "'today'", "'done'", "'pending'", "':'", "'set'", "'show'", 
			"'check'", "'complete'", "'finish'", "'incomplete'", "'unfinish'", "'delete'", 
			"'remove'", "'cancel'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(24);
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
		public TerminalNode TITLE_STRING() { return getToken(ChatGrammarParser.TITLE_STRING, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).exitExpression(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_expression);
		int _la;
		try {
			setState(38);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(26);
				verbs();
				setState(27);
				index_number();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(29);
				verbs();
				setState(31);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__2 || _la==T__3) {
					{
					setState(30);
					status_filter();
					}
				}

				setState(33);
				objects();
				setState(35);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__1 || _la==INT) {
					{
					setState(34);
					time();
					}
				}

				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(37);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).enterTime(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).exitTime(this);
		}
	}

	public final TimeContext time() throws RecognitionException {
		TimeContext _localctx = new TimeContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_time);
		try {
			setState(51);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(40);
				start_time();
				setState(42);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
				case 1:
					{
					setState(41);
					end_time();
					}
					break;
				}
				setState(46);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__1:
					{
					setState(44);
					today();
					}
					break;
				case INT:
					{
					setState(45);
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
				setState(48);
				today();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(49);
				date();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(50);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).enterDate(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).exitDate(this);
		}
	}

	public final DateContext date() throws RecognitionException {
		DateContext _localctx = new DateContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_date);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			match(INT);
			setState(54);
			match(T__0);
			setState(55);
			match(INT);
			setState(56);
			match(T__0);
			setState(57);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).enterToday(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).exitToday(this);
		}
	}

	public final TodayContext today() throws RecognitionException {
		TodayContext _localctx = new TodayContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_today);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
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
	public static class Status_filterContext extends ParserRuleContext {
		public Status_filterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_status_filter; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).enterStatus_filter(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).exitStatus_filter(this);
		}
	}

	public final Status_filterContext status_filter() throws RecognitionException {
		Status_filterContext _localctx = new Status_filterContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_status_filter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			_la = _input.LA(1);
			if ( !(_la==T__2 || _la==T__3) ) {
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).enterStart_time(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).exitStart_time(this);
		}
	}

	public final Start_timeContext start_time() throws RecognitionException {
		Start_timeContext _localctx = new Start_timeContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_start_time);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(INT);
			setState(64);
			match(T__4);
			setState(65);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).enterEnd_time(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).exitEnd_time(this);
		}
	}

	public final End_timeContext end_time() throws RecognitionException {
		End_timeContext _localctx = new End_timeContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_end_time);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(INT);
			setState(68);
			match(T__4);
			setState(69);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).enterDuration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).exitDuration(this);
		}
	}

	public final DurationContext duration() throws RecognitionException {
		DurationContext _localctx = new DurationContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_duration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).enterIndex_number(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).exitIndex_number(this);
		}
	}

	public final Index_numberContext index_number() throws RecognitionException {
		Index_numberContext _localctx = new Index_numberContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_index_number);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(73);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).enterObjects(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).exitObjects(this);
		}
	}

	public final ObjectsContext objects() throws RecognitionException {
		ObjectsContext _localctx = new ObjectsContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_objects);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).enterVerbs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChatGrammarListener ) ((ChatGrammarListener)listener).exitVerbs(this);
		}
	}

	public final VerbsContext verbs() throws RecognitionException {
		VerbsContext _localctx = new VerbsContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_verbs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 65472L) != 0)) ) {
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
		"\u0004\u0001\u0013P\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0003\u0001 \b\u0001\u0001\u0001\u0001\u0001\u0003\u0001$\b\u0001"+
		"\u0001\u0001\u0003\u0001\'\b\u0001\u0001\u0002\u0001\u0002\u0003\u0002"+
		"+\b\u0002\u0001\u0002\u0001\u0002\u0003\u0002/\b\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0003\u00024\b\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0000\u0000\f\u0000"+
		"\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0000\u0002\u0001"+
		"\u0000\u0003\u0004\u0001\u0000\u0006\u000fL\u0000\u0018\u0001\u0000\u0000"+
		"\u0000\u0002&\u0001\u0000\u0000\u0000\u00043\u0001\u0000\u0000\u0000\u0006"+
		"5\u0001\u0000\u0000\u0000\b;\u0001\u0000\u0000\u0000\n=\u0001\u0000\u0000"+
		"\u0000\f?\u0001\u0000\u0000\u0000\u000eC\u0001\u0000\u0000\u0000\u0010"+
		"G\u0001\u0000\u0000\u0000\u0012I\u0001\u0000\u0000\u0000\u0014K\u0001"+
		"\u0000\u0000\u0000\u0016M\u0001\u0000\u0000\u0000\u0018\u0019\u0003\u0002"+
		"\u0001\u0000\u0019\u0001\u0001\u0000\u0000\u0000\u001a\u001b\u0003\u0016"+
		"\u000b\u0000\u001b\u001c\u0003\u0012\t\u0000\u001c\'\u0001\u0000\u0000"+
		"\u0000\u001d\u001f\u0003\u0016\u000b\u0000\u001e \u0003\n\u0005\u0000"+
		"\u001f\u001e\u0001\u0000\u0000\u0000\u001f \u0001\u0000\u0000\u0000 !"+
		"\u0001\u0000\u0000\u0000!#\u0003\u0014\n\u0000\"$\u0003\u0004\u0002\u0000"+
		"#\"\u0001\u0000\u0000\u0000#$\u0001\u0000\u0000\u0000$\'\u0001\u0000\u0000"+
		"\u0000%\'\u0005\u0010\u0000\u0000&\u001a\u0001\u0000\u0000\u0000&\u001d"+
		"\u0001\u0000\u0000\u0000&%\u0001\u0000\u0000\u0000\'\u0003\u0001\u0000"+
		"\u0000\u0000(*\u0003\f\u0006\u0000)+\u0003\u000e\u0007\u0000*)\u0001\u0000"+
		"\u0000\u0000*+\u0001\u0000\u0000\u0000+.\u0001\u0000\u0000\u0000,/\u0003"+
		"\b\u0004\u0000-/\u0003\u0006\u0003\u0000.,\u0001\u0000\u0000\u0000.-\u0001"+
		"\u0000\u0000\u0000/4\u0001\u0000\u0000\u000004\u0003\b\u0004\u000014\u0003"+
		"\u0006\u0003\u000024\u0003\u0010\b\u00003(\u0001\u0000\u0000\u000030\u0001"+
		"\u0000\u0000\u000031\u0001\u0000\u0000\u000032\u0001\u0000\u0000\u0000"+
		"4\u0005\u0001\u0000\u0000\u000056\u0005\u0012\u0000\u000067\u0005\u0001"+
		"\u0000\u000078\u0005\u0012\u0000\u000089\u0005\u0001\u0000\u00009:\u0005"+
		"\u0012\u0000\u0000:\u0007\u0001\u0000\u0000\u0000;<\u0005\u0002\u0000"+
		"\u0000<\t\u0001\u0000\u0000\u0000=>\u0007\u0000\u0000\u0000>\u000b\u0001"+
		"\u0000\u0000\u0000?@\u0005\u0012\u0000\u0000@A\u0005\u0005\u0000\u0000"+
		"AB\u0005\u0012\u0000\u0000B\r\u0001\u0000\u0000\u0000CD\u0005\u0012\u0000"+
		"\u0000DE\u0005\u0005\u0000\u0000EF\u0005\u0012\u0000\u0000F\u000f\u0001"+
		"\u0000\u0000\u0000GH\u0005\u0012\u0000\u0000H\u0011\u0001\u0000\u0000"+
		"\u0000IJ\u0005\u0012\u0000\u0000J\u0013\u0001\u0000\u0000\u0000KL\u0005"+
		"\u0011\u0000\u0000L\u0015\u0001\u0000\u0000\u0000MN\u0007\u0001\u0000"+
		"\u0000N\u0017\u0001\u0000\u0000\u0000\u0006\u001f#&*.3";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}