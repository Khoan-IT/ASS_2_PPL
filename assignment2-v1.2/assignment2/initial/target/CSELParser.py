# Generated from main/csel/parser/CSEL.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\66")
        buf.write("\u01ec\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\7\2r\n\2\f\2")
        buf.write("\16\2u\13\2\3\2\3\2\3\3\3\3\5\3{\n\3\3\4\3\4\5\4\177\n")
        buf.write("\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\7\6\u0088\n\6\f\6\16\6")
        buf.write("\u008b\13\6\3\7\3\7\3\7\5\7\u0090\n\7\3\7\3\7\5\7\u0094")
        buf.write("\n\7\3\b\3\b\3\b\3\b\3\b\7\b\u009b\n\b\f\b\16\b\u009e")
        buf.write("\13\b\5\b\u00a0\n\b\3\b\5\b\u00a3\n\b\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\7\n\u00ac\n\n\f\n\16\n\u00af\13\n\3\13\3")
        buf.write("\13\3\13\5\13\u00b4\n\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\7\f\u00be\n\f\f\f\16\f\u00c1\13\f\5\f\u00c3\n\f")
        buf.write("\3\f\5\f\u00c6\n\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\5\17\u00d2\n\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\5\20\u00db\n\20\3\21\3\21\3\21\3\21\3\22\3")
        buf.write("\22\7\22\u00e3\n\22\f\22\16\22\u00e6\13\22\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\5\23\u00f0\n\23\3\24\3\24")
        buf.write("\3\24\5\24\u00f5\n\24\3\24\3\24\3\24\3\24\3\25\3\25\3")
        buf.write("\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\5\27")
        buf.write("\u0107\n\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\5\31\u0114\n\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\7\32\u011c\n\32\f\32\16\32\u011f\13\32\3\32\3\32")
        buf.write("\5\32\u0123\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3")
        buf.write("\34\5\34\u012d\n\34\3\35\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u0135\n\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\5")
        buf.write("\36\u013f\n\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("$\3$\3$\5$\u015c\n$\3$\3$\3%\3%\3%\3%\3%\5%\u0165\n%\3")
        buf.write("&\3&\3\'\3\'\5\'\u016b\n\'\3\'\3\'\3(\3(\3(\3(\3(\5(\u0174")
        buf.write("\n(\3)\3)\3)\3)\3)\5)\u017b\n)\3*\3*\3*\3*\3*\3*\7*\u0183")
        buf.write("\n*\f*\16*\u0186\13*\3+\3+\3+\3+\3+\3+\7+\u018e\n+\f+")
        buf.write("\16+\u0191\13+\3,\3,\3,\3,\3,\3,\7,\u0199\n,\f,\16,\u019c")
        buf.write("\13,\3-\3-\3-\5-\u01a1\n-\3.\3.\3.\5.\u01a6\n.\3/\3/\3")
        buf.write("/\3/\3/\3/\5/\u01ae\n/\7/\u01b0\n/\f/\16/\u01b3\13/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\5\63\u01c3\n\63\3\64\3\64\3\64\3\64\3")
        buf.write("\64\5\64\u01ca\n\64\3\65\3\65\3\65\3\65\7\65\u01d0\n\65")
        buf.write("\f\65\16\65\u01d3\13\65\5\65\u01d5\n\65\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\3\67\7\67\u01e1\n\67\f")
        buf.write("\67\16\67\u01e4\13\67\5\67\u01e6\n\67\3\67\3\67\38\38")
        buf.write("\38\2\6RTV\\9\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 ")
        buf.write("\"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln\2\4")
        buf.write("\3\2\31\32\3\2\25\26\2\u01f0\2s\3\2\2\2\4z\3\2\2\2\6~")
        buf.write("\3\2\2\2\b\u0080\3\2\2\2\n\u0084\3\2\2\2\f\u008c\3\2\2")
        buf.write("\2\16\u0095\3\2\2\2\20\u00a4\3\2\2\2\22\u00a8\3\2\2\2")
        buf.write("\24\u00b0\3\2\2\2\26\u00b8\3\2\2\2\30\u00c7\3\2\2\2\32")
        buf.write("\u00c9\3\2\2\2\34\u00ce\3\2\2\2\36\u00da\3\2\2\2 \u00dc")
        buf.write("\3\2\2\2\"\u00e4\3\2\2\2$\u00ef\3\2\2\2&\u00f4\3\2\2\2")
        buf.write("(\u00fa\3\2\2\2*\u00fd\3\2\2\2,\u0106\3\2\2\2.\u0108\3")
        buf.write("\2\2\2\60\u0113\3\2\2\2\62\u0115\3\2\2\2\64\u0124\3\2")
        buf.write("\2\2\66\u012c\3\2\2\28\u012e\3\2\2\2:\u0138\3\2\2\2<\u0142")
        buf.write("\3\2\2\2>\u0148\3\2\2\2@\u014b\3\2\2\2B\u014e\3\2\2\2")
        buf.write("D\u0151\3\2\2\2F\u0158\3\2\2\2H\u0164\3\2\2\2J\u0166\3")
        buf.write("\2\2\2L\u0168\3\2\2\2N\u0173\3\2\2\2P\u017a\3\2\2\2R\u017c")
        buf.write("\3\2\2\2T\u0187\3\2\2\2V\u0192\3\2\2\2X\u01a0\3\2\2\2")
        buf.write("Z\u01a5\3\2\2\2\\\u01a7\3\2\2\2^\u01b4\3\2\2\2`\u01b6")
        buf.write("\3\2\2\2b\u01b8\3\2\2\2d\u01c2\3\2\2\2f\u01c9\3\2\2\2")
        buf.write("h\u01cb\3\2\2\2j\u01d8\3\2\2\2l\u01dc\3\2\2\2n\u01e9\3")
        buf.write("\2\2\2pr\5\4\3\2qp\3\2\2\2ru\3\2\2\2sq\3\2\2\2st\3\2\2")
        buf.write("\2tv\3\2\2\2us\3\2\2\2vw\7\2\2\3w\3\3\2\2\2x{\5\6\4\2")
        buf.write("y{\5\32\16\2zx\3\2\2\2zy\3\2\2\2{\5\3\2\2\2|\177\5\b\5")
        buf.write("\2}\177\5\20\t\2~|\3\2\2\2~}\3\2\2\2\177\7\3\2\2\2\u0080")
        buf.write("\u0081\7\'\2\2\u0081\u0082\5\n\6\2\u0082\u0083\7\3\2\2")
        buf.write("\u0083\t\3\2\2\2\u0084\u0089\5\f\7\2\u0085\u0086\7\4\2")
        buf.write("\2\u0086\u0088\5\f\7\2\u0087\u0085\3\2\2\2\u0088\u008b")
        buf.write("\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a")
        buf.write("\13\3\2\2\2\u008b\u0089\3\2\2\2\u008c\u008f\5\16\b\2\u008d")
        buf.write("\u008e\7\5\2\2\u008e\u0090\7\16\2\2\u008f\u008d\3\2\2")
        buf.write("\2\u008f\u0090\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u0092")
        buf.write("\7\6\2\2\u0092\u0094\5N(\2\u0093\u0091\3\2\2\2\u0093\u0094")
        buf.write("\3\2\2\2\u0094\r\3\2\2\2\u0095\u00a2\7\22\2\2\u0096\u009f")
        buf.write("\7\7\2\2\u0097\u009c\7\17\2\2\u0098\u0099\7\4\2\2\u0099")
        buf.write("\u009b\7\17\2\2\u009a\u0098\3\2\2\2\u009b\u009e\3\2\2")
        buf.write("\2\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u00a0")
        buf.write("\3\2\2\2\u009e\u009c\3\2\2\2\u009f\u0097\3\2\2\2\u009f")
        buf.write("\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a3\7\b\2\2")
        buf.write("\u00a2\u0096\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\17\3\2")
        buf.write("\2\2\u00a4\u00a5\7(\2\2\u00a5\u00a6\5\22\n\2\u00a6\u00a7")
        buf.write("\7\3\2\2\u00a7\21\3\2\2\2\u00a8\u00ad\5\24\13\2\u00a9")
        buf.write("\u00aa\7\4\2\2\u00aa\u00ac\5\24\13\2\u00ab\u00a9\3\2\2")
        buf.write("\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae")
        buf.write("\3\2\2\2\u00ae\23\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b3")
        buf.write("\5\26\f\2\u00b1\u00b2\7\5\2\2\u00b2\u00b4\7\16\2\2\u00b3")
        buf.write("\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2")
        buf.write("\u00b5\u00b6\7\6\2\2\u00b6\u00b7\5N(\2\u00b7\25\3\2\2")
        buf.write("\2\u00b8\u00c5\7\21\2\2\u00b9\u00c2\7\7\2\2\u00ba\u00bf")
        buf.write("\7\17\2\2\u00bb\u00bc\7\4\2\2\u00bc\u00be\7\17\2\2\u00bd")
        buf.write("\u00bb\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf\u00bd\3\2\2\2")
        buf.write("\u00bf\u00c0\3\2\2\2\u00c0\u00c3\3\2\2\2\u00c1\u00bf\3")
        buf.write("\2\2\2\u00c2\u00ba\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4")
        buf.write("\3\2\2\2\u00c4\u00c6\7\b\2\2\u00c5\u00b9\3\2\2\2\u00c5")
        buf.write("\u00c6\3\2\2\2\u00c6\27\3\2\2\2\u00c7\u00c8\5\16\b\2\u00c8")
        buf.write("\31\3\2\2\2\u00c9\u00ca\7&\2\2\u00ca\u00cb\7\22\2\2\u00cb")
        buf.write("\u00cc\5\34\17\2\u00cc\u00cd\5 \21\2\u00cd\33\3\2\2\2")
        buf.write("\u00ce\u00d1\7\t\2\2\u00cf\u00d2\5\36\20\2\u00d0\u00d2")
        buf.write("\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2")
        buf.write("\u00d3\3\2\2\2\u00d3\u00d4\7\n\2\2\u00d4\35\3\2\2\2\u00d5")
        buf.write("\u00d6\5\30\r\2\u00d6\u00d7\7\4\2\2\u00d7\u00d8\5\36\20")
        buf.write("\2\u00d8\u00db\3\2\2\2\u00d9\u00db\5\30\r\2\u00da\u00d5")
        buf.write("\3\2\2\2\u00da\u00d9\3\2\2\2\u00db\37\3\2\2\2\u00dc\u00dd")
        buf.write("\7\13\2\2\u00dd\u00de\5\"\22\2\u00de\u00df\7\f\2\2\u00df")
        buf.write("!\3\2\2\2\u00e0\u00e3\5\6\4\2\u00e1\u00e3\5$\23\2\u00e2")
        buf.write("\u00e0\3\2\2\2\u00e2\u00e1\3\2\2\2\u00e3\u00e6\3\2\2\2")
        buf.write("\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5#\3\2\2")
        buf.write("\2\u00e6\u00e4\3\2\2\2\u00e7\u00f0\5&\24\2\u00e8\u00f0")
        buf.write("\5\62\32\2\u00e9\u00f0\5\66\34\2\u00ea\u00f0\5<\37\2\u00eb")
        buf.write("\u00f0\5> \2\u00ec\u00f0\5@!\2\u00ed\u00f0\5B\"\2\u00ee")
        buf.write("\u00f0\5L\'\2\u00ef\u00e7\3\2\2\2\u00ef\u00e8\3\2\2\2")
        buf.write("\u00ef\u00e9\3\2\2\2\u00ef\u00ea\3\2\2\2\u00ef\u00eb\3")
        buf.write("\2\2\2\u00ef\u00ec\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00ee")
        buf.write("\3\2\2\2\u00f0%\3\2\2\2\u00f1\u00f5\7\22\2\2\u00f2\u00f5")
        buf.write("\5(\25\2\u00f3\u00f5\5.\30\2\u00f4\u00f1\3\2\2\2\u00f4")
        buf.write("\u00f2\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2")
        buf.write("\u00f6\u00f7\7\6\2\2\u00f7\u00f8\5N(\2\u00f8\u00f9\7\3")
        buf.write("\2\2\u00f9\'\3\2\2\2\u00fa\u00fb\7\22\2\2\u00fb\u00fc")
        buf.write("\5*\26\2\u00fc)\3\2\2\2\u00fd\u00fe\7\7\2\2\u00fe\u00ff")
        buf.write("\5,\27\2\u00ff\u0100\7\b\2\2\u0100+\3\2\2\2\u0101\u0102")
        buf.write("\5N(\2\u0102\u0103\7\4\2\2\u0103\u0104\5,\27\2\u0104\u0107")
        buf.write("\3\2\2\2\u0105\u0107\5N(\2\u0106\u0101\3\2\2\2\u0106\u0105")
        buf.write("\3\2\2\2\u0107-\3\2\2\2\u0108\u0109\7\22\2\2\u0109\u010a")
        buf.write("\5\60\31\2\u010a/\3\2\2\2\u010b\u010c\7\7\2\2\u010c\u010d")
        buf.write("\7\60\2\2\u010d\u0114\7\b\2\2\u010e\u010f\7\7\2\2\u010f")
        buf.write("\u0110\7\60\2\2\u0110\u0111\7\b\2\2\u0111\u0112\3\2\2")
        buf.write("\2\u0112\u0114\5\60\31\2\u0113\u010b\3\2\2\2\u0113\u010e")
        buf.write("\3\2\2\2\u0114\61\3\2\2\2\u0115\u0116\7\35\2\2\u0116\u0117")
        buf.write("\7\t\2\2\u0117\u0118\5N(\2\u0118\u0119\7\n\2\2\u0119\u011d")
        buf.write("\5 \21\2\u011a\u011c\5\64\33\2\u011b\u011a\3\2\2\2\u011c")
        buf.write("\u011f\3\2\2\2\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2\2")
        buf.write("\u011e\u0122\3\2\2\2\u011f\u011d\3\2\2\2\u0120\u0121\7")
        buf.write("\37\2\2\u0121\u0123\5 \21\2\u0122\u0120\3\2\2\2\u0122")
        buf.write("\u0123\3\2\2\2\u0123\63\3\2\2\2\u0124\u0125\7\36\2\2\u0125")
        buf.write("\u0126\7\t\2\2\u0126\u0127\5N(\2\u0127\u0128\7\n\2\2\u0128")
        buf.write("\u0129\5 \21\2\u0129\65\3\2\2\2\u012a\u012d\58\35\2\u012b")
        buf.write("\u012d\5:\36\2\u012c\u012a\3\2\2\2\u012c\u012b\3\2\2\2")
        buf.write("\u012d\67\3\2\2\2\u012e\u012f\7!\2\2\u012f\u0130\7\22")
        buf.write("\2\2\u0130\u0134\7#\2\2\u0131\u0135\5l\67\2\u0132\u0135")
        buf.write("\7\22\2\2\u0133\u0135\7\21\2\2\u0134\u0131\3\2\2\2\u0134")
        buf.write("\u0132\3\2\2\2\u0134\u0133\3\2\2\2\u0135\u0136\3\2\2\2")
        buf.write("\u0136\u0137\5 \21\2\u01379\3\2\2\2\u0138\u0139\7!\2\2")
        buf.write("\u0139\u013a\7\22\2\2\u013a\u013e\7\"\2\2\u013b\u013f")
        buf.write("\5h\65\2\u013c\u013f\7\22\2\2\u013d\u013f\7\21\2\2\u013e")
        buf.write("\u013b\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013d\3\2\2\2")
        buf.write("\u013f\u0140\3\2\2\2\u0140\u0141\5 \21\2\u0141;\3\2\2")
        buf.write("\2\u0142\u0143\7 \2\2\u0143\u0144\7\t\2\2\u0144\u0145")
        buf.write("\5N(\2\u0145\u0146\7\n\2\2\u0146\u0147\5 \21\2\u0147=")
        buf.write("\3\2\2\2\u0148\u0149\7\33\2\2\u0149\u014a\7\3\2\2\u014a")
        buf.write("?\3\2\2\2\u014b\u014c\7\34\2\2\u014c\u014d\7\3\2\2\u014d")
        buf.write("A\3\2\2\2\u014e\u014f\5D#\2\u014f\u0150\7\3\2\2\u0150")
        buf.write("C\3\2\2\2\u0151\u0152\7$\2\2\u0152\u0153\7\t\2\2\u0153")
        buf.write("\u0154\7\22\2\2\u0154\u0155\7\4\2\2\u0155\u0156\5F$\2")
        buf.write("\u0156\u0157\7\n\2\2\u0157E\3\2\2\2\u0158\u015b\7\7\2")
        buf.write("\2\u0159\u015c\5H%\2\u015a\u015c\3\2\2\2\u015b\u0159\3")
        buf.write("\2\2\2\u015b\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e")
        buf.write("\7\b\2\2\u015eG\3\2\2\2\u015f\u0160\5J&\2\u0160\u0161")
        buf.write("\7\4\2\2\u0161\u0162\5H%\2\u0162\u0165\3\2\2\2\u0163\u0165")
        buf.write("\5J&\2\u0164\u015f\3\2\2\2\u0164\u0163\3\2\2\2\u0165I")
        buf.write("\3\2\2\2\u0166\u0167\5N(\2\u0167K\3\2\2\2\u0168\u016a")
        buf.write("\7%\2\2\u0169\u016b\5N(\2\u016a\u0169\3\2\2\2\u016a\u016b")
        buf.write("\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016d\7\3\2\2\u016d")
        buf.write("M\3\2\2\2\u016e\u016f\5P)\2\u016f\u0170\t\2\2\2\u0170")
        buf.write("\u0171\5P)\2\u0171\u0174\3\2\2\2\u0172\u0174\5P)\2\u0173")
        buf.write("\u016e\3\2\2\2\u0173\u0172\3\2\2\2\u0174O\3\2\2\2\u0175")
        buf.write("\u0176\5R*\2\u0176\u0177\7\23\2\2\u0177\u0178\5R*\2\u0178")
        buf.write("\u017b\3\2\2\2\u0179\u017b\5R*\2\u017a\u0175\3\2\2\2\u017a")
        buf.write("\u0179\3\2\2\2\u017bQ\3\2\2\2\u017c\u017d\b*\1\2\u017d")
        buf.write("\u017e\5T+\2\u017e\u0184\3\2\2\2\u017f\u0180\f\4\2\2\u0180")
        buf.write("\u0181\7\24\2\2\u0181\u0183\5T+\2\u0182\u017f\3\2\2\2")
        buf.write("\u0183\u0186\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3")
        buf.write("\2\2\2\u0185S\3\2\2\2\u0186\u0184\3\2\2\2\u0187\u0188")
        buf.write("\b+\1\2\u0188\u0189\5V,\2\u0189\u018f\3\2\2\2\u018a\u018b")
        buf.write("\f\4\2\2\u018b\u018c\t\3\2\2\u018c\u018e\5V,\2\u018d\u018a")
        buf.write("\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f")
        buf.write("\u0190\3\2\2\2\u0190U\3\2\2\2\u0191\u018f\3\2\2\2\u0192")
        buf.write("\u0193\b,\1\2\u0193\u0194\5X-\2\u0194\u019a\3\2\2\2\u0195")
        buf.write("\u0196\f\4\2\2\u0196\u0197\7\27\2\2\u0197\u0199\5X-\2")
        buf.write("\u0198\u0195\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198\3")
        buf.write("\2\2\2\u019a\u019b\3\2\2\2\u019bW\3\2\2\2\u019c\u019a")
        buf.write("\3\2\2\2\u019d\u019e\7\30\2\2\u019e\u01a1\5X-\2\u019f")
        buf.write("\u01a1\5Z.\2\u01a0\u019d\3\2\2\2\u01a0\u019f\3\2\2\2\u01a1")
        buf.write("Y\3\2\2\2\u01a2\u01a3\7\26\2\2\u01a3\u01a6\5Z.\2\u01a4")
        buf.write("\u01a6\5\\/\2\u01a5\u01a2\3\2\2\2\u01a5\u01a4\3\2\2\2")
        buf.write("\u01a6[\3\2\2\2\u01a7\u01a8\b/\1\2\u01a8\u01a9\5b\62\2")
        buf.write("\u01a9\u01b1\3\2\2\2\u01aa\u01ad\f\4\2\2\u01ab\u01ae\5")
        buf.write("^\60\2\u01ac\u01ae\5`\61\2\u01ad\u01ab\3\2\2\2\u01ad\u01ac")
        buf.write("\3\2\2\2\u01ae\u01b0\3\2\2\2\u01af\u01aa\3\2\2\2\u01b0")
        buf.write("\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2")
        buf.write("\u01b2]\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4\u01b5\5*\26")
        buf.write("\2\u01b5_\3\2\2\2\u01b6\u01b7\5\60\31\2\u01b7a\3\2\2\2")
        buf.write("\u01b8\u01b9\5d\63\2\u01b9c\3\2\2\2\u01ba\u01bb\7\t\2")
        buf.write("\2\u01bb\u01bc\5N(\2\u01bc\u01bd\7\n\2\2\u01bd\u01c3\3")
        buf.write("\2\2\2\u01be\u01c3\5f\64\2\u01bf\u01c3\7\22\2\2\u01c0")
        buf.write("\u01c3\7\21\2\2\u01c1\u01c3\5D#\2\u01c2\u01ba\3\2\2\2")
        buf.write("\u01c2\u01be\3\2\2\2\u01c2\u01bf\3\2\2\2\u01c2\u01c0\3")
        buf.write("\2\2\2\u01c2\u01c1\3\2\2\2\u01c3e\3\2\2\2\u01c4\u01ca")
        buf.write("\7\17\2\2\u01c5\u01ca\7\20\2\2\u01c6\u01ca\7\60\2\2\u01c7")
        buf.write("\u01ca\5h\65\2\u01c8\u01ca\5l\67\2\u01c9\u01c4\3\2\2\2")
        buf.write("\u01c9\u01c5\3\2\2\2\u01c9\u01c6\3\2\2\2\u01c9\u01c7\3")
        buf.write("\2\2\2\u01c9\u01c8\3\2\2\2\u01cag\3\2\2\2\u01cb\u01d4")
        buf.write("\7\13\2\2\u01cc\u01d1\5j\66\2\u01cd\u01ce\7\4\2\2\u01ce")
        buf.write("\u01d0\5j\66\2\u01cf\u01cd\3\2\2\2\u01d0\u01d3\3\2\2\2")
        buf.write("\u01d1\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d5\3")
        buf.write("\2\2\2\u01d3\u01d1\3\2\2\2\u01d4\u01cc\3\2\2\2\u01d4\u01d5")
        buf.write("\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d7\7\f\2\2\u01d7")
        buf.write("i\3\2\2\2\u01d8\u01d9\7\22\2\2\u01d9\u01da\7\5\2\2\u01da")
        buf.write("\u01db\5f\64\2\u01dbk\3\2\2\2\u01dc\u01e5\7\7\2\2\u01dd")
        buf.write("\u01e2\5n8\2\u01de\u01df\7\4\2\2\u01df\u01e1\5n8\2\u01e0")
        buf.write("\u01de\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2\u01e0\3\2\2\2")
        buf.write("\u01e2\u01e3\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4\u01e2\3")
        buf.write("\2\2\2\u01e5\u01dd\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e7")
        buf.write("\3\2\2\2\u01e7\u01e8\7\b\2\2\u01e8m\3\2\2\2\u01e9\u01ea")
        buf.write("\5N(\2\u01eao\3\2\2\2/sz~\u0089\u008f\u0093\u009c\u009f")
        buf.write("\u00a2\u00ad\u00b3\u00bf\u00c2\u00c5\u00d1\u00da\u00e2")
        buf.write("\u00e4\u00ef\u00f4\u0106\u0113\u011d\u0122\u012c\u0134")
        buf.write("\u013e\u015b\u0164\u016a\u0173\u017a\u0184\u018f\u019a")
        buf.write("\u01a0\u01a5\u01ad\u01b1\u01c2\u01c9\u01d1\u01d4\u01e2")
        buf.write("\u01e5")
        return buf.getvalue()


class CSELParser ( Parser ):

    grammarFileName = "CSEL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "':'", "'='", "'['", "']'", 
                     "'('", "')'", "'{'", "'}'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "<INVALID>", 
                     "'!'", "'+.'", "'==.'", "'Break'", "'Continue'", "'If'", 
                     "'Elif'", "'Else'", "'While'", "'For'", "'Of'", "'In'", 
                     "'Call'", "'Return'", "'Function'", "'Let'", "'Constant'", 
                     "'str2num'", "'num2str'", "'str2bool'", "'bool2str'", 
                     "'print'", "'printLn'", "'read'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "COMMENT", 
                      "LIT_TYPE", "NUMBER", "BOOLEAN", "CON_IDENTIFIERS", 
                      "VAR_IDENTIFIERS", "RELATION_OP", "LOGIC_BINARY_OP", 
                      "PLUS_OP", "MINUS_OP", "MULTIPLYING_OP", "LOGICAL_UNARY_OP", 
                      "PLUS_OP_STR", "RELATION_OP_STR", "BREAK", "CONTINUE", 
                      "IF", "ELIF", "ELSE", "WHILE", "FOR", "OF", "IN", 
                      "CALL", "RETURN", "FUNCTION", "LET", "CONSTANT", "STR2NUM", 
                      "NUM2STR", "STR2BOOL", "BOOL2STR", "PRINT", "PRINTLN", 
                      "READ", "STRINGLIT", "SEP", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_declares = 1
    RULE_var_declare = 2
    RULE_normal_declare = 3
    RULE_var_list = 4
    RULE_var_part = 5
    RULE_var_normal = 6
    RULE_const_declare = 7
    RULE_var_list_const = 8
    RULE_var_part_const = 9
    RULE_var_const = 10
    RULE_var = 11
    RULE_function_declare = 12
    RULE_parameters = 13
    RULE_param_list = 14
    RULE_func_body = 15
    RULE_func_body_stm = 16
    RULE_stm = 17
    RULE_assign_stm = 18
    RULE_index_exp = 19
    RULE_index_op = 20
    RULE_index = 21
    RULE_key_exp = 22
    RULE_key_op = 23
    RULE_if_stm = 24
    RULE_stm_else_if = 25
    RULE_for_stm = 26
    RULE_for_in = 27
    RULE_for_of = 28
    RULE_while_stm = 29
    RULE_break_stm = 30
    RULE_continue_stm = 31
    RULE_call_stm = 32
    RULE_call = 33
    RULE_pass_param = 34
    RULE_params = 35
    RULE_param = 36
    RULE_return_stm = 37
    RULE_exp = 38
    RULE_exp1 = 39
    RULE_exp2 = 40
    RULE_exp3 = 41
    RULE_exp4 = 42
    RULE_exp5 = 43
    RULE_exp6 = 44
    RULE_exp7 = 45
    RULE_index_operator = 46
    RULE_key_operator = 47
    RULE_exp8 = 48
    RULE_operands = 49
    RULE_lit = 50
    RULE_json = 51
    RULE_key_value = 52
    RULE_array = 53
    RULE_element = 54

    ruleNames =  [ "program", "declares", "var_declare", "normal_declare", 
                   "var_list", "var_part", "var_normal", "const_declare", 
                   "var_list_const", "var_part_const", "var_const", "var", 
                   "function_declare", "parameters", "param_list", "func_body", 
                   "func_body_stm", "stm", "assign_stm", "index_exp", "index_op", 
                   "index", "key_exp", "key_op", "if_stm", "stm_else_if", 
                   "for_stm", "for_in", "for_of", "while_stm", "break_stm", 
                   "continue_stm", "call_stm", "call", "pass_param", "params", 
                   "param", "return_stm", "exp", "exp1", "exp2", "exp3", 
                   "exp4", "exp5", "exp6", "exp7", "index_operator", "key_operator", 
                   "exp8", "operands", "lit", "json", "key_value", "array", 
                   "element" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    COMMENT=11
    LIT_TYPE=12
    NUMBER=13
    BOOLEAN=14
    CON_IDENTIFIERS=15
    VAR_IDENTIFIERS=16
    RELATION_OP=17
    LOGIC_BINARY_OP=18
    PLUS_OP=19
    MINUS_OP=20
    MULTIPLYING_OP=21
    LOGICAL_UNARY_OP=22
    PLUS_OP_STR=23
    RELATION_OP_STR=24
    BREAK=25
    CONTINUE=26
    IF=27
    ELIF=28
    ELSE=29
    WHILE=30
    FOR=31
    OF=32
    IN=33
    CALL=34
    RETURN=35
    FUNCTION=36
    LET=37
    CONSTANT=38
    STR2NUM=39
    NUM2STR=40
    STR2BOOL=41
    BOOL2STR=42
    PRINT=43
    PRINTLN=44
    READ=45
    STRINGLIT=46
    SEP=47
    WS=48
    ERROR_CHAR=49
    UNCLOSE_STRING=50
    ILLEGAL_ESCAPE=51
    UNTERMINATED_COMMENT=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CSELParser.EOF, 0)

        def declares(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.DeclaresContext)
            else:
                return self.getTypedRuleContext(CSELParser.DeclaresContext,i)


        def getRuleIndex(self):
            return CSELParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CSELParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.FUNCTION) | (1 << CSELParser.LET) | (1 << CSELParser.CONSTANT))) != 0):
                self.state = 110
                self.declares()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
            self.match(CSELParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaresContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(CSELParser.Var_declareContext,0)


        def function_declare(self):
            return self.getTypedRuleContext(CSELParser.Function_declareContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_declares

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclares" ):
                return visitor.visitDeclares(self)
            else:
                return visitor.visitChildren(self)




    def declares(self):

        localctx = CSELParser.DeclaresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declares)
        try:
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.LET, CSELParser.CONSTANT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.var_declare()
                pass
            elif token in [CSELParser.FUNCTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.function_declare()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normal_declare(self):
            return self.getTypedRuleContext(CSELParser.Normal_declareContext,0)


        def const_declare(self):
            return self.getTypedRuleContext(CSELParser.Const_declareContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = CSELParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_declare)
        try:
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.LET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.normal_declare()
                pass
            elif token in [CSELParser.CONSTANT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.const_declare()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(CSELParser.LET, 0)

        def var_list(self):
            return self.getTypedRuleContext(CSELParser.Var_listContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_normal_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_declare" ):
                return visitor.visitNormal_declare(self)
            else:
                return visitor.visitChildren(self)




    def normal_declare(self):

        localctx = CSELParser.Normal_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_normal_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(CSELParser.LET)
            self.state = 127
            self.var_list()
            self.state = 128
            self.match(CSELParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.Var_partContext)
            else:
                return self.getTypedRuleContext(CSELParser.Var_partContext,i)


        def getRuleIndex(self):
            return CSELParser.RULE_var_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_list" ):
                return visitor.visitVar_list(self)
            else:
                return visitor.visitChildren(self)




    def var_list(self):

        localctx = CSELParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.var_part()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.T__1:
                self.state = 131
                self.match(CSELParser.T__1)
                self.state = 132
                self.var_part()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_normal(self):
            return self.getTypedRuleContext(CSELParser.Var_normalContext,0)


        def LIT_TYPE(self):
            return self.getToken(CSELParser.LIT_TYPE, 0)

        def exp(self):
            return self.getTypedRuleContext(CSELParser.ExpContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_var_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_part" ):
                return visitor.visitVar_part(self)
            else:
                return visitor.visitChildren(self)




    def var_part(self):

        localctx = CSELParser.Var_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.var_normal()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.T__2:
                self.state = 139
                self.match(CSELParser.T__2)
                self.state = 140
                self.match(CSELParser.LIT_TYPE)


            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.T__3:
                self.state = 143
                self.match(CSELParser.T__3)
                self.state = 144
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_normalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_IDENTIFIERS(self):
            return self.getToken(CSELParser.VAR_IDENTIFIERS, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.NUMBER)
            else:
                return self.getToken(CSELParser.NUMBER, i)

        def getRuleIndex(self):
            return CSELParser.RULE_var_normal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_normal" ):
                return visitor.visitVar_normal(self)
            else:
                return visitor.visitChildren(self)




    def var_normal(self):

        localctx = CSELParser.Var_normalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_normal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(CSELParser.VAR_IDENTIFIERS)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.T__4:
                self.state = 148
                self.match(CSELParser.T__4)
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSELParser.NUMBER:
                    self.state = 149
                    self.match(CSELParser.NUMBER)
                    self.state = 154
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==CSELParser.T__1:
                        self.state = 150
                        self.match(CSELParser.T__1)
                        self.state = 151
                        self.match(CSELParser.NUMBER)
                        self.state = 156
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 159
                self.match(CSELParser.T__5)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTANT(self):
            return self.getToken(CSELParser.CONSTANT, 0)

        def var_list_const(self):
            return self.getTypedRuleContext(CSELParser.Var_list_constContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_const_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_declare" ):
                return visitor.visitConst_declare(self)
            else:
                return visitor.visitChildren(self)




    def const_declare(self):

        localctx = CSELParser.Const_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_const_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(CSELParser.CONSTANT)
            self.state = 163
            self.var_list_const()
            self.state = 164
            self.match(CSELParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_list_constContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_part_const(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.Var_part_constContext)
            else:
                return self.getTypedRuleContext(CSELParser.Var_part_constContext,i)


        def getRuleIndex(self):
            return CSELParser.RULE_var_list_const

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_list_const" ):
                return visitor.visitVar_list_const(self)
            else:
                return visitor.visitChildren(self)




    def var_list_const(self):

        localctx = CSELParser.Var_list_constContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_var_list_const)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.var_part_const()
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.T__1:
                self.state = 167
                self.match(CSELParser.T__1)
                self.state = 168
                self.var_part_const()
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_part_constContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_const(self):
            return self.getTypedRuleContext(CSELParser.Var_constContext,0)


        def exp(self):
            return self.getTypedRuleContext(CSELParser.ExpContext,0)


        def LIT_TYPE(self):
            return self.getToken(CSELParser.LIT_TYPE, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_var_part_const

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_part_const" ):
                return visitor.visitVar_part_const(self)
            else:
                return visitor.visitChildren(self)




    def var_part_const(self):

        localctx = CSELParser.Var_part_constContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var_part_const)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.var_const()
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.T__2:
                self.state = 175
                self.match(CSELParser.T__2)
                self.state = 176
                self.match(CSELParser.LIT_TYPE)


            self.state = 179
            self.match(CSELParser.T__3)
            self.state = 180
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_constContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CON_IDENTIFIERS(self):
            return self.getToken(CSELParser.CON_IDENTIFIERS, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.NUMBER)
            else:
                return self.getToken(CSELParser.NUMBER, i)

        def getRuleIndex(self):
            return CSELParser.RULE_var_const

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_const" ):
                return visitor.visitVar_const(self)
            else:
                return visitor.visitChildren(self)




    def var_const(self):

        localctx = CSELParser.Var_constContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_var_const)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(CSELParser.CON_IDENTIFIERS)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.T__4:
                self.state = 183
                self.match(CSELParser.T__4)
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSELParser.NUMBER:
                    self.state = 184
                    self.match(CSELParser.NUMBER)
                    self.state = 189
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==CSELParser.T__1:
                        self.state = 185
                        self.match(CSELParser.T__1)
                        self.state = 186
                        self.match(CSELParser.NUMBER)
                        self.state = 191
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 194
                self.match(CSELParser.T__5)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_normal(self):
            return self.getTypedRuleContext(CSELParser.Var_normalContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = CSELParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.var_normal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(CSELParser.FUNCTION, 0)

        def VAR_IDENTIFIERS(self):
            return self.getToken(CSELParser.VAR_IDENTIFIERS, 0)

        def parameters(self):
            return self.getTypedRuleContext(CSELParser.ParametersContext,0)


        def func_body(self):
            return self.getTypedRuleContext(CSELParser.Func_bodyContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_function_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declare" ):
                return visitor.visitFunction_declare(self)
            else:
                return visitor.visitChildren(self)




    def function_declare(self):

        localctx = CSELParser.Function_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_function_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(CSELParser.FUNCTION)
            self.state = 200
            self.match(CSELParser.VAR_IDENTIFIERS)
            self.state = 201
            self.parameters()
            self.state = 202
            self.func_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_list(self):
            return self.getTypedRuleContext(CSELParser.Param_listContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = CSELParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(CSELParser.T__6)
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.VAR_IDENTIFIERS]:
                self.state = 205
                self.param_list()
                pass
            elif token in [CSELParser.T__7]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 209
            self.match(CSELParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(CSELParser.VarContext,0)


        def param_list(self):
            return self.getTypedRuleContext(CSELParser.Param_listContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = CSELParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param_list)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.var()
                self.state = 212
                self.match(CSELParser.T__1)
                self.state = 213
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_body_stm(self):
            return self.getTypedRuleContext(CSELParser.Func_body_stmContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_func_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = CSELParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_func_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(CSELParser.T__8)
            self.state = 219
            self.func_body_stm()
            self.state = 220
            self.match(CSELParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_body_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(CSELParser.Var_declareContext,i)


        def stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.StmContext)
            else:
                return self.getTypedRuleContext(CSELParser.StmContext,i)


        def getRuleIndex(self):
            return CSELParser.RULE_func_body_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body_stm" ):
                return visitor.visitFunc_body_stm(self)
            else:
                return visitor.visitChildren(self)




    def func_body_stm(self):

        localctx = CSELParser.Func_body_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_func_body_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.VAR_IDENTIFIERS) | (1 << CSELParser.BREAK) | (1 << CSELParser.CONTINUE) | (1 << CSELParser.IF) | (1 << CSELParser.WHILE) | (1 << CSELParser.FOR) | (1 << CSELParser.CALL) | (1 << CSELParser.RETURN) | (1 << CSELParser.LET) | (1 << CSELParser.CONSTANT))) != 0):
                self.state = 224
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSELParser.LET, CSELParser.CONSTANT]:
                    self.state = 222
                    self.var_declare()
                    pass
                elif token in [CSELParser.VAR_IDENTIFIERS, CSELParser.BREAK, CSELParser.CONTINUE, CSELParser.IF, CSELParser.WHILE, CSELParser.FOR, CSELParser.CALL, CSELParser.RETURN]:
                    self.state = 223
                    self.stm()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stm(self):
            return self.getTypedRuleContext(CSELParser.Assign_stmContext,0)


        def if_stm(self):
            return self.getTypedRuleContext(CSELParser.If_stmContext,0)


        def for_stm(self):
            return self.getTypedRuleContext(CSELParser.For_stmContext,0)


        def while_stm(self):
            return self.getTypedRuleContext(CSELParser.While_stmContext,0)


        def break_stm(self):
            return self.getTypedRuleContext(CSELParser.Break_stmContext,0)


        def continue_stm(self):
            return self.getTypedRuleContext(CSELParser.Continue_stmContext,0)


        def call_stm(self):
            return self.getTypedRuleContext(CSELParser.Call_stmContext,0)


        def return_stm(self):
            return self.getTypedRuleContext(CSELParser.Return_stmContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStm" ):
                return visitor.visitStm(self)
            else:
                return visitor.visitChildren(self)




    def stm(self):

        localctx = CSELParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_stm)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.VAR_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.assign_stm()
                pass
            elif token in [CSELParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.if_stm()
                pass
            elif token in [CSELParser.FOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 231
                self.for_stm()
                pass
            elif token in [CSELParser.WHILE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 232
                self.while_stm()
                pass
            elif token in [CSELParser.BREAK]:
                self.enterOuterAlt(localctx, 5)
                self.state = 233
                self.break_stm()
                pass
            elif token in [CSELParser.CONTINUE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 234
                self.continue_stm()
                pass
            elif token in [CSELParser.CALL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 235
                self.call_stm()
                pass
            elif token in [CSELParser.RETURN]:
                self.enterOuterAlt(localctx, 8)
                self.state = 236
                self.return_stm()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(CSELParser.ExpContext,0)


        def VAR_IDENTIFIERS(self):
            return self.getToken(CSELParser.VAR_IDENTIFIERS, 0)

        def index_exp(self):
            return self.getTypedRuleContext(CSELParser.Index_expContext,0)


        def key_exp(self):
            return self.getTypedRuleContext(CSELParser.Key_expContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_assign_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stm" ):
                return visitor.visitAssign_stm(self)
            else:
                return visitor.visitChildren(self)




    def assign_stm(self):

        localctx = CSELParser.Assign_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assign_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 239
                self.match(CSELParser.VAR_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 240
                self.index_exp()
                pass

            elif la_ == 3:
                self.state = 241
                self.key_exp()
                pass


            self.state = 244
            self.match(CSELParser.T__3)
            self.state = 245
            self.exp()
            self.state = 246
            self.match(CSELParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_op(self):
            return self.getTypedRuleContext(CSELParser.Index_opContext,0)


        def VAR_IDENTIFIERS(self):
            return self.getToken(CSELParser.VAR_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_index_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_exp" ):
                return visitor.visitIndex_exp(self)
            else:
                return visitor.visitChildren(self)




    def index_exp(self):

        localctx = CSELParser.Index_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_index_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(CSELParser.VAR_IDENTIFIERS)
            self.state = 249
            self.index_op()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index(self):
            return self.getTypedRuleContext(CSELParser.IndexContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op" ):
                return visitor.visitIndex_op(self)
            else:
                return visitor.visitChildren(self)




    def index_op(self):

        localctx = CSELParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_index_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(CSELParser.T__4)
            self.state = 252
            self.index()
            self.state = 253
            self.match(CSELParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(CSELParser.ExpContext,0)


        def index(self):
            return self.getTypedRuleContext(CSELParser.IndexContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)




    def index(self):

        localctx = CSELParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_index)
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.exp()
                self.state = 256
                self.match(CSELParser.T__1)
                self.state = 257
                self.index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Key_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key_op(self):
            return self.getTypedRuleContext(CSELParser.Key_opContext,0)


        def VAR_IDENTIFIERS(self):
            return self.getToken(CSELParser.VAR_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_key_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey_exp" ):
                return visitor.visitKey_exp(self)
            else:
                return visitor.visitChildren(self)




    def key_exp(self):

        localctx = CSELParser.Key_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_key_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(CSELParser.VAR_IDENTIFIERS)
            self.state = 263
            self.key_op()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Key_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLIT(self):
            return self.getToken(CSELParser.STRINGLIT, 0)

        def key_op(self):
            return self.getTypedRuleContext(CSELParser.Key_opContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_key_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey_op" ):
                return visitor.visitKey_op(self)
            else:
                return visitor.visitChildren(self)




    def key_op(self):

        localctx = CSELParser.Key_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_key_op)
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(CSELParser.T__4)
                self.state = 266
                self.match(CSELParser.STRINGLIT)
                self.state = 267
                self.match(CSELParser.T__5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.match(CSELParser.T__4)
                self.state = 269
                self.match(CSELParser.STRINGLIT)
                self.state = 270
                self.match(CSELParser.T__5)
                self.state = 272
                self.key_op()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CSELParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(CSELParser.ExpContext,0)


        def func_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.Func_bodyContext)
            else:
                return self.getTypedRuleContext(CSELParser.Func_bodyContext,i)


        def stm_else_if(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.Stm_else_ifContext)
            else:
                return self.getTypedRuleContext(CSELParser.Stm_else_ifContext,i)


        def ELSE(self):
            return self.getToken(CSELParser.ELSE, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_if_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stm" ):
                return visitor.visitIf_stm(self)
            else:
                return visitor.visitChildren(self)




    def if_stm(self):

        localctx = CSELParser.If_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_if_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(CSELParser.IF)
            self.state = 276
            self.match(CSELParser.T__6)
            self.state = 277
            self.exp()
            self.state = 278
            self.match(CSELParser.T__7)
            self.state = 279
            self.func_body()
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.ELIF:
                self.state = 280
                self.stm_else_if()
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.ELSE:
                self.state = 286
                self.match(CSELParser.ELSE)
                self.state = 287
                self.func_body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stm_else_ifContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(CSELParser.ELIF, 0)

        def exp(self):
            return self.getTypedRuleContext(CSELParser.ExpContext,0)


        def func_body(self):
            return self.getTypedRuleContext(CSELParser.Func_bodyContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_stm_else_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStm_else_if" ):
                return visitor.visitStm_else_if(self)
            else:
                return visitor.visitChildren(self)




    def stm_else_if(self):

        localctx = CSELParser.Stm_else_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_stm_else_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(CSELParser.ELIF)
            self.state = 291
            self.match(CSELParser.T__6)
            self.state = 292
            self.exp()
            self.state = 293
            self.match(CSELParser.T__7)
            self.state = 294
            self.func_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_in(self):
            return self.getTypedRuleContext(CSELParser.For_inContext,0)


        def for_of(self):
            return self.getTypedRuleContext(CSELParser.For_ofContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_for_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stm" ):
                return visitor.visitFor_stm(self)
            else:
                return visitor.visitChildren(self)




    def for_stm(self):

        localctx = CSELParser.For_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_for_stm)
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.for_in()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.for_of()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_inContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSELParser.FOR, 0)

        def VAR_IDENTIFIERS(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.VAR_IDENTIFIERS)
            else:
                return self.getToken(CSELParser.VAR_IDENTIFIERS, i)

        def IN(self):
            return self.getToken(CSELParser.IN, 0)

        def func_body(self):
            return self.getTypedRuleContext(CSELParser.Func_bodyContext,0)


        def array(self):
            return self.getTypedRuleContext(CSELParser.ArrayContext,0)


        def CON_IDENTIFIERS(self):
            return self.getToken(CSELParser.CON_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_for_in

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in" ):
                return visitor.visitFor_in(self)
            else:
                return visitor.visitChildren(self)




    def for_in(self):

        localctx = CSELParser.For_inContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_for_in)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(CSELParser.FOR)
            self.state = 301
            self.match(CSELParser.VAR_IDENTIFIERS)
            self.state = 302
            self.match(CSELParser.IN)
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.T__4]:
                self.state = 303
                self.array()
                pass
            elif token in [CSELParser.VAR_IDENTIFIERS]:
                self.state = 304
                self.match(CSELParser.VAR_IDENTIFIERS)
                pass
            elif token in [CSELParser.CON_IDENTIFIERS]:
                self.state = 305
                self.match(CSELParser.CON_IDENTIFIERS)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 308
            self.func_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_ofContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSELParser.FOR, 0)

        def VAR_IDENTIFIERS(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.VAR_IDENTIFIERS)
            else:
                return self.getToken(CSELParser.VAR_IDENTIFIERS, i)

        def OF(self):
            return self.getToken(CSELParser.OF, 0)

        def func_body(self):
            return self.getTypedRuleContext(CSELParser.Func_bodyContext,0)


        def json(self):
            return self.getTypedRuleContext(CSELParser.JsonContext,0)


        def CON_IDENTIFIERS(self):
            return self.getToken(CSELParser.CON_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_for_of

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_of" ):
                return visitor.visitFor_of(self)
            else:
                return visitor.visitChildren(self)




    def for_of(self):

        localctx = CSELParser.For_ofContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_for_of)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(CSELParser.FOR)
            self.state = 311
            self.match(CSELParser.VAR_IDENTIFIERS)
            self.state = 312
            self.match(CSELParser.OF)
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.T__8]:
                self.state = 313
                self.json()
                pass
            elif token in [CSELParser.VAR_IDENTIFIERS]:
                self.state = 314
                self.match(CSELParser.VAR_IDENTIFIERS)
                pass
            elif token in [CSELParser.CON_IDENTIFIERS]:
                self.state = 315
                self.match(CSELParser.CON_IDENTIFIERS)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 318
            self.func_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(CSELParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(CSELParser.ExpContext,0)


        def func_body(self):
            return self.getTypedRuleContext(CSELParser.Func_bodyContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_while_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stm" ):
                return visitor.visitWhile_stm(self)
            else:
                return visitor.visitChildren(self)




    def while_stm(self):

        localctx = CSELParser.While_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_while_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(CSELParser.WHILE)
            self.state = 321
            self.match(CSELParser.T__6)
            self.state = 322
            self.exp()
            self.state = 323
            self.match(CSELParser.T__7)
            self.state = 324
            self.func_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(CSELParser.BREAK, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_break_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stm" ):
                return visitor.visitBreak_stm(self)
            else:
                return visitor.visitChildren(self)




    def break_stm(self):

        localctx = CSELParser.Break_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_break_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(CSELParser.BREAK)
            self.state = 327
            self.match(CSELParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(CSELParser.CONTINUE, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_continue_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stm" ):
                return visitor.visitContinue_stm(self)
            else:
                return visitor.visitChildren(self)




    def continue_stm(self):

        localctx = CSELParser.Continue_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_continue_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(CSELParser.CONTINUE)
            self.state = 330
            self.match(CSELParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self):
            return self.getTypedRuleContext(CSELParser.CallContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_call_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stm" ):
                return visitor.visitCall_stm(self)
            else:
                return visitor.visitChildren(self)




    def call_stm(self):

        localctx = CSELParser.Call_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_call_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.call()
            self.state = 333
            self.match(CSELParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CALL(self):
            return self.getToken(CSELParser.CALL, 0)

        def pass_param(self):
            return self.getTypedRuleContext(CSELParser.Pass_paramContext,0)


        def VAR_IDENTIFIERS(self):
            return self.getToken(CSELParser.VAR_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = CSELParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(CSELParser.CALL)
            self.state = 336
            self.match(CSELParser.T__6)

            self.state = 337
            self.match(CSELParser.VAR_IDENTIFIERS)
            self.state = 338
            self.match(CSELParser.T__1)
            self.state = 339
            self.pass_param()
            self.state = 340
            self.match(CSELParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pass_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params(self):
            return self.getTypedRuleContext(CSELParser.ParamsContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_pass_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPass_param" ):
                return visitor.visitPass_param(self)
            else:
                return visitor.visitChildren(self)




    def pass_param(self):

        localctx = CSELParser.Pass_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_pass_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(CSELParser.T__4)
            self.state = 345
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.T__4, CSELParser.T__6, CSELParser.T__8, CSELParser.NUMBER, CSELParser.BOOLEAN, CSELParser.CON_IDENTIFIERS, CSELParser.VAR_IDENTIFIERS, CSELParser.MINUS_OP, CSELParser.LOGICAL_UNARY_OP, CSELParser.CALL, CSELParser.STRINGLIT]:
                self.state = 343
                self.params()
                pass
            elif token in [CSELParser.T__5]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 347
            self.match(CSELParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(CSELParser.ParamContext,0)


        def params(self):
            return self.getTypedRuleContext(CSELParser.ParamsContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = CSELParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_params)
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.param()
                self.state = 350
                self.match(CSELParser.T__1)
                self.state = 351
                self.params()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(CSELParser.ExpContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = CSELParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CSELParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(CSELParser.ExpContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_return_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stm" ):
                return visitor.visitReturn_stm(self)
            else:
                return visitor.visitChildren(self)




    def return_stm(self):

        localctx = CSELParser.Return_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_return_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(CSELParser.RETURN)
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.T__4) | (1 << CSELParser.T__6) | (1 << CSELParser.T__8) | (1 << CSELParser.NUMBER) | (1 << CSELParser.BOOLEAN) | (1 << CSELParser.CON_IDENTIFIERS) | (1 << CSELParser.VAR_IDENTIFIERS) | (1 << CSELParser.MINUS_OP) | (1 << CSELParser.LOGICAL_UNARY_OP) | (1 << CSELParser.CALL) | (1 << CSELParser.STRINGLIT))) != 0):
                self.state = 359
                self.exp()


            self.state = 362
            self.match(CSELParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.Exp1Context)
            else:
                return self.getTypedRuleContext(CSELParser.Exp1Context,i)


        def RELATION_OP_STR(self):
            return self.getToken(CSELParser.RELATION_OP_STR, 0)

        def PLUS_OP_STR(self):
            return self.getToken(CSELParser.PLUS_OP_STR, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = CSELParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.exp1()
                self.state = 365
                _la = self._input.LA(1)
                if not(_la==CSELParser.PLUS_OP_STR or _la==CSELParser.RELATION_OP_STR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 366
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.Exp2Context)
            else:
                return self.getTypedRuleContext(CSELParser.Exp2Context,i)


        def RELATION_OP(self):
            return self.getToken(CSELParser.RELATION_OP, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = CSELParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_exp1)
        try:
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.exp2(0)
                self.state = 372
                self.match(CSELParser.RELATION_OP)
                self.state = 373
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(CSELParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(CSELParser.Exp2Context,0)


        def LOGIC_BINARY_OP(self):
            return self.getToken(CSELParser.LOGIC_BINARY_OP, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSELParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 386
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSELParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 381
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 382
                    self.match(CSELParser.LOGIC_BINARY_OP)
                    self.state = 383
                    self.exp3(0) 
                self.state = 388
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(CSELParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(CSELParser.Exp3Context,0)


        def PLUS_OP(self):
            return self.getToken(CSELParser.PLUS_OP, 0)

        def MINUS_OP(self):
            return self.getToken(CSELParser.MINUS_OP, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSELParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 397
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSELParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 392
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 393
                    _la = self._input.LA(1)
                    if not(_la==CSELParser.PLUS_OP or _la==CSELParser.MINUS_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 394
                    self.exp4(0) 
                self.state = 399
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(CSELParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(CSELParser.Exp4Context,0)


        def MULTIPLYING_OP(self):
            return self.getToken(CSELParser.MULTIPLYING_OP, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSELParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 408
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSELParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 403
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 404
                    self.match(CSELParser.MULTIPLYING_OP)
                    self.state = 405
                    self.exp5() 
                self.state = 410
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOGICAL_UNARY_OP(self):
            return self.getToken(CSELParser.LOGICAL_UNARY_OP, 0)

        def exp5(self):
            return self.getTypedRuleContext(CSELParser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(CSELParser.Exp6Context,0)


        def getRuleIndex(self):
            return CSELParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = CSELParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_exp5)
        try:
            self.state = 414
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.LOGICAL_UNARY_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.match(CSELParser.LOGICAL_UNARY_OP)
                self.state = 412
                self.exp5()
                pass
            elif token in [CSELParser.T__4, CSELParser.T__6, CSELParser.T__8, CSELParser.NUMBER, CSELParser.BOOLEAN, CSELParser.CON_IDENTIFIERS, CSELParser.VAR_IDENTIFIERS, CSELParser.MINUS_OP, CSELParser.CALL, CSELParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.exp6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS_OP(self):
            return self.getToken(CSELParser.MINUS_OP, 0)

        def exp6(self):
            return self.getTypedRuleContext(CSELParser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(CSELParser.Exp7Context,0)


        def getRuleIndex(self):
            return CSELParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = CSELParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_exp6)
        try:
            self.state = 419
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.MINUS_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.match(CSELParser.MINUS_OP)
                self.state = 417
                self.exp6()
                pass
            elif token in [CSELParser.T__4, CSELParser.T__6, CSELParser.T__8, CSELParser.NUMBER, CSELParser.BOOLEAN, CSELParser.CON_IDENTIFIERS, CSELParser.VAR_IDENTIFIERS, CSELParser.CALL, CSELParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 418
                self.exp7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(CSELParser.Exp8Context,0)


        def exp7(self):
            return self.getTypedRuleContext(CSELParser.Exp7Context,0)


        def index_operator(self):
            return self.getTypedRuleContext(CSELParser.Index_operatorContext,0)


        def key_operator(self):
            return self.getTypedRuleContext(CSELParser.Key_operatorContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)



    def exp7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSELParser.Exp7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_exp7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.exp8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 431
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSELParser.Exp7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                    self.state = 424
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 427
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        self.state = 425
                        self.index_operator()
                        pass

                    elif la_ == 2:
                        self.state = 426
                        self.key_operator()
                        pass

             
                self.state = 433
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Index_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_op(self):
            return self.getTypedRuleContext(CSELParser.Index_opContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = CSELParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_index_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.index_op()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Key_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key_op(self):
            return self.getTypedRuleContext(CSELParser.Key_opContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_key_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey_operator" ):
                return visitor.visitKey_operator(self)
            else:
                return visitor.visitChildren(self)




    def key_operator(self):

        localctx = CSELParser.Key_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_key_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.key_op()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operands(self):
            return self.getTypedRuleContext(CSELParser.OperandsContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = CSELParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_exp8)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.operands()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(CSELParser.ExpContext,0)


        def lit(self):
            return self.getTypedRuleContext(CSELParser.LitContext,0)


        def VAR_IDENTIFIERS(self):
            return self.getToken(CSELParser.VAR_IDENTIFIERS, 0)

        def CON_IDENTIFIERS(self):
            return self.getToken(CSELParser.CON_IDENTIFIERS, 0)

        def call(self):
            return self.getTypedRuleContext(CSELParser.CallContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = CSELParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_operands)
        try:
            self.state = 448
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.match(CSELParser.T__6)
                self.state = 441
                self.exp()
                self.state = 442
                self.match(CSELParser.T__7)
                pass
            elif token in [CSELParser.T__4, CSELParser.T__8, CSELParser.NUMBER, CSELParser.BOOLEAN, CSELParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
                self.lit()
                pass
            elif token in [CSELParser.VAR_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 445
                self.match(CSELParser.VAR_IDENTIFIERS)
                pass
            elif token in [CSELParser.CON_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 446
                self.match(CSELParser.CON_IDENTIFIERS)
                pass
            elif token in [CSELParser.CALL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 447
                self.call()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(CSELParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(CSELParser.BOOLEAN, 0)

        def STRINGLIT(self):
            return self.getToken(CSELParser.STRINGLIT, 0)

        def json(self):
            return self.getTypedRuleContext(CSELParser.JsonContext,0)


        def array(self):
            return self.getTypedRuleContext(CSELParser.ArrayContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit" ):
                return visitor.visitLit(self)
            else:
                return visitor.visitChildren(self)




    def lit(self):

        localctx = CSELParser.LitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_lit)
        try:
            self.state = 455
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.match(CSELParser.NUMBER)
                pass
            elif token in [CSELParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                self.match(CSELParser.BOOLEAN)
                pass
            elif token in [CSELParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 452
                self.match(CSELParser.STRINGLIT)
                pass
            elif token in [CSELParser.T__8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 453
                self.json()
                pass
            elif token in [CSELParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 454
                self.array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JsonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.Key_valueContext)
            else:
                return self.getTypedRuleContext(CSELParser.Key_valueContext,i)


        def getRuleIndex(self):
            return CSELParser.RULE_json

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJson" ):
                return visitor.visitJson(self)
            else:
                return visitor.visitChildren(self)




    def json(self):

        localctx = CSELParser.JsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_json)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(CSELParser.T__8)
            self.state = 466
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.VAR_IDENTIFIERS:
                self.state = 458
                self.key_value()
                self.state = 463
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSELParser.T__1:
                    self.state = 459
                    self.match(CSELParser.T__1)
                    self.state = 460
                    self.key_value()
                    self.state = 465
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 468
            self.match(CSELParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Key_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lit(self):
            return self.getTypedRuleContext(CSELParser.LitContext,0)


        def VAR_IDENTIFIERS(self):
            return self.getToken(CSELParser.VAR_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_key_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey_value" ):
                return visitor.visitKey_value(self)
            else:
                return visitor.visitChildren(self)




    def key_value(self):

        localctx = CSELParser.Key_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_key_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.match(CSELParser.VAR_IDENTIFIERS)
            self.state = 471
            self.match(CSELParser.T__2)
            self.state = 472
            self.lit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.ElementContext)
            else:
                return self.getTypedRuleContext(CSELParser.ElementContext,i)


        def getRuleIndex(self):
            return CSELParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = CSELParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(CSELParser.T__4)
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.T__4) | (1 << CSELParser.T__6) | (1 << CSELParser.T__8) | (1 << CSELParser.NUMBER) | (1 << CSELParser.BOOLEAN) | (1 << CSELParser.CON_IDENTIFIERS) | (1 << CSELParser.VAR_IDENTIFIERS) | (1 << CSELParser.MINUS_OP) | (1 << CSELParser.LOGICAL_UNARY_OP) | (1 << CSELParser.CALL) | (1 << CSELParser.STRINGLIT))) != 0):
                self.state = 475
                self.element()
                self.state = 480
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSELParser.T__1:
                    self.state = 476
                    self.match(CSELParser.T__1)
                    self.state = 477
                    self.element()
                    self.state = 482
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 485
            self.match(CSELParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(CSELParser.ExpContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = CSELParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[40] = self.exp2_sempred
        self._predicates[41] = self.exp3_sempred
        self._predicates[42] = self.exp4_sempred
        self._predicates[45] = self.exp7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp7_sempred(self, localctx:Exp7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




