# Generated from main/csel/parser/CSEL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u01d5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\7\f")
        buf.write("\u0090\n\f\f\f\16\f\u0093\13\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u00b6\n\r\3\16\3\16\5\16\u00ba\n\16\3\16\5\16\u00bd")
        buf.write("\n\16\3\17\6\17\u00c0\n\17\r\17\16\17\u00c1\3\20\3\20")
        buf.write("\7\20\u00c6\n\20\f\20\16\20\u00c9\13\20\3\21\3\21\5\21")
        buf.write("\u00cd\n\21\3\21\6\21\u00d0\n\21\r\21\16\21\u00d1\3\22")
        buf.write("\3\22\5\22\u00d6\n\22\3\23\3\23\3\23\3\23\3\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\25\3\25\6\25\u00e5\n\25\r\25")
        buf.write("\16\25\u00e6\3\26\3\26\7\26\u00eb\n\26\f\26\16\26\u00ee")
        buf.write("\13\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5")
        buf.write("\27\u00f9\n\27\3\30\3\30\3\30\3\30\5\30\u00ff\n\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*")
        buf.write("\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\7\64\u0195\n\64\f\64\16\64\u0198\13\64\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\65\3\65\5\65\u01a2\n\65\3")
        buf.write("\66\3\66\3\67\6\67\u01a7\n\67\r\67\16\67\u01a8\3\67\3")
        buf.write("\67\38\38\38\39\39\79\u01b2\n9\f9\169\u01b5\139\39\59")
        buf.write("\u01b8\n9\39\39\3:\3:\7:\u01be\n:\f:\16:\u01c1\13:\3:")
        buf.write("\3:\3:\3:\5:\u01c7\n:\3:\3:\3;\3;\3;\3;\7;\u01cf\n;\f")
        buf.write(";\16;\u01d2\13;\3;\3;\4\u0091\u01d0\2<\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\2\37")
        buf.write("\2!\2#\20%\2\'\2)\21+\22-\23/\24\61\25\63\26\65\27\67")
        buf.write("\309\31;\32=\33?\34A\35C\36E\37G I!K\"M#O$Q%S&U\'W(Y)")
        buf.write("[*]+_,a-c.e/g\60i\2k\61m\62o\63q\64s\65u\66\3\2\17\3\2")
        buf.write("\62;\4\2GGgg\4\2--//\6\2\62;C\\aac|\3\2c|\4\2>>@@\5\2")
        buf.write("\'\',,\61\61\7\2\f\f\17\17$$))^^\t\2))^^ddhhppttvv\n\2")
        buf.write("*+..\60\60<=]]__}}\177\177\5\2\13\f\17\17\"\"\4\3\n\f")
        buf.write("\16\17\3\2$$\2\u01e9\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2#\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2")
        buf.write("q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\3w\3\2\2\2\5y\3\2\2\2")
        buf.write("\7{\3\2\2\2\t}\3\2\2\2\13\177\3\2\2\2\r\u0081\3\2\2\2")
        buf.write("\17\u0083\3\2\2\2\21\u0085\3\2\2\2\23\u0087\3\2\2\2\25")
        buf.write("\u0089\3\2\2\2\27\u008b\3\2\2\2\31\u00b5\3\2\2\2\33\u00b7")
        buf.write("\3\2\2\2\35\u00bf\3\2\2\2\37\u00c3\3\2\2\2!\u00ca\3\2")
        buf.write("\2\2#\u00d5\3\2\2\2%\u00d7\3\2\2\2\'\u00dc\3\2\2\2)\u00e2")
        buf.write("\3\2\2\2+\u00e8\3\2\2\2-\u00f8\3\2\2\2/\u00fe\3\2\2\2")
        buf.write("\61\u0100\3\2\2\2\63\u0102\3\2\2\2\65\u0104\3\2\2\2\67")
        buf.write("\u0106\3\2\2\29\u0108\3\2\2\2;\u010b\3\2\2\2=\u010f\3")
        buf.write("\2\2\2?\u0115\3\2\2\2A\u011e\3\2\2\2C\u0121\3\2\2\2E\u0126")
        buf.write("\3\2\2\2G\u012b\3\2\2\2I\u0131\3\2\2\2K\u0135\3\2\2\2")
        buf.write("M\u0138\3\2\2\2O\u013b\3\2\2\2Q\u0140\3\2\2\2S\u0147\3")
        buf.write("\2\2\2U\u0150\3\2\2\2W\u0154\3\2\2\2Y\u015d\3\2\2\2[\u0165")
        buf.write("\3\2\2\2]\u016d\3\2\2\2_\u0176\3\2\2\2a\u017f\3\2\2\2")
        buf.write("c\u0185\3\2\2\2e\u018d\3\2\2\2g\u0192\3\2\2\2i\u01a1\3")
        buf.write("\2\2\2k\u01a3\3\2\2\2m\u01a6\3\2\2\2o\u01ac\3\2\2\2q\u01af")
        buf.write("\3\2\2\2s\u01bb\3\2\2\2u\u01ca\3\2\2\2wx\7=\2\2x\4\3\2")
        buf.write("\2\2yz\7.\2\2z\6\3\2\2\2{|\7<\2\2|\b\3\2\2\2}~\7?\2\2")
        buf.write("~\n\3\2\2\2\177\u0080\7]\2\2\u0080\f\3\2\2\2\u0081\u0082")
        buf.write("\7_\2\2\u0082\16\3\2\2\2\u0083\u0084\7*\2\2\u0084\20\3")
        buf.write("\2\2\2\u0085\u0086\7+\2\2\u0086\22\3\2\2\2\u0087\u0088")
        buf.write("\7}\2\2\u0088\24\3\2\2\2\u0089\u008a\7\177\2\2\u008a\26")
        buf.write("\3\2\2\2\u008b\u008c\7%\2\2\u008c\u008d\7%\2\2\u008d\u0091")
        buf.write("\3\2\2\2\u008e\u0090\13\2\2\2\u008f\u008e\3\2\2\2\u0090")
        buf.write("\u0093\3\2\2\2\u0091\u0092\3\2\2\2\u0091\u008f\3\2\2\2")
        buf.write("\u0092\u0094\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0095\7")
        buf.write("%\2\2\u0095\u0096\7%\2\2\u0096\u0097\3\2\2\2\u0097\u0098")
        buf.write("\b\f\2\2\u0098\30\3\2\2\2\u0099\u009a\7P\2\2\u009a\u009b")
        buf.write("\7w\2\2\u009b\u009c\7o\2\2\u009c\u009d\7d\2\2\u009d\u009e")
        buf.write("\7g\2\2\u009e\u00b6\7t\2\2\u009f\u00a0\7D\2\2\u00a0\u00a1")
        buf.write("\7q\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3\7n\2\2\u00a3\u00a4")
        buf.write("\7g\2\2\u00a4\u00a5\7c\2\2\u00a5\u00b6\7p\2\2\u00a6\u00a7")
        buf.write("\7C\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa")
        buf.write("\7c\2\2\u00aa\u00b6\7{\2\2\u00ab\u00ac\7L\2\2\u00ac\u00ad")
        buf.write("\7U\2\2\u00ad\u00ae\7Q\2\2\u00ae\u00b6\7P\2\2\u00af\u00b0")
        buf.write("\7U\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b2\7t\2\2\u00b2\u00b3")
        buf.write("\7k\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b6\7i\2\2\u00b5\u0099")
        buf.write("\3\2\2\2\u00b5\u009f\3\2\2\2\u00b5\u00a6\3\2\2\2\u00b5")
        buf.write("\u00ab\3\2\2\2\u00b5\u00af\3\2\2\2\u00b6\32\3\2\2\2\u00b7")
        buf.write("\u00b9\5\35\17\2\u00b8\u00ba\5\37\20\2\u00b9\u00b8\3\2")
        buf.write("\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bc\3\2\2\2\u00bb\u00bd")
        buf.write("\5!\21\2\u00bc\u00bb\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("\34\3\2\2\2\u00be\u00c0\t\2\2\2\u00bf\u00be\3\2\2\2\u00c0")
        buf.write("\u00c1\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2")
        buf.write("\u00c2\36\3\2\2\2\u00c3\u00c7\7\60\2\2\u00c4\u00c6\t\2")
        buf.write("\2\2\u00c5\u00c4\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5")
        buf.write("\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8 \3\2\2\2\u00c9\u00c7")
        buf.write("\3\2\2\2\u00ca\u00cc\t\3\2\2\u00cb\u00cd\t\4\2\2\u00cc")
        buf.write("\u00cb\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00cf\3\2\2\2")
        buf.write("\u00ce\u00d0\t\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\u00d1\3")
        buf.write("\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\"")
        buf.write("\3\2\2\2\u00d3\u00d6\5%\23\2\u00d4\u00d6\5\'\24\2\u00d5")
        buf.write("\u00d3\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6$\3\2\2\2\u00d7")
        buf.write("\u00d8\7V\2\2\u00d8\u00d9\7t\2\2\u00d9\u00da\7w\2\2\u00da")
        buf.write("\u00db\7g\2\2\u00db&\3\2\2\2\u00dc\u00dd\7H\2\2\u00dd")
        buf.write("\u00de\7c\2\2\u00de\u00df\7n\2\2\u00df\u00e0\7u\2\2\u00e0")
        buf.write("\u00e1\7g\2\2\u00e1(\3\2\2\2\u00e2\u00e4\7&\2\2\u00e3")
        buf.write("\u00e5\t\5\2\2\u00e4\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2")
        buf.write("\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7*\3\2\2")
        buf.write("\2\u00e8\u00ec\t\6\2\2\u00e9\u00eb\t\5\2\2\u00ea\u00e9")
        buf.write("\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec")
        buf.write("\u00ed\3\2\2\2\u00ed,\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef")
        buf.write("\u00f0\7?\2\2\u00f0\u00f9\7?\2\2\u00f1\u00f2\7#\2\2\u00f2")
        buf.write("\u00f9\7?\2\2\u00f3\u00f9\t\7\2\2\u00f4\u00f5\7>\2\2\u00f5")
        buf.write("\u00f9\7?\2\2\u00f6\u00f7\7@\2\2\u00f7\u00f9\7?\2\2\u00f8")
        buf.write("\u00ef\3\2\2\2\u00f8\u00f1\3\2\2\2\u00f8\u00f3\3\2\2\2")
        buf.write("\u00f8\u00f4\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f9.\3\2\2")
        buf.write("\2\u00fa\u00fb\7(\2\2\u00fb\u00ff\7(\2\2\u00fc\u00fd\7")
        buf.write("~\2\2\u00fd\u00ff\7~\2\2\u00fe\u00fa\3\2\2\2\u00fe\u00fc")
        buf.write("\3\2\2\2\u00ff\60\3\2\2\2\u0100\u0101\7-\2\2\u0101\62")
        buf.write("\3\2\2\2\u0102\u0103\7/\2\2\u0103\64\3\2\2\2\u0104\u0105")
        buf.write("\t\b\2\2\u0105\66\3\2\2\2\u0106\u0107\7#\2\2\u01078\3")
        buf.write("\2\2\2\u0108\u0109\7-\2\2\u0109\u010a\7\60\2\2\u010a:")
        buf.write("\3\2\2\2\u010b\u010c\7?\2\2\u010c\u010d\7?\2\2\u010d\u010e")
        buf.write("\7\60\2\2\u010e<\3\2\2\2\u010f\u0110\7D\2\2\u0110\u0111")
        buf.write("\7t\2\2\u0111\u0112\7g\2\2\u0112\u0113\7c\2\2\u0113\u0114")
        buf.write("\7m\2\2\u0114>\3\2\2\2\u0115\u0116\7E\2\2\u0116\u0117")
        buf.write("\7q\2\2\u0117\u0118\7p\2\2\u0118\u0119\7v\2\2\u0119\u011a")
        buf.write("\7k\2\2\u011a\u011b\7p\2\2\u011b\u011c\7w\2\2\u011c\u011d")
        buf.write("\7g\2\2\u011d@\3\2\2\2\u011e\u011f\7K\2\2\u011f\u0120")
        buf.write("\7h\2\2\u0120B\3\2\2\2\u0121\u0122\7G\2\2\u0122\u0123")
        buf.write("\7n\2\2\u0123\u0124\7k\2\2\u0124\u0125\7h\2\2\u0125D\3")
        buf.write("\2\2\2\u0126\u0127\7G\2\2\u0127\u0128\7n\2\2\u0128\u0129")
        buf.write("\7u\2\2\u0129\u012a\7g\2\2\u012aF\3\2\2\2\u012b\u012c")
        buf.write("\7Y\2\2\u012c\u012d\7j\2\2\u012d\u012e\7k\2\2\u012e\u012f")
        buf.write("\7n\2\2\u012f\u0130\7g\2\2\u0130H\3\2\2\2\u0131\u0132")
        buf.write("\7H\2\2\u0132\u0133\7q\2\2\u0133\u0134\7t\2\2\u0134J\3")
        buf.write("\2\2\2\u0135\u0136\7Q\2\2\u0136\u0137\7h\2\2\u0137L\3")
        buf.write("\2\2\2\u0138\u0139\7K\2\2\u0139\u013a\7p\2\2\u013aN\3")
        buf.write("\2\2\2\u013b\u013c\7E\2\2\u013c\u013d\7c\2\2\u013d\u013e")
        buf.write("\7n\2\2\u013e\u013f\7n\2\2\u013fP\3\2\2\2\u0140\u0141")
        buf.write("\7T\2\2\u0141\u0142\7g\2\2\u0142\u0143\7v\2\2\u0143\u0144")
        buf.write("\7w\2\2\u0144\u0145\7t\2\2\u0145\u0146\7p\2\2\u0146R\3")
        buf.write("\2\2\2\u0147\u0148\7H\2\2\u0148\u0149\7w\2\2\u0149\u014a")
        buf.write("\7p\2\2\u014a\u014b\7e\2\2\u014b\u014c\7v\2\2\u014c\u014d")
        buf.write("\7k\2\2\u014d\u014e\7q\2\2\u014e\u014f\7p\2\2\u014fT\3")
        buf.write("\2\2\2\u0150\u0151\7N\2\2\u0151\u0152\7g\2\2\u0152\u0153")
        buf.write("\7v\2\2\u0153V\3\2\2\2\u0154\u0155\7E\2\2\u0155\u0156")
        buf.write("\7q\2\2\u0156\u0157\7p\2\2\u0157\u0158\7u\2\2\u0158\u0159")
        buf.write("\7v\2\2\u0159\u015a\7c\2\2\u015a\u015b\7p\2\2\u015b\u015c")
        buf.write("\7v\2\2\u015cX\3\2\2\2\u015d\u015e\7u\2\2\u015e\u015f")
        buf.write("\7v\2\2\u015f\u0160\7t\2\2\u0160\u0161\7\64\2\2\u0161")
        buf.write("\u0162\7p\2\2\u0162\u0163\7w\2\2\u0163\u0164\7o\2\2\u0164")
        buf.write("Z\3\2\2\2\u0165\u0166\7p\2\2\u0166\u0167\7w\2\2\u0167")
        buf.write("\u0168\7o\2\2\u0168\u0169\7\64\2\2\u0169\u016a\7u\2\2")
        buf.write("\u016a\u016b\7v\2\2\u016b\u016c\7t\2\2\u016c\\\3\2\2\2")
        buf.write("\u016d\u016e\7u\2\2\u016e\u016f\7v\2\2\u016f\u0170\7t")
        buf.write("\2\2\u0170\u0171\7\64\2\2\u0171\u0172\7d\2\2\u0172\u0173")
        buf.write("\7q\2\2\u0173\u0174\7q\2\2\u0174\u0175\7n\2\2\u0175^\3")
        buf.write("\2\2\2\u0176\u0177\7d\2\2\u0177\u0178\7q\2\2\u0178\u0179")
        buf.write("\7q\2\2\u0179\u017a\7n\2\2\u017a\u017b\7\64\2\2\u017b")
        buf.write("\u017c\7u\2\2\u017c\u017d\7v\2\2\u017d\u017e\7t\2\2\u017e")
        buf.write("`\3\2\2\2\u017f\u0180\7r\2\2\u0180\u0181\7t\2\2\u0181")
        buf.write("\u0182\7k\2\2\u0182\u0183\7p\2\2\u0183\u0184\7v\2\2\u0184")
        buf.write("b\3\2\2\2\u0185\u0186\7r\2\2\u0186\u0187\7t\2\2\u0187")
        buf.write("\u0188\7k\2\2\u0188\u0189\7p\2\2\u0189\u018a\7v\2\2\u018a")
        buf.write("\u018b\7N\2\2\u018b\u018c\7p\2\2\u018cd\3\2\2\2\u018d")
        buf.write("\u018e\7t\2\2\u018e\u018f\7g\2\2\u018f\u0190\7c\2\2\u0190")
        buf.write("\u0191\7f\2\2\u0191f\3\2\2\2\u0192\u0196\7$\2\2\u0193")
        buf.write("\u0195\5i\65\2\u0194\u0193\3\2\2\2\u0195\u0198\3\2\2\2")
        buf.write("\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0199\3")
        buf.write("\2\2\2\u0198\u0196\3\2\2\2\u0199\u019a\7$\2\2\u019a\u019b")
        buf.write("\b\64\3\2\u019bh\3\2\2\2\u019c\u01a2\n\t\2\2\u019d\u019e")
        buf.write("\7)\2\2\u019e\u01a2\7$\2\2\u019f\u01a0\7^\2\2\u01a0\u01a2")
        buf.write("\t\n\2\2\u01a1\u019c\3\2\2\2\u01a1\u019d\3\2\2\2\u01a1")
        buf.write("\u019f\3\2\2\2\u01a2j\3\2\2\2\u01a3\u01a4\t\13\2\2\u01a4")
        buf.write("l\3\2\2\2\u01a5\u01a7\t\f\2\2\u01a6\u01a5\3\2\2\2\u01a7")
        buf.write("\u01a8\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2")
        buf.write("\u01a9\u01aa\3\2\2\2\u01aa\u01ab\b\67\2\2\u01abn\3\2\2")
        buf.write("\2\u01ac\u01ad\13\2\2\2\u01ad\u01ae\b8\4\2\u01aep\3\2")
        buf.write("\2\2\u01af\u01b3\7$\2\2\u01b0\u01b2\5i\65\2\u01b1\u01b0")
        buf.write("\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3")
        buf.write("\u01b4\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2")
        buf.write("\u01b6\u01b8\t\r\2\2\u01b7\u01b6\3\2\2\2\u01b8\u01b9\3")
        buf.write("\2\2\2\u01b9\u01ba\b9\5\2\u01bar\3\2\2\2\u01bb\u01bf\7")
        buf.write("$\2\2\u01bc\u01be\5i\65\2\u01bd\u01bc\3\2\2\2\u01be\u01c1")
        buf.write("\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0")
        buf.write("\u01c6\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c3\7^\2\2")
        buf.write("\u01c3\u01c7\n\n\2\2\u01c4\u01c5\7)\2\2\u01c5\u01c7\n")
        buf.write("\16\2\2\u01c6\u01c2\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7")
        buf.write("\u01c8\3\2\2\2\u01c8\u01c9\b:\6\2\u01c9t\3\2\2\2\u01ca")
        buf.write("\u01cb\7%\2\2\u01cb\u01cc\7%\2\2\u01cc\u01d0\3\2\2\2\u01cd")
        buf.write("\u01cf\13\2\2\2\u01ce\u01cd\3\2\2\2\u01cf\u01d2\3\2\2")
        buf.write("\2\u01d0\u01d1\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d1\u01d3")
        buf.write("\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d4\b;\7\2\u01d4")
        buf.write("v\3\2\2\2\32\2\u0091\u00b5\u00b9\u00bc\u00c1\u00c7\u00cc")
        buf.write("\u00d1\u00d5\u00e4\u00e6\u00ea\u00ec\u00f8\u00fe\u0196")
        buf.write("\u01a1\u01a8\u01b3\u01b7\u01bf\u01c6\u01d0\b\b\2\2\3\64")
        buf.write("\2\38\3\39\4\3:\5\3;\6")
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
    COMMENT = 11
    LIT_TYPE = 12
    NUMBER = 13
    BOOLEAN = 14
    CON_IDENTIFIERS = 15
    VAR_IDENTIFIERS = 16
    RELATION_OP = 17
    LOGIC_BINARY_OP = 18
    PLUS_OP = 19
    MINUS_OP = 20
    MULTIPLYING_OP = 21
    LOGICAL_UNARY_OP = 22
    PLUS_OP_STR = 23
    RELATION_OP_STR = 24
    BREAK = 25
    CONTINUE = 26
    IF = 27
    ELIF = 28
    ELSE = 29
    WHILE = 30
    FOR = 31
    OF = 32
    IN = 33
    CALL = 34
    RETURN = 35
    FUNCTION = 36
    LET = 37
    CONSTANT = 38
    STR2NUM = 39
    NUM2STR = 40
    STR2BOOL = 41
    BOOL2STR = 42
    PRINT = 43
    PRINTLN = 44
    READ = 45
    STRINGLIT = 46
    SEP = 47
    WS = 48
    ERROR_CHAR = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51
    UNTERMINATED_COMMENT = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "','", "':'", "'='", "'['", "']'", "'('", "')'", "'{'", 
            "'}'", "'+'", "'-'", "'!'", "'+.'", "'==.'", "'Break'", "'Continue'", 
            "'If'", "'Elif'", "'Else'", "'While'", "'For'", "'Of'", "'In'", 
            "'Call'", "'Return'", "'Function'", "'Let'", "'Constant'", "'str2num'", 
            "'num2str'", "'str2bool'", "'bool2str'", "'print'", "'printLn'", 
            "'read'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "LIT_TYPE", "NUMBER", "BOOLEAN", "CON_IDENTIFIERS", 
            "VAR_IDENTIFIERS", "RELATION_OP", "LOGIC_BINARY_OP", "PLUS_OP", 
            "MINUS_OP", "MULTIPLYING_OP", "LOGICAL_UNARY_OP", "PLUS_OP_STR", 
            "RELATION_OP_STR", "BREAK", "CONTINUE", "IF", "ELIF", "ELSE", 
            "WHILE", "FOR", "OF", "IN", "CALL", "RETURN", "FUNCTION", "LET", 
            "CONSTANT", "STR2NUM", "NUM2STR", "STR2BOOL", "BOOL2STR", "PRINT", 
            "PRINTLN", "READ", "STRINGLIT", "SEP", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "COMMENT", "LIT_TYPE", "NUMBER", 
                  "INT_PART", "DECIMAL_PART", "EXP_PART", "BOOLEAN", "TRUE", 
                  "FALSE", "CON_IDENTIFIERS", "VAR_IDENTIFIERS", "RELATION_OP", 
                  "LOGIC_BINARY_OP", "PLUS_OP", "MINUS_OP", "MULTIPLYING_OP", 
                  "LOGICAL_UNARY_OP", "PLUS_OP_STR", "RELATION_OP_STR", 
                  "BREAK", "CONTINUE", "IF", "ELIF", "ELSE", "WHILE", "FOR", 
                  "OF", "IN", "CALL", "RETURN", "FUNCTION", "LET", "CONSTANT", 
                  "STR2NUM", "NUM2STR", "STR2BOOL", "BOOL2STR", "PRINT", 
                  "PRINTLN", "READ", "STRINGLIT", "CHAR_STRING", "SEP", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
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
            actions[50] = self.STRINGLIT_action 
            actions[54] = self.ERROR_CHAR_action 
            actions[55] = self.UNCLOSE_STRING_action 
            actions[56] = self.ILLEGAL_ESCAPE_action 
            actions[57] = self.UNTERMINATED_COMMENT_action 
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
                
     


