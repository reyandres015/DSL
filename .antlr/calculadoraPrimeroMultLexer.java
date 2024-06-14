// Generated from /home/reyandres015/universidad/5to Semestre/lenguajes/3erCorte/project/PrimeroMultiplicacion/calculadoraPrimeroMult.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class calculadoraPrimeroMultLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, MUL=7, DIV=8, ADD=9, SUB=10, 
		SIN=11, COS=12, TAN=13, MOD=14, RAIZ=15, ID=16, INT=17, FLOAT=18, NEWLINE=19, 
		WS=20;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "MUL", "DIV", "ADD", 
			"SUB", "SIN", "COS", "TAN", "MOD", "RAIZ", "ID", "INT", "FLOAT", "NEWLINE", 
			"WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "'('", "')'", "','", "'['", "']'", "'*'", "'/'", "'+'", 
			"'-'", "'sin'", "'cos'", "'tan'", "'%'", "'root'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, "MUL", "DIV", "ADD", "SUB", 
			"SIN", "COS", "TAN", "MOD", "RAIZ", "ID", "INT", "FLOAT", "NEWLINE", 
			"WS"
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


	public calculadoraPrimeroMultLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "calculadoraPrimeroMult.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0014q\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000f\u0004\u000fR\b\u000f\u000b\u000f"+
		"\f\u000fS\u0001\u0010\u0004\u0010W\b\u0010\u000b\u0010\f\u0010X\u0001"+
		"\u0011\u0004\u0011\\\b\u0011\u000b\u0011\f\u0011]\u0001\u0011\u0001\u0011"+
		"\u0004\u0011b\b\u0011\u000b\u0011\f\u0011c\u0001\u0012\u0003\u0012g\b"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0004\u0013l\b\u0013\u000b"+
		"\u0013\f\u0013m\u0001\u0013\u0001\u0013\u0000\u0000\u0014\u0001\u0001"+
		"\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f"+
		"\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f"+
		"\u001f\u0010!\u0011#\u0012%\u0013\'\u0014\u0001\u0000\u0003\u0002\u0000"+
		"AZaz\u0001\u000009\u0002\u0000\t\t  v\u0000\u0001\u0001\u0000\u0000\u0000"+
		"\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000"+
		"\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000"+
		"\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f"+
		"\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013"+
		"\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017"+
		"\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b"+
		"\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f"+
		"\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000"+
		"\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000"+
		"\u0000\u0001)\u0001\u0000\u0000\u0000\u0003+\u0001\u0000\u0000\u0000\u0005"+
		"-\u0001\u0000\u0000\u0000\u0007/\u0001\u0000\u0000\u0000\t1\u0001\u0000"+
		"\u0000\u0000\u000b3\u0001\u0000\u0000\u0000\r5\u0001\u0000\u0000\u0000"+
		"\u000f7\u0001\u0000\u0000\u0000\u00119\u0001\u0000\u0000\u0000\u0013;"+
		"\u0001\u0000\u0000\u0000\u0015=\u0001\u0000\u0000\u0000\u0017A\u0001\u0000"+
		"\u0000\u0000\u0019E\u0001\u0000\u0000\u0000\u001bI\u0001\u0000\u0000\u0000"+
		"\u001dK\u0001\u0000\u0000\u0000\u001fQ\u0001\u0000\u0000\u0000!V\u0001"+
		"\u0000\u0000\u0000#[\u0001\u0000\u0000\u0000%f\u0001\u0000\u0000\u0000"+
		"\'k\u0001\u0000\u0000\u0000)*\u0005=\u0000\u0000*\u0002\u0001\u0000\u0000"+
		"\u0000+,\u0005(\u0000\u0000,\u0004\u0001\u0000\u0000\u0000-.\u0005)\u0000"+
		"\u0000.\u0006\u0001\u0000\u0000\u0000/0\u0005,\u0000\u00000\b\u0001\u0000"+
		"\u0000\u000012\u0005[\u0000\u00002\n\u0001\u0000\u0000\u000034\u0005]"+
		"\u0000\u00004\f\u0001\u0000\u0000\u000056\u0005*\u0000\u00006\u000e\u0001"+
		"\u0000\u0000\u000078\u0005/\u0000\u00008\u0010\u0001\u0000\u0000\u0000"+
		"9:\u0005+\u0000\u0000:\u0012\u0001\u0000\u0000\u0000;<\u0005-\u0000\u0000"+
		"<\u0014\u0001\u0000\u0000\u0000=>\u0005s\u0000\u0000>?\u0005i\u0000\u0000"+
		"?@\u0005n\u0000\u0000@\u0016\u0001\u0000\u0000\u0000AB\u0005c\u0000\u0000"+
		"BC\u0005o\u0000\u0000CD\u0005s\u0000\u0000D\u0018\u0001\u0000\u0000\u0000"+
		"EF\u0005t\u0000\u0000FG\u0005a\u0000\u0000GH\u0005n\u0000\u0000H\u001a"+
		"\u0001\u0000\u0000\u0000IJ\u0005%\u0000\u0000J\u001c\u0001\u0000\u0000"+
		"\u0000KL\u0005r\u0000\u0000LM\u0005o\u0000\u0000MN\u0005o\u0000\u0000"+
		"NO\u0005t\u0000\u0000O\u001e\u0001\u0000\u0000\u0000PR\u0007\u0000\u0000"+
		"\u0000QP\u0001\u0000\u0000\u0000RS\u0001\u0000\u0000\u0000SQ\u0001\u0000"+
		"\u0000\u0000ST\u0001\u0000\u0000\u0000T \u0001\u0000\u0000\u0000UW\u0007"+
		"\u0001\u0000\u0000VU\u0001\u0000\u0000\u0000WX\u0001\u0000\u0000\u0000"+
		"XV\u0001\u0000\u0000\u0000XY\u0001\u0000\u0000\u0000Y\"\u0001\u0000\u0000"+
		"\u0000Z\\\u0007\u0001\u0000\u0000[Z\u0001\u0000\u0000\u0000\\]\u0001\u0000"+
		"\u0000\u0000][\u0001\u0000\u0000\u0000]^\u0001\u0000\u0000\u0000^_\u0001"+
		"\u0000\u0000\u0000_a\u0005.\u0000\u0000`b\u0007\u0001\u0000\u0000a`\u0001"+
		"\u0000\u0000\u0000bc\u0001\u0000\u0000\u0000ca\u0001\u0000\u0000\u0000"+
		"cd\u0001\u0000\u0000\u0000d$\u0001\u0000\u0000\u0000eg\u0005\r\u0000\u0000"+
		"fe\u0001\u0000\u0000\u0000fg\u0001\u0000\u0000\u0000gh\u0001\u0000\u0000"+
		"\u0000hi\u0005\n\u0000\u0000i&\u0001\u0000\u0000\u0000jl\u0007\u0002\u0000"+
		"\u0000kj\u0001\u0000\u0000\u0000lm\u0001\u0000\u0000\u0000mk\u0001\u0000"+
		"\u0000\u0000mn\u0001\u0000\u0000\u0000no\u0001\u0000\u0000\u0000op\u0006"+
		"\u0013\u0000\u0000p(\u0001\u0000\u0000\u0000\u0007\u0000SX]cfm\u0001\u0006"+
		"\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}