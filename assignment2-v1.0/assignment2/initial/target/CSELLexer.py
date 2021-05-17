# Generated from main/csel/parser/CSEL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u01e0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\7\21\u00b9\n\21\f\21\16\21\u00bc\13\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\5\22\u00c5\n\22\3")
        buf.write("\22\5\22\u00c8\n\22\3\23\6\23\u00cb\n\23\r\23\16\23\u00cc")
        buf.write("\3\24\3\24\7\24\u00d1\n\24\f\24\16\24\u00d4\13\24\3\25")
        buf.write("\3\25\5\25\u00d8\n\25\3\25\6\25\u00db\n\25\r\25\16\25")
        buf.write("\u00dc\3\26\3\26\5\26\u00e1\n\26\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\6\31\u00f0")
        buf.write("\n\31\r\31\16\31\u00f1\3\32\3\32\7\32\u00f6\n\32\f\32")
        buf.write("\16\32\u00f9\13\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\5\33\u0104\n\33\3\34\3\34\3\34\3\34\5\34\u010a")
        buf.write("\n\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\3,\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write("/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\38\38\7")
        buf.write("8\u01a0\n8\f8\168\u01a3\138\38\38\38\39\39\39\39\39\5")
        buf.write("9\u01ad\n9\3:\3:\3;\6;\u01b2\n;\r;\16;\u01b3\3;\3;\3<")
        buf.write("\3<\3<\3=\3=\7=\u01bd\n=\f=\16=\u01c0\13=\3=\5=\u01c3")
        buf.write("\n=\3=\3=\3>\3>\7>\u01c9\n>\f>\16>\u01cc\13>\3>\3>\3>")
        buf.write("\3>\5>\u01d2\n>\3>\3>\3?\3?\3?\3?\7?\u01da\n?\f?\16?\u01dd")
        buf.write("\13?\3?\3?\4\u00ba\u01db\2@\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\2\'\2)\2+\24-\2/\2\61\25\63\26\65\27\67\309\31;\32=")
        buf.write("\33?\34A\35C\36E\37G I!K\"M#O$Q%S&U\'W(Y)[*]+_,a-c.e/")
        buf.write("g\60i\61k\62m\63o\64q\2s\65u\66w\67y8{9}:\3\2\17\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\6\2\62;C\\aac|\3\2c|\4\2>>@@\5\2\'\'")
        buf.write(",,\61\61\7\2\f\f\17\17$$))^^\t\2))^^ddhhppttvv\n\2*+.")
        buf.write(".\60\60<=]]__}}\177\177\5\2\13\f\17\17\"\"\4\3\n\f\16")
        buf.write("\17\3\2$$\2\u01f0\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2+\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2")
        buf.write("\2{\3\2\2\2\2}\3\2\2\2\3\177\3\2\2\2\5\u0081\3\2\2\2\7")
        buf.write("\u0083\3\2\2\2\t\u0085\3\2\2\2\13\u0087\3\2\2\2\r\u0089")
        buf.write("\3\2\2\2\17\u008b\3\2\2\2\21\u008d\3\2\2\2\23\u008f\3")
        buf.write("\2\2\2\25\u0091\3\2\2\2\27\u0093\3\2\2\2\31\u009a\3\2")
        buf.write("\2\2\33\u00a2\3\2\2\2\35\u00a8\3\2\2\2\37\u00ad\3\2\2")
        buf.write("\2!\u00b4\3\2\2\2#\u00c2\3\2\2\2%\u00ca\3\2\2\2\'\u00ce")
        buf.write("\3\2\2\2)\u00d5\3\2\2\2+\u00e0\3\2\2\2-\u00e2\3\2\2\2")
        buf.write("/\u00e7\3\2\2\2\61\u00ed\3\2\2\2\63\u00f3\3\2\2\2\65\u0103")
        buf.write("\3\2\2\2\67\u0109\3\2\2\29\u010b\3\2\2\2;\u010d\3\2\2")
        buf.write("\2=\u010f\3\2\2\2?\u0111\3\2\2\2A\u0113\3\2\2\2C\u0116")
        buf.write("\3\2\2\2E\u011a\3\2\2\2G\u0120\3\2\2\2I\u0129\3\2\2\2")
        buf.write("K\u012c\3\2\2\2M\u0131\3\2\2\2O\u0136\3\2\2\2Q\u013c\3")
        buf.write("\2\2\2S\u0140\3\2\2\2U\u0143\3\2\2\2W\u0146\3\2\2\2Y\u014b")
        buf.write("\3\2\2\2[\u0152\3\2\2\2]\u015b\3\2\2\2_\u015f\3\2\2\2")
        buf.write("a\u0168\3\2\2\2c\u0170\3\2\2\2e\u0178\3\2\2\2g\u0181\3")
        buf.write("\2\2\2i\u018a\3\2\2\2k\u0190\3\2\2\2m\u0198\3\2\2\2o\u019d")
        buf.write("\3\2\2\2q\u01ac\3\2\2\2s\u01ae\3\2\2\2u\u01b1\3\2\2\2")
        buf.write("w\u01b7\3\2\2\2y\u01ba\3\2\2\2{\u01c6\3\2\2\2}\u01d5\3")
        buf.write("\2\2\2\177\u0080\7=\2\2\u0080\4\3\2\2\2\u0081\u0082\7")
        buf.write(".\2\2\u0082\6\3\2\2\2\u0083\u0084\7<\2\2\u0084\b\3\2\2")
        buf.write("\2\u0085\u0086\7?\2\2\u0086\n\3\2\2\2\u0087\u0088\7]\2")
        buf.write("\2\u0088\f\3\2\2\2\u0089\u008a\7_\2\2\u008a\16\3\2\2\2")
        buf.write("\u008b\u008c\7*\2\2\u008c\20\3\2\2\2\u008d\u008e\7+\2")
        buf.write("\2\u008e\22\3\2\2\2\u008f\u0090\7}\2\2\u0090\24\3\2\2")
        buf.write("\2\u0091\u0092\7\177\2\2\u0092\26\3\2\2\2\u0093\u0094")
        buf.write("\7P\2\2\u0094\u0095\7w\2\2\u0095\u0096\7o\2\2\u0096\u0097")
        buf.write("\7d\2\2\u0097\u0098\7g\2\2\u0098\u0099\7t\2\2\u0099\30")
        buf.write("\3\2\2\2\u009a\u009b\7D\2\2\u009b\u009c\7q\2\2\u009c\u009d")
        buf.write("\7q\2\2\u009d\u009e\7n\2\2\u009e\u009f\7g\2\2\u009f\u00a0")
        buf.write("\7c\2\2\u00a0\u00a1\7p\2\2\u00a1\32\3\2\2\2\u00a2\u00a3")
        buf.write("\7C\2\2\u00a3\u00a4\7t\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6")
        buf.write("\7c\2\2\u00a6\u00a7\7{\2\2\u00a7\34\3\2\2\2\u00a8\u00a9")
        buf.write("\7L\2\2\u00a9\u00aa\7U\2\2\u00aa\u00ab\7Q\2\2\u00ab\u00ac")
        buf.write("\7P\2\2\u00ac\36\3\2\2\2\u00ad\u00ae\7U\2\2\u00ae\u00af")
        buf.write("\7v\2\2\u00af\u00b0\7t\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2")
        buf.write("\7p\2\2\u00b2\u00b3\7i\2\2\u00b3 \3\2\2\2\u00b4\u00b5")
        buf.write("\7%\2\2\u00b5\u00b6\7%\2\2\u00b6\u00ba\3\2\2\2\u00b7\u00b9")
        buf.write("\13\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba")
        buf.write("\u00bb\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00bd\3\2\2\2")
        buf.write("\u00bc\u00ba\3\2\2\2\u00bd\u00be\7%\2\2\u00be\u00bf\7")
        buf.write("%\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1\b\21\2\2\u00c1\"")
        buf.write("\3\2\2\2\u00c2\u00c4\5%\23\2\u00c3\u00c5\5\'\24\2\u00c4")
        buf.write("\u00c3\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c7\3\2\2\2")
        buf.write("\u00c6\u00c8\5)\25\2\u00c7\u00c6\3\2\2\2\u00c7\u00c8\3")
        buf.write("\2\2\2\u00c8$\3\2\2\2\u00c9\u00cb\t\2\2\2\u00ca\u00c9")
        buf.write("\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc")
        buf.write("\u00cd\3\2\2\2\u00cd&\3\2\2\2\u00ce\u00d2\7\60\2\2\u00cf")
        buf.write("\u00d1\t\2\2\2\u00d0\u00cf\3\2\2\2\u00d1\u00d4\3\2\2\2")
        buf.write("\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3(\3\2\2")
        buf.write("\2\u00d4\u00d2\3\2\2\2\u00d5\u00d7\t\3\2\2\u00d6\u00d8")
        buf.write("\t\4\2\2\u00d7\u00d6\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8")
        buf.write("\u00da\3\2\2\2\u00d9\u00db\t\2\2\2\u00da\u00d9\3\2\2\2")
        buf.write("\u00db\u00dc\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3")
        buf.write("\2\2\2\u00dd*\3\2\2\2\u00de\u00e1\5-\27\2\u00df\u00e1")
        buf.write("\5/\30\2\u00e0\u00de\3\2\2\2\u00e0\u00df\3\2\2\2\u00e1")
        buf.write(",\3\2\2\2\u00e2\u00e3\7V\2\2\u00e3\u00e4\7t\2\2\u00e4")
        buf.write("\u00e5\7w\2\2\u00e5\u00e6\7g\2\2\u00e6.\3\2\2\2\u00e7")
        buf.write("\u00e8\7H\2\2\u00e8\u00e9\7c\2\2\u00e9\u00ea\7n\2\2\u00ea")
        buf.write("\u00eb\7u\2\2\u00eb\u00ec\7g\2\2\u00ec\60\3\2\2\2\u00ed")
        buf.write("\u00ef\7&\2\2\u00ee\u00f0\t\5\2\2\u00ef\u00ee\3\2\2\2")
        buf.write("\u00f0\u00f1\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3")
        buf.write("\2\2\2\u00f2\62\3\2\2\2\u00f3\u00f7\t\6\2\2\u00f4\u00f6")
        buf.write("\t\5\2\2\u00f5\u00f4\3\2\2\2\u00f6\u00f9\3\2\2\2\u00f7")
        buf.write("\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\64\3\2\2\2\u00f9")
        buf.write("\u00f7\3\2\2\2\u00fa\u00fb\7?\2\2\u00fb\u0104\7?\2\2\u00fc")
        buf.write("\u00fd\7#\2\2\u00fd\u0104\7?\2\2\u00fe\u0104\t\7\2\2\u00ff")
        buf.write("\u0100\7>\2\2\u0100\u0104\7?\2\2\u0101\u0102\7@\2\2\u0102")
        buf.write("\u0104\7?\2\2\u0103\u00fa\3\2\2\2\u0103\u00fc\3\2\2\2")
        buf.write("\u0103\u00fe\3\2\2\2\u0103\u00ff\3\2\2\2\u0103\u0101\3")
        buf.write("\2\2\2\u0104\66\3\2\2\2\u0105\u0106\7(\2\2\u0106\u010a")
        buf.write("\7(\2\2\u0107\u0108\7~\2\2\u0108\u010a\7~\2\2\u0109\u0105")
        buf.write("\3\2\2\2\u0109\u0107\3\2\2\2\u010a8\3\2\2\2\u010b\u010c")
        buf.write("\7-\2\2\u010c:\3\2\2\2\u010d\u010e\7/\2\2\u010e<\3\2\2")
        buf.write("\2\u010f\u0110\t\b\2\2\u0110>\3\2\2\2\u0111\u0112\7#\2")
        buf.write("\2\u0112@\3\2\2\2\u0113\u0114\7-\2\2\u0114\u0115\7\60")
        buf.write("\2\2\u0115B\3\2\2\2\u0116\u0117\7?\2\2\u0117\u0118\7?")
        buf.write("\2\2\u0118\u0119\7\60\2\2\u0119D\3\2\2\2\u011a\u011b\7")
        buf.write("D\2\2\u011b\u011c\7t\2\2\u011c\u011d\7g\2\2\u011d\u011e")
        buf.write("\7c\2\2\u011e\u011f\7m\2\2\u011fF\3\2\2\2\u0120\u0121")
        buf.write("\7E\2\2\u0121\u0122\7q\2\2\u0122\u0123\7p\2\2\u0123\u0124")
        buf.write("\7v\2\2\u0124\u0125\7k\2\2\u0125\u0126\7p\2\2\u0126\u0127")
        buf.write("\7w\2\2\u0127\u0128\7g\2\2\u0128H\3\2\2\2\u0129\u012a")
        buf.write("\7K\2\2\u012a\u012b\7h\2\2\u012bJ\3\2\2\2\u012c\u012d")
        buf.write("\7G\2\2\u012d\u012e\7n\2\2\u012e\u012f\7k\2\2\u012f\u0130")
        buf.write("\7h\2\2\u0130L\3\2\2\2\u0131\u0132\7G\2\2\u0132\u0133")
        buf.write("\7n\2\2\u0133\u0134\7u\2\2\u0134\u0135\7g\2\2\u0135N\3")
        buf.write("\2\2\2\u0136\u0137\7Y\2\2\u0137\u0138\7j\2\2\u0138\u0139")
        buf.write("\7k\2\2\u0139\u013a\7n\2\2\u013a\u013b\7g\2\2\u013bP\3")
        buf.write("\2\2\2\u013c\u013d\7H\2\2\u013d\u013e\7q\2\2\u013e\u013f")
        buf.write("\7t\2\2\u013fR\3\2\2\2\u0140\u0141\7Q\2\2\u0141\u0142")
        buf.write("\7h\2\2\u0142T\3\2\2\2\u0143\u0144\7K\2\2\u0144\u0145")
        buf.write("\7p\2\2\u0145V\3\2\2\2\u0146\u0147\7E\2\2\u0147\u0148")
        buf.write("\7c\2\2\u0148\u0149\7n\2\2\u0149\u014a\7n\2\2\u014aX\3")
        buf.write("\2\2\2\u014b\u014c\7T\2\2\u014c\u014d\7g\2\2\u014d\u014e")
        buf.write("\7v\2\2\u014e\u014f\7w\2\2\u014f\u0150\7t\2\2\u0150\u0151")
        buf.write("\7p\2\2\u0151Z\3\2\2\2\u0152\u0153\7H\2\2\u0153\u0154")
        buf.write("\7w\2\2\u0154\u0155\7p\2\2\u0155\u0156\7e\2\2\u0156\u0157")
        buf.write("\7v\2\2\u0157\u0158\7k\2\2\u0158\u0159\7q\2\2\u0159\u015a")
        buf.write("\7p\2\2\u015a\\\3\2\2\2\u015b\u015c\7N\2\2\u015c\u015d")
        buf.write("\7g\2\2\u015d\u015e\7v\2\2\u015e^\3\2\2\2\u015f\u0160")
        buf.write("\7E\2\2\u0160\u0161\7q\2\2\u0161\u0162\7p\2\2\u0162\u0163")
        buf.write("\7u\2\2\u0163\u0164\7v\2\2\u0164\u0165\7c\2\2\u0165\u0166")
        buf.write("\7p\2\2\u0166\u0167\7v\2\2\u0167`\3\2\2\2\u0168\u0169")
        buf.write("\7u\2\2\u0169\u016a\7v\2\2\u016a\u016b\7t\2\2\u016b\u016c")
        buf.write("\7\64\2\2\u016c\u016d\7p\2\2\u016d\u016e\7w\2\2\u016e")
        buf.write("\u016f\7o\2\2\u016fb\3\2\2\2\u0170\u0171\7p\2\2\u0171")
        buf.write("\u0172\7w\2\2\u0172\u0173\7o\2\2\u0173\u0174\7\64\2\2")
        buf.write("\u0174\u0175\7u\2\2\u0175\u0176\7v\2\2\u0176\u0177\7t")
        buf.write("\2\2\u0177d\3\2\2\2\u0178\u0179\7u\2\2\u0179\u017a\7v")
        buf.write("\2\2\u017a\u017b\7t\2\2\u017b\u017c\7\64\2\2\u017c\u017d")
        buf.write("\7d\2\2\u017d\u017e\7q\2\2\u017e\u017f\7q\2\2\u017f\u0180")
        buf.write("\7n\2\2\u0180f\3\2\2\2\u0181\u0182\7d\2\2\u0182\u0183")
        buf.write("\7q\2\2\u0183\u0184\7q\2\2\u0184\u0185\7n\2\2\u0185\u0186")
        buf.write("\7\64\2\2\u0186\u0187\7u\2\2\u0187\u0188\7v\2\2\u0188")
        buf.write("\u0189\7t\2\2\u0189h\3\2\2\2\u018a\u018b\7r\2\2\u018b")
        buf.write("\u018c\7t\2\2\u018c\u018d\7k\2\2\u018d\u018e\7p\2\2\u018e")
        buf.write("\u018f\7v\2\2\u018fj\3\2\2\2\u0190\u0191\7r\2\2\u0191")
        buf.write("\u0192\7t\2\2\u0192\u0193\7k\2\2\u0193\u0194\7p\2\2\u0194")
        buf.write("\u0195\7v\2\2\u0195\u0196\7N\2\2\u0196\u0197\7p\2\2\u0197")
        buf.write("l\3\2\2\2\u0198\u0199\7t\2\2\u0199\u019a\7g\2\2\u019a")
        buf.write("\u019b\7c\2\2\u019b\u019c\7f\2\2\u019cn\3\2\2\2\u019d")
        buf.write("\u01a1\7$\2\2\u019e\u01a0\5q9\2\u019f\u019e\3\2\2\2\u01a0")
        buf.write("\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2")
        buf.write("\u01a2\u01a4\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a5\7")
        buf.write("$\2\2\u01a5\u01a6\b8\3\2\u01a6p\3\2\2\2\u01a7\u01ad\n")
        buf.write("\t\2\2\u01a8\u01a9\7)\2\2\u01a9\u01ad\7$\2\2\u01aa\u01ab")
        buf.write("\7^\2\2\u01ab\u01ad\t\n\2\2\u01ac\u01a7\3\2\2\2\u01ac")
        buf.write("\u01a8\3\2\2\2\u01ac\u01aa\3\2\2\2\u01adr\3\2\2\2\u01ae")
        buf.write("\u01af\t\13\2\2\u01aft\3\2\2\2\u01b0\u01b2\t\f\2\2\u01b1")
        buf.write("\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b1\3\2\2\2")
        buf.write("\u01b3\u01b4\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b6\b")
        buf.write(";\2\2\u01b6v\3\2\2\2\u01b7\u01b8\13\2\2\2\u01b8\u01b9")
        buf.write("\b<\4\2\u01b9x\3\2\2\2\u01ba\u01be\7$\2\2\u01bb\u01bd")
        buf.write("\5q9\2\u01bc\u01bb\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc")
        buf.write("\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0")
        buf.write("\u01be\3\2\2\2\u01c1\u01c3\t\r\2\2\u01c2\u01c1\3\2\2\2")
        buf.write("\u01c3\u01c4\3\2\2\2\u01c4\u01c5\b=\5\2\u01c5z\3\2\2\2")
        buf.write("\u01c6\u01ca\7$\2\2\u01c7\u01c9\5q9\2\u01c8\u01c7\3\2")
        buf.write("\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb")
        buf.write("\3\2\2\2\u01cb\u01d1\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd")
        buf.write("\u01ce\7^\2\2\u01ce\u01d2\n\n\2\2\u01cf\u01d0\7)\2\2\u01d0")
        buf.write("\u01d2\n\16\2\2\u01d1\u01cd\3\2\2\2\u01d1\u01cf\3\2\2")
        buf.write("\2\u01d2\u01d3\3\2\2\2\u01d3\u01d4\b>\6\2\u01d4|\3\2\2")
        buf.write("\2\u01d5\u01d6\7%\2\2\u01d6\u01d7\7%\2\2\u01d7\u01db\3")
        buf.write("\2\2\2\u01d8\u01da\13\2\2\2\u01d9\u01d8\3\2\2\2\u01da")
        buf.write("\u01dd\3\2\2\2\u01db\u01dc\3\2\2\2\u01db\u01d9\3\2\2\2")
        buf.write("\u01dc\u01de\3\2\2\2\u01dd\u01db\3\2\2\2\u01de\u01df\b")
        buf.write("?\7\2\u01df~\3\2\2\2\31\2\u00ba\u00c4\u00c7\u00cc\u00d2")
        buf.write("\u00d7\u00dc\u00e0\u00ef\u00f1\u00f5\u00f7\u0103\u0109")
        buf.write("\u01a1\u01ac\u01b3\u01be\u01c2\u01ca\u01d1\u01db\b\b\2")
        buf.write("\2\38\2\3<\3\3=\4\3>\5\3?\6")
        return buf.getvalue()


class CSELLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    COMMENT = 16
    NUMBER = 17
    BOOLEAN = 18
    CON_IDENTIFIERS = 19
    VAR_IDENTIFIERS = 20
    RELATION_OP = 21
    LOGIC_BINARY_OP = 22
    PLUS_OP = 23
    MINUS_OP = 24
    MULTIPLYING_OP = 25
    LOGICAL_UNARY_OP = 26
    PLUS_OP_STR = 27
    RELATION_OP_STR = 28
    BREAK = 29
    CONTINUE = 30
    IF = 31
    ELIF = 32
    ELSE = 33
    WHILE = 34
    FOR = 35
    OF = 36
    IN = 37
    CALL = 38
    RETURN = 39
    FUNCTION = 40
    LET = 41
    CONSTANT = 42
    STR2NUM = 43
    NUM2STR = 44
    STR2BOOL = 45
    BOOL2STR = 46
    PRINT = 47
    PRINTLN = 48
    READ = 49
    STRINGLIT = 50
    SEP = 51
    WS = 52
    ERROR_CHAR = 53
    UNCLOSE_STRING = 54
    ILLEGAL_ESCAPE = 55
    UNTERMINATED_COMMENT = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "','", "':'", "'='", "'['", "']'", "'('", "')'", "'{'", 
            "'}'", "'Number'", "'Boolean'", "'Array'", "'JSON'", "'String'", 
            "'+'", "'-'", "'!'", "'+.'", "'==.'", "'Break'", "'Continue'", 
            "'If'", "'Elif'", "'Else'", "'While'", "'For'", "'Of'", "'In'", 
            "'Call'", "'Return'", "'Function'", "'Let'", "'Constant'", "'str2num'", 
            "'num2str'", "'str2bool'", "'bool2str'", "'print'", "'printLn'", 
            "'read'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "NUMBER", "BOOLEAN", "CON_IDENTIFIERS", "VAR_IDENTIFIERS", 
            "RELATION_OP", "LOGIC_BINARY_OP", "PLUS_OP", "MINUS_OP", "MULTIPLYING_OP", 
            "LOGICAL_UNARY_OP", "PLUS_OP_STR", "RELATION_OP_STR", "BREAK", 
            "CONTINUE", "IF", "ELIF", "ELSE", "WHILE", "FOR", "OF", "IN", 
            "CALL", "RETURN", "FUNCTION", "LET", "CONSTANT", "STR2NUM", 
            "NUM2STR", "STR2BOOL", "BOOL2STR", "PRINT", "PRINTLN", "READ", 
            "STRINGLIT", "SEP", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "COMMENT", "NUMBER", "INT_PART", "DECIMAL_PART", 
                  "EXP_PART", "BOOLEAN", "TRUE", "FALSE", "CON_IDENTIFIERS", 
                  "VAR_IDENTIFIERS", "RELATION_OP", "LOGIC_BINARY_OP", "PLUS_OP", 
                  "MINUS_OP", "MULTIPLYING_OP", "LOGICAL_UNARY_OP", "PLUS_OP_STR", 
                  "RELATION_OP_STR", "BREAK", "CONTINUE", "IF", "ELIF", 
                  "ELSE", "WHILE", "FOR", "OF", "IN", "CALL", "RETURN", 
                  "FUNCTION", "LET", "CONSTANT", "STR2NUM", "NUM2STR", "STR2BOOL", 
                  "BOOL2STR", "PRINT", "PRINTLN", "READ", "STRINGLIT", "CHAR_STRING", 
                  "SEP", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT" ]

    grammarFileName = "CSEL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[54] = self.STRINGLIT_action 
            actions[58] = self.ERROR_CHAR_action 
            actions[59] = self.UNCLOSE_STRING_action 
            actions[60] = self.ILLEGAL_ESCAPE_action 
            actions[61] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            y = str(self.text)
            self.text = y[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise ErrorToken(self.text)
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		text = str(self.text)
            		if (text[-1] is '\r') or (text[-1] is '\n') or (text[-1] is '\b') or (text[-1] is '\t') or (text[-1] is '\f'):
            			raise UncloseString(text[1:-1])
            		else:
            			raise UncloseString(text[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    raise IllegalEscape(str(self.text)[1:])
                
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    raise UnterminatedComment()
                
     


