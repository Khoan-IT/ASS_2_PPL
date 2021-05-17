import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("Let a[10];", "Let,a,[,10,],;,<EOF>", 101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Let", "Let,<EOF>", 102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn", "ab,Error Token ?", 103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Let x;", "Let,x,;,<EOF>", 104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  """, """Illegal Escape In String: abc\\h""", 105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  """, """Unclosed String: abc def  """, 106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  """, """ab'"c\\n def,<EOF>""", 107))

    def test_wrong_token_1(self):
        self.assertTrue(TestLexer.checkLexeme("abs?asd", """abs,Error Token ?""", 108))

    def test_wrong_token_2(self):
        self.assertTrue(TestLexer.checkLexeme("abs`asd", """abs,Error Token `""", 109))

    def test_cho_vui(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "aa\\n" """, """aa\\n,<EOF>""", 110))

    def test_cho_vui_1(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "aa\n" """, """Unclosed String: aa""", 111))

    def test_cho_vui_12(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc""", """Unclosed String: abc""", 112))

    def test_cho_vui_13(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\nabc" """, """Unclosed String: abc""", 113))

    def test_float_14(self):
        self.assertTrue(TestLexer.checkLexeme("""1.22""", """1.22,<EOF>""", 114))

    def test_float_15(self):
        self.assertTrue(TestLexer.checkLexeme("""22.""", """22.,<EOF>""", 115))

    def test_float_16(self):
        self.assertTrue(TestLexer.checkLexeme("""1.e2""", """1.e2,<EOF>""", 116))

    def test_float_17(self):
        self.assertTrue(TestLexer.checkLexeme("""1.e+2""", """1.e+2,<EOF>""", 117))

    def test_float_18(self):
        self.assertTrue(TestLexer.checkLexeme("""1.e-2""", """1.e-2,<EOF>""", 118))

    def test_float_19(self):
        self.assertTrue(TestLexer.checkLexeme("""1.e""", """1.,e,<EOF>""", 119))

    def test_comment_20(self):
        self.assertTrue(TestLexer.checkLexeme(""" ##COMMENT## """, """<EOF>""", 120))

    def test_comment_21(self):
        self.assertTrue(TestLexer.checkLexeme(""" ##COMMENT """, """Unterminated Comment""", 121))

    def test_comment_22(self):
        self.assertTrue(TestLexer.checkLexeme(""" ##### """, """Error Token #""", 122))

    def test_comment_23(self):
        self.assertTrue(TestLexer.checkLexeme(""" ###### """, """Unterminated Comment""", 123))

    def test_comment_24(self):
        self.assertTrue(TestLexer.checkLexeme(""" ######## """, """<EOF>""", 124))

    def test_comment_25(self):
        self.assertTrue(TestLexer.checkLexeme(""" ##"aStrng"/an\\rd/d" ## """, """<EOF>""", 125))

    def test_comment_26(self):
        self.assertTrue(TestLexer.checkLexeme(""" ####dadada#### """, """dadada,<EOF>""", 126))

    def test_comment_27(self):
        input = r""" 
        ## comment
        #a
        #b
        ## """
        self.assertTrue(TestLexer.checkLexeme(input, """<EOF>""", 127))

    def test_comment_28(self):
        input = r""" 
        ## comment
        #a.\nass
        #b.\t
        ## """
        self.assertTrue(TestLexer.checkLexeme(input, """<EOF>""", 128))

    def test_comment_29(self):
        input = r""" 
        ## comment
        #a
        #b
        """
        self.assertTrue(TestLexer.checkLexeme(input, """Unterminated Comment""", 129))

    def test_comment_30(self):
        input = r""" 
        ## comment
        #a
        #b
        ###
        """
        self.assertTrue(TestLexer.checkLexeme(input, """Error Token #""", 130))

    def test_comment_31(self):
        input = r""" 
        ## comment
        #a
        ##b
        ##
        """
        self.assertTrue(TestLexer.checkLexeme(input, """b,Unterminated Comment""", 131))

    def test_id_32(self):
        self.assertTrue(TestLexer.checkLexeme(""" testne """, """testne,<EOF>""", 132))

    def test_id_33(self):
        self.assertTrue(TestLexer.checkLexeme(""" BeNa """, """Error Token B""", 133))

    def test_id_34(self):
        self.assertTrue(TestLexer.checkLexeme(""" $asd23 """, """$asd23,<EOF>""", 134))

    def test_id_35(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0testne """, """0,testne,<EOF>""", 135))

    def test_id_36(self):
        self.assertTrue(TestLexer.checkLexeme(""" _khoanne """, """Error Token _""", 136))

    def test_id_37(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0.11$khoanne0.11 """, """0.11,$khoanne0,.,11,<EOF>""", 137))

    def test_id_38(self):
        self.assertTrue(TestLexer.checkLexeme(""" khoanne12NNa_ """, """khoanne12NNa_,<EOF>""", 138))

    def test_id_39(self):
        self.assertTrue(TestLexer.checkLexeme(""" khoanne12NNa_ beNa """, """khoanne12NNa_,beNa,<EOF>""", 139))

    def test_id_40(self):
        self.assertTrue(TestLexer.checkLexeme(""" khoanne12NNa_ _ena """, """khoanne12NNa_,Error Token _""", 140))

    def test_id_41(self):
        self.assertTrue(TestLexer.checkLexeme(""" khoanne12NNa- Bena """, """khoanne12NNa,-,Error Token B""", 141))

    def test_id_42(self):
        self.assertTrue(
            TestLexer.checkLexeme(""" khoanne12NNa_Bena___0_123 """, """khoanne12NNa_Bena___0_123,<EOF>""", 142))

    def test_kw(self):
        self.assertTrue(
            TestLexer.checkLexeme(""" While For Continue Break """, """While,For,Continue,Break,<EOF>""", 143))

    def test_kw_44(self):
        self.assertTrue(TestLexer.checkLexeme(""" +-=.<. """, """+,-,=,.,<,.,<EOF>""", 144))

    def test_kw_45(self):
        self.assertTrue(TestLexer.checkLexeme(""" Does """, """Error Token D""", 145))

    def test_kw_46(self):
        self.assertTrue(TestLexer.checkLexeme("""While IFs While""", """While,Error Token I""", 146))

    def test_int_47(self):
        self.assertTrue(TestLexer.checkLexeme("""1222""", """1222,<EOF>""", 147))

    def test_int_48(self):
        self.assertTrue(TestLexer.checkLexeme("""-1222""", """-,1222,<EOF>""", 148))

    def test_int_49(self):
        self.assertTrue(TestLexer.checkLexeme("""01222""", """01222,<EOF>""", 149))

    def test_int_50(self):
        self.assertTrue(TestLexer.checkLexeme("""0""", """0,<EOF>""", 150))

    def test_kw_51(self):
        self.assertTrue(TestLexer.checkLexeme(""" (+-=.<.) """, """(,+,-,=,.,<,.,),<EOF>""", 151))

    def test_int_52(self):
        self.assertTrue(TestLexer.checkLexeme("""!===""", """!=,==,<EOF>""", 152))

    def test_id_53(self):
        self.assertTrue(TestLexer.checkLexeme("""$a$abd12$$""", """$a,$abd12,Error Token $""", 153))

    def test_int_54(self):
        self.assertTrue(TestLexer.checkLexeme(""" --12.e123""", """-,-,12.e123,<EOF>""", 154))

    def test_int_55(self):
        self.assertTrue(TestLexer.checkLexeme(""".1.e""", """.,1.,e,<EOF>""", 155))

    def test_op_56(self):
        self.assertTrue(TestLexer.checkLexeme(""" <==""", """<=,=,<EOF>""", 156))

    def test_type_57(self):
        self.assertTrue(TestLexer.checkLexeme(""" JSON String$12""", """JSON,String,$12,<EOF>""", 157))

    def test_id_58(self):
        self.assertTrue(TestLexer.checkLexeme(""" $123_11-khoan""", """$123_11,-,khoan,<EOF>""", 158))

    def test_int_59(self):
        self.assertTrue(TestLexer.checkLexeme(""" 1+0.1E-0.1""", """1,+,0.1E-0,.,1,<EOF>""", 159))

    def test_int_60(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0oAA1""", """0,oAA1,<EOF>""", 160))

    def test_int_61(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0B""", """0,Error Token B""", 161))

    def test_string_62(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello world ! \\n\\t" """, """hello world ! \\n\\t,<EOF>""", 162))

    def test_string_63(self):
        self.assertTrue(TestLexer.checkLexeme(""" "khoan '"'" abc" """, """khoan '"'" abc,<EOF>""", 163))

    def test_float_64(self):
        self.assertTrue(TestLexer.checkLexeme("""0.^022""", """0.,Error Token ^""", 164))

    def test_float_65(self):
        self.assertTrue(TestLexer.checkLexeme("""0.005""", """0.005,<EOF>""", 165))

    def test_float_66(self):
        self.assertTrue(TestLexer.checkLexeme("""00.005""", """00.005,<EOF>""", 166))

    def test_float_67(self):
        self.assertTrue(TestLexer.checkLexeme("""-00.005""", """-,00.005,<EOF>""", 167))

    def test_float_68(self):
        self.assertTrue(TestLexer.checkLexeme("""11.005""", """11.005,<EOF>""", 168))

    def test_float_69(self):
        self.assertTrue(TestLexer.checkLexeme("""1.""", """1.,<EOF>""", 169))

    def test_float_70(self):
        self.assertTrue(TestLexer.checkLexeme("""1.e""", """1.,e,<EOF>""", 170))

    def test_float_71(self):
        self.assertTrue(TestLexer.checkLexeme("""1.E3""", """1.E3,<EOF>""", 171))

    def test_float_72(self):
        self.assertTrue(TestLexer.checkLexeme("""1.E-3""", """1.E-3,<EOF>""", 172))

    def test_float_73(self):
        self.assertTrue(TestLexer.checkLexeme("""1.E+3""", """1.E+3,<EOF>""", 173))

    def test_float_74(self):
        self.assertTrue(TestLexer.checkLexeme("""1.13E3""", """1.13E3,<EOF>""", 174))

    def test_float_75(self):
        self.assertTrue(TestLexer.checkLexeme("""1.13E+344""", """1.13E+344,<EOF>""", 175))

    def test_float_76(self):
        self.assertTrue(TestLexer.checkLexeme("""1.13E-344""", """1.13E-344,<EOF>""", 176))

    def test_float_77(self):
        self.assertTrue(TestLexer.checkLexeme("""-2.E+22""", """-,2.E+22,<EOF>""", 177))

    def test_float_78(self):
        self.assertTrue(TestLexer.checkLexeme("""-2.E-22""", """-,2.E-22,<EOF>""", 178))

    def test_float_79(self):
        self.assertTrue(TestLexer.checkLexeme("""-2.Ee22""", """-,2.,Error Token E""", 179))

    def test_float_80(self):
        self.assertTrue(TestLexer.checkLexeme("""-2Pad0x.^2""", """-,2,Error Token P""", 180))

    def test_float_81(self):
        self.assertTrue(TestLexer.checkLexeme("""True False""", """True,False,<EOF>""", 181))

    def test_float_82(self):
        self.assertTrue(TestLexer.checkLexeme("""TRUE""", """Error Token T""", 182))

    def test_float_83(self):
        self.assertTrue(TestLexer.checkLexeme("""FALSE""", """Error Token F""", 183))

    def test_float_84(self):
        self.assertTrue(TestLexer.checkLexeme("""tRue""", """tRue,<EOF>""", 184))

    def test_string_85(self):
        self.assertTrue(TestLexer.checkLexeme(""" "He asked me: 'Where is John?'"" """,
                                              """Illegal Escape In String: He asked me: 'W""", 185))

    def test_string_86(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hello \n" """, """Unclosed String: Hello """, 186))

    def test_string_87(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hello \\n" """, """Hello \\n,<EOF>""", 187))

    def test_string_88(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hello""", """Unclosed String: Hello""", 188))

    def test_string_89(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hello \r" """, """Unclosed String: Hello """, 189))

    def test_string_90(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hello \'k" """, """Illegal Escape In String: Hello 'k""", 190))

    def test_string_91(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hello \\a" """, """Illegal Escape In String: Hello \\a""", 191))

    def test_string_92(self):
        self.assertTrue(
            TestLexer.checkLexeme(""" "Dai. Hoc. Bach' Khoa" """, """Illegal Escape In String: Dai. Hoc. Bach' """,
                                  192))

    def test_string_93(self):
        self.assertTrue(
            TestLexer.checkLexeme(""" "Thanh Pho'" Ho_ Chi???Minh" """, """Thanh Pho'" Ho_ Chi???Minh,<EOF>""", 193))

    def test_string_94(self):
        self.assertTrue(
            TestLexer.checkLexeme(""" "Really \\t DON\'T know" """, """Illegal Escape In String: Really \\t DON\'T""",
                                  194))

    def test_string_95(self):
        self.assertTrue(TestLexer.checkLexeme(""" {{}{}} """, """{,{,},{,},},<EOF>""", 195))

    def test_string_96(self):
        self.assertTrue(TestLexer.checkLexeme(""" a ||| b  """, """a,||,Error Token |""", 196))

    def test_string_97(self):
        self.assertTrue(TestLexer.checkLexeme(""" a \\\\\\ """, """a,Error Token \\""", 197))

    def test_string_98(self):
        self.assertTrue(TestLexer.checkLexeme(""" "c0' """, """Illegal Escape In String: c0' """, 198))

    def test_string_99(self):
        self.assertTrue(TestLexer.checkLexeme("""++.-.- """, """+,+.,-,.,-,<EOF>""", 199))

    def test_string_100(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hello" "Myname" """, """Hello,Myname,<EOF>""", 200))


