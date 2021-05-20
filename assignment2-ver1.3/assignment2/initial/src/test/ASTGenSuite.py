import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Let x;"""
        expect = Program([VarDecl(Id("x"), [], NoneType(), None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    def test1(self):
        input = """Let x = 1, y;
        Constant $a[2]:JSON = 3, $b[4] = 4;"""
        expect = Program([
            VarDecl(Id("x"),[],NoneType(),NumberLiteral(1.0)),
            VarDecl(Id("y"),[],NoneType(),None),
            ConstDecl(Id("$a"),[NumberLiteral(2.0)],JSONType(),NumberLiteral(3.0)),
            ConstDecl(Id("$b"),[NumberLiteral(4.0)],NoneType(),NumberLiteral(4.0))
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test2(self):
        input = """Let abc[1,2,3] = 212;"""
        expect = Program([
            VarDecl(Id("abc"),[NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0)],NoneType(),NumberLiteral(212.0))
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test3(self):
        input = """Let abc[a,b,c]:Number = 2.12;"""
        expect = Program([
            VarDecl(Id("abc"),[Id('a'),Id('b'),Id('c')],NumberType(),NumberLiteral(2.12))
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test4(self):
        input = r"""
        Function fact(a,b[1,2,3]){
            Let c;
            c = 5;
            Call(writeln,[a[i], "lala", b]);
        }"""
        expect = Program([
            FuncDecl(Id('fact'),
             [
                 VarDecl(Id('a'),[],NoneType(),None),
                 VarDecl(Id('b'),[NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0)],NoneType(),None)
             ],
             [
                 VarDecl(Id('c'),[],NoneType(),None),
                 Assign(Id('c'),NumberLiteral(5.0)),
                 CallStmt(Id('writeln'),
                          [
                              ArrayAccess(Id('a'),[Id('i')]),
                              StringLiteral('lala'),
                              Id('b')
                          ])
             ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test5(self):
        input = r"""
        Let a[1,2]:JSON = [{name:"Khoan",class:15},{age : 20, num:[1,2,3]}];
        """
        expect = Program(
            [
                VarDecl(Id('a'),[NumberLiteral(1.0),NumberLiteral(2.0)],JSONType(),
                            ArrayLiteral([
                                    JSONLiteral([
                                            (Id('name'),StringLiteral('Khoan')),
                                            (Id('class'),NumberLiteral(15.0))
                                        ]),
                                    JSONLiteral(
                                        [
                                            (Id('age'), NumberLiteral(20.0)),
                                            (Id('num'), ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0)]))
                                    ])
                            ])
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test6(self):
        input="""
        Let a:JSON = {name : "Khoan",age : {age:20,class:[1,2]}};
        """
        expect = Program(
            [
                VarDecl(Id("a"),[],JSONType(),JSONLiteral(
                    [
                        (Id("name"),StringLiteral("Khoan")),
                        (Id("age"),JSONLiteral(
                            [
                                (Id("age"),NumberLiteral(20.0)),
                                (Id("class"),ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0)]))
                            ]))
                    ]
                ))
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test7(self):
        input="""
        Let a,b:String = "Duc" +. "Khoan";
        """
        expect = Program(
            [
                VarDecl(Id("a"),[],NoneType(),None),
                VarDecl(Id("b"),[],StringType(),BinaryOp("+.",StringLiteral("Duc"),StringLiteral("Khoan")))
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))
    def test8(self):
        input="""
        Let a:Boolean = (x>0)&&(i<10);
        """
        expect = Program(
            [
                VarDecl(Id("a"),[],BooleanType(),BinaryOp("&&",BinaryOp('>',Id("x"),NumberLiteral(0.0)),BinaryOp("<",Id("i"),NumberLiteral(10.0))))
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test9(self):
        input="""
        Function foo(){
            Let a[2,2]:Number = [[1,2],[3,4]];
            a[0,1] = 10 + z;
        }
        """
        expect = Program(
            [
                FuncDecl(Id("foo"),[],
                    [
                        VarDecl(Id("a"),[NumberLiteral(2.0),NumberLiteral(2.0)],NumberType(),
                                ArrayLiteral(
                                    [
                                        ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0)]),
                                        ArrayLiteral([NumberLiteral(3.0), NumberLiteral(4.0)])
                                    ]
                                )
                                ),
                        Assign(ArrayAccess(Id("a"),[NumberLiteral(0.0),NumberLiteral(1.0)]),BinaryOp("+",NumberLiteral(10.0),Id("z")))
                    ]
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test10(self):
        input="""
        Function foo(){
            Let a:JSON = {name:"Khoan",age:20};
            a{"name"} = "Duc" +. "Khoan";
        }
        """
        expect = Program(
            [
                FuncDecl(Id("foo"),[],
                    [
                        VarDecl(Id("a"),[],JSONType(),
                                JSONLiteral(
                                    [
                                        (Id("name"),StringLiteral("Khoan")),
                                        (Id("age"),NumberLiteral(20.0))
                                    ]
                                )
                                ),
                        Assign(JSONAccess(Id("a"),[StringLiteral("name")]),BinaryOp("+.",StringLiteral("Duc"),StringLiteral("Khoan")))
                    ]
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test11(self):
        input="""
        Function foo(){
            Let a:JSON = {json:{name:"Khoan",class:15},age:20};
            a{"json"}{"name"} = "Duc" +. "Khoan";
        }
        """
        expect = Program(
            [
                FuncDecl(Id("foo"),[],
                    [
                        VarDecl(Id("a"),[],JSONType(),
                                JSONLiteral(
                                    [
                                        (Id("json"),JSONLiteral(
                                            [
                                                (Id("name"),StringLiteral("Khoan")),
                                                (Id("class"),NumberLiteral(15.0))
                                            ]
                                        )),
                                        (Id("age"),NumberLiteral(20.0))
                                    ]
                                )
                                ),
                        Assign(JSONAccess(Id("a"),[StringLiteral("json"),StringLiteral("name")]),BinaryOp("+.",StringLiteral("Duc"),StringLiteral("Khoan")))
                    ]
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test12(self):
        input="""
        Function foo(){
            Let age:Number;
            age = Call(read,[]);
            If ((age>=10)&&(age<=19)){
                Call(printLn,["Teenager"]);
            }Elif (age<10){
                Call(printLn,["Not Teenager"]);
            }Else{
                Call(printLn,["Invalid"]);
            }   
        }
        """
        expect =Program(
            [
                FuncDecl(Id("foo"),[],
                         [
                             VarDecl(Id("age"),[],NumberType(),None),
                             Assign(Id("age"),CallExpr(Id("read"),[])),
                             If(
                                 [
                                     (
                                         BinaryOp("&&",BinaryOp(">=",Id("age"),NumberLiteral(10.0)),BinaryOp("<=",Id("age"),NumberLiteral(19.0))),
                                         [
                                             CallStmt(Id("printLn"), [StringLiteral("Teenager")])
                                         ]
                                     ),
                                     (
                                         BinaryOp("<", Id("age"), NumberLiteral(10.0)),
                                         [
                                             CallStmt(Id("printLn"), [StringLiteral("Not Teenager")])
                                         ]
                                     )
                                 ],
                                 [
                                     CallStmt(Id("printLn"), [StringLiteral("Invalid")])
                                 ]
                             )
                        ])
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))
    def test13(self):
        input="""
        Function foo(){
            For i In [0,10]{
                i = i+1;
                Call(println,[i]);
            }
            For j In a{
                j = j + 1;
                Call(println,[j]);
            }
        }
        """
        expect = Program(
            [
                FuncDecl(Id("foo"),[],
                         [
                             ForIn(Id("i"),ArrayLiteral([NumberLiteral(0.0),NumberLiteral(10.0)]),[
                                 Assign(Id("i"),BinaryOp("+",Id("i"),NumberLiteral(1.0))),
                                 CallStmt(Id("println"),[Id("i")])
                             ]),
                             ForIn(Id("j"), Id("a"), [
                                 Assign(Id("j"), BinaryOp("+", Id("j"), NumberLiteral(1.0))),
                                 CallStmt(Id("println"), [Id("j")])
                             ])
                         ])
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    def test14(self):
        input="""
        Function foo(){
            For i Of {name:"Khoan",age:20}{
                Call(println,[i]);
            }
            For j Of a{
                Call(println,[j]);
            }
        }
        """
        expect = Program(
            [
                FuncDecl(Id("foo"),[],
                         [
                             ForOf(Id("i"),JSONLiteral([(Id("name"),StringLiteral("Khoan")),(Id("age"),NumberLiteral(20.0))]),[
                                 CallStmt(Id("println"),[Id("i")])
                             ]),
                             ForOf(Id("j"), Id("a"), [
                                 CallStmt(Id("println"), [Id("j")])
                             ])
                         ])
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test15(self):
        input="""
        Function foo(){
            Let a[4] = [1,2,3,4];
            Let i:Number = 0;
            While(i<4){
                Call(println,[a[i]]);
            }
        }
        """
        expect=Program(
            [
                FuncDecl(Id("foo"),[],
                         [
                             VarDecl(Id("a"),[NumberLiteral(4.0)],NoneType(),
                                     ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0),NumberLiteral(4.0)])),
                             VarDecl(Id("i"),[],NumberType(),NumberLiteral(0.0)),
                             While(BinaryOp("<",Id("i"),NumberLiteral(4.0)),
                                   [
                                       CallStmt(Id("println"),[ArrayAccess(Id("a"),[Id("i")])])
                                   ])
                         ])
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    def test16(self):
        input="""
        Function foo(){
            Let a[4] = [1,2,3,4];
            Let i:Number = 0;
            While(i<4){
                If(i==2){
                    Break;
                }
                Call(println,[a[i]]);
                i = i+1;
            }
        }
        """
        expect=Program(
            [
                FuncDecl(Id("foo"),[],
                         [
                             VarDecl(Id("a"),[NumberLiteral(4.0)],NoneType(),
                                     ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0),NumberLiteral(4.0)])),
                             VarDecl(Id("i"),[],NumberType(),NumberLiteral(0.0)),
                             While(BinaryOp("<",Id("i"),NumberLiteral(4.0)),
                                   [
                                       If([(BinaryOp('==',Id('i'),NumberLiteral(2.0)),[Break()])],[]),
                                       CallStmt(Id("println"),[ArrayAccess(Id("a"),[Id("i")])]),
                                       Assign(Id("i"),BinaryOp("+",Id("i"),NumberLiteral(1.0)))
                                   ])
                         ])
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test17(self):
        input="""
        Function foo(){
            For i Of {name:"Khoan",age:20}{
                If (i =="name"){
                    Return i;
                }
                Call(println,[i]);
            }
        }
        """
        expect = Program(
            [
                FuncDecl(Id("foo"),[],
                         [
                             ForOf(Id("i"),JSONLiteral([(Id("name"),StringLiteral("Khoan")),(Id("age"),NumberLiteral(20.0))]),[
                                 If([(BinaryOp("==",Id("i"),StringLiteral("name")),[Return(Id("i"))])],[]),
                                 CallStmt(Id("println"),[Id("i")])
                             ])
                         ])
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test18(self):
        input="""
        Function foo(){
            Let a[4] = [1,2,3,4];
            Let i:Number = 4;
            Call(println,[a[i-1],a[-1]]);
        }
        """
        expect=Program(
            [
                FuncDecl(Id("foo"),[],
                         [
                             VarDecl(Id("a"),[NumberLiteral(4.0)],NoneType(),
                                     ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0),NumberLiteral(4.0)])),
                             VarDecl(Id("i"),[],NumberType(),NumberLiteral(4.0)),
                             CallStmt(Id("println"),[
                                 ArrayAccess(Id("a"),
                                                [
                                                     BinaryOp("-",Id("i"),NumberLiteral(1.0))
                                                ]),
                                 ArrayAccess(Id("a"),
                                             [
                                                 UnaryOp("-", NumberLiteral(1.0))
                                             ])
                             ])
                         ])
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test19(self):
        input="""
        Let a,b,c;
        Function main(a,b){
            Constant $b:Number =20;
            a{"hello"} =  c[20,2,2,2];
        }
        """
        expect = Program(
            [
                VarDecl(Id("a"), [], NoneType(), None),
                VarDecl(Id("b"), [], NoneType(), None),
                VarDecl(Id("c"), [], NoneType(), None),
                FuncDecl(Id("main"),[
                            VarDecl(Id("a"),[],NoneType(),None),
                            VarDecl(Id("b"), [], NoneType(), None)
                        ],
                         [
                             ConstDecl(Id("$b"),[],NumberType(),NumberLiteral(20.0)),
                             Assign(JSONAccess(Id("a"),[StringLiteral("hello")]),ArrayAccess(Id("c"),[NumberLiteral(20.0),NumberLiteral(2.0),NumberLiteral(2.0),NumberLiteral(2.0)]))
                         ])
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test20(self):
        input="""
        Function test_call(){
            Call(foo, [2 + x + y, 4 / y]);
            Call(goo, []);
            Return 2+x;
        }
        """
        expect = Program(
            [
                FuncDecl(Id("test_call"),[],
                        [
                            CallStmt(Id("foo"),[BinaryOp("+",BinaryOp('+',NumberLiteral(2.0),Id("x")),Id("y")),BinaryOp('/',NumberLiteral(4.0),Id("y"))]),
                            CallStmt(Id("goo"),[]),
                            Return(BinaryOp("+",NumberLiteral(2.0),Id("x")))
                        ]
                        )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test21(self):
        input="""
        Let a:String = "Khoan";
        Let b:String = "Duc";
        Let c = a +. b;
        Let d = a==.b;
        """
        expect = Program(
            [
                VarDecl(Id("a"),[],StringType(),StringLiteral("Khoan")),
                VarDecl(Id("b"), [], StringType(), StringLiteral("Duc")),
                VarDecl(Id("c"),[],NoneType(),BinaryOp("+.",Id("a"),Id("b"))),
                VarDecl(Id("d"), [], NoneType(), BinaryOp("==.", Id("a"), Id("b")))
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test22(self):
        input="""
        Let a=1;
        Let b=2;
        Let c = a==b;
        Let d = a!=b;
        """
        expect = Program(
            [
                VarDecl(Id("a"),[],NoneType(),NumberLiteral(1.0)),
                VarDecl(Id("b"), [], NoneType(), NumberLiteral(2.0)),
                VarDecl(Id("c"),[],NoneType(),BinaryOp("==",Id("a"),Id("b"))),
                VarDecl(Id("d"), [], NoneType(), BinaryOp("!=", Id("a"), Id("b")))
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test23(self):
        input = """Let a = (c==2)&&!d&&(e!=10)||c;"""
        expect = Program(
            [
                VarDecl(Id("a"),[],NoneType(),
                            BinaryOp("||",
                                     BinaryOp("&&",
                                              BinaryOp("&&",
                                                       BinaryOp("==",Id("c"),NumberLiteral(2.0)),
                                                       UnaryOp("!",Id("d"))
                                                       ),
                                              BinaryOp("!=",Id("e"),NumberLiteral(10.0))
                                              ),
                                     Id("c")
                                     )
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test24(self):
        input="""
        Let a = x+n+b*c-d+e*f;
        """
        expect = Program(
            [
                VarDecl(Id('a'),[],NoneType(),
                        BinaryOp('+',
                                 BinaryOp('-',
                                          BinaryOp('+',
                                                   BinaryOp('+',
                                                            Id("x"),
                                                            Id("n")
                                                            ),
                                                   BinaryOp('*',
                                                            Id("b"),
                                                            Id("c"))
                                                   ),
                                          Id("d")
                                          ),
                                 BinaryOp('*',
                                          Id("e"),
                                          Id("f"))
                                 )
                        )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test25(self):
        input="""
        Let a = x*n/b%c-d*e*f;
        """
        expect = Program(
            [
                VarDecl(Id('a'),[],NoneType(),
                        BinaryOp('-',
                                 BinaryOp('%',
                                          BinaryOp('/',
                                                   BinaryOp('*',
                                                            Id("x"),
                                                            Id("n")
                                                            ),
                                                            Id("b")
                                                   ),
                                          Id("c")
                                          ),
                                 BinaryOp('*',
                                          BinaryOp('*',
                                                   Id("d"),
                                                   Id("e")),
                                          Id("f"))
                                 )
                        )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test26(self):
        input="""
        Function  main(){
            Let a = {name:"Khoan",faculty : "KHMT"};
            Let b;
            b = (a{"name"} +. a{"faculty"}) + Call(foo,[1,2]);
        }
        """
        expect = Program(
            [
                FuncDecl(Id("main"),[],
                         [
                             VarDecl(Id("a"),[],NoneType(),
                                     JSONLiteral(
                                         [
                                             (Id("name"),StringLiteral("Khoan")),
                                             (Id("faculty"),StringLiteral("KHMT"))
                                         ]
                                     )
                                     ),
                             VarDecl(Id("b"),[],NoneType(),None),
                             Assign(Id("b"),
                                    BinaryOp("+",
                                             BinaryOp("+.",
                                                      JSONAccess(Id("a"),[StringLiteral("name")]),
                                                      JSONAccess(Id("a"), [StringLiteral("faculty")])
                                                      ),
                                             CallExpr(Id("foo"),[NumberLiteral(1.0),NumberLiteral(2.0)])
                                             )
                                    )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test27(self):
        input="""
        Let x;
        Function fact(n){
                If (n==0){
                    Return 1;
                }
                Else{
                    Return n * Call(fact,[n - 1]);
                }
        }
        Function main(){
            x = 10;
            Call(fact,[x]);
            }
        """
        expect = Program(
            [
                VarDecl(Id("x"),[],NoneType(),None),
                FuncDecl(Id("fact"),[VarDecl(Id("n"),[],NoneType(),None)],
                         [If(
                             [
                                 (BinaryOp('==',Id('n'),NumberLiteral(0.0)),[Return(NumberLiteral(1.0))])
                             ],
                             [
                                 Return(BinaryOp('*',Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),NumberLiteral(1.0))])))
                             ]
                         )]),
                FuncDecl(Id("main"),[],
                         [
                             Assign(Id("x"),NumberLiteral(10.0)),
                             CallStmt(Id("fact"),[Id("x")])
                         ]
                         )
            ]
        )
        self.assertTrue((TestAST.checkASTGen(input,expect,327)))
    def test28(self):
        input="""Let abc:Number =  1.e+12,    x___asdyz = -0.12E12;"""
        expect = Program(
            [
                VarDecl(Id("abc"),[],NumberType(),NumberLiteral(1.e+12)),
                VarDecl(Id("x___asdyz"), [], NoneType(), UnaryOp('-',NumberLiteral(0.12E12)))
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test29(self):
        input="""
        Let x:Number,y:Number;
        Function main(x,a[3]){
            Let i = 0;
            a[3+Call(foo,[2])] = a[b[2,3]]+4;
        }
        """
        expect = Program(
            [
                VarDecl(Id("x"),[],NumberType(),None),
                VarDecl(Id("y"), [], NumberType(), None),
                FuncDecl(Id('main'),
                         [
                             VarDecl(Id("x"),[],NoneType(),None),
                             VarDecl(Id("a"),[NumberLiteral(3.0)],NoneType(),None)
                         ],
                         [
                             VarDecl(Id("i"), [], NoneType(), NumberLiteral(0.0)),
                             Assign(
                                 ArrayAccess(Id('a'),
                                             [
                                                 BinaryOp('+',
                                                          NumberLiteral(3.0),
                                                          CallExpr(Id("foo"),[NumberLiteral(2.0)])
                                                          )
                                             ]
                                             ),
                                 BinaryOp("+",
                                          ArrayAccess(Id("a"),[ArrayAccess(Id("b"),[NumberLiteral(2.0),NumberLiteral(3.0)])]),
                                          NumberLiteral(4.0)
                                          )
                             )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test30(self):
        input = """
        Function main(x,a[3],b[2,3,2]){
                    Let d = e[Call(foo,[2]),a[5,Call(foo,[2])]];
                    x[2,3,3] = [1,2,[1,2]];
        }
        """
        expect = Program(
            [
                FuncDecl(Id("main"),
                         [
                             VarDecl(Id("x"),[],NoneType(),None),
                             VarDecl(Id("a"), [NumberLiteral(3.0)], NoneType(), None),
                             VarDecl(Id("b"), [NumberLiteral(2.0),NumberLiteral(3.0),NumberLiteral(2.0)], NoneType(), None)
                         ],
                         [
                             VarDecl(Id("d"),[],NoneType(),
                                     ArrayAccess(Id("e"),
                                                 [
                                                     CallExpr(Id("foo"),[NumberLiteral(2.0)]),
                                                     ArrayAccess(Id("a"),
                                                                 [
                                                                    NumberLiteral(5.0),
                                                                    CallExpr(Id("foo"),[NumberLiteral(2.0)])
                                                                 ]
                                                                 )
                                                 ]
                                     )
                                     ),
                             Assign(
                                 ArrayAccess(Id("x"),[NumberLiteral(2.0),NumberLiteral(3.0),NumberLiteral(3.0)]),
                                 ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0)])])
                             )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test31(self):
        input = """
        Function foo(a[5],b){
            Let i=0;
            While(i<5){
                a[i] = b + 1.0;
                i=i+1;
            }
        }"""
        expect = Program(
            [
                FuncDecl(Id('foo'),
                         [
                             VarDecl(Id("a"),[NumberLiteral(5.0)],NoneType(),None),
                             VarDecl(Id("b"),[],NoneType(),None)
                         ],
                         [
                             VarDecl(Id("i"),[],NoneType(),NumberLiteral(0.0)),
                             While(
                                 BinaryOp("<",Id("i"),NumberLiteral(5.0)),
                                 [
                                     Assign(
                                         ArrayAccess(Id("a"),[Id("i")]),
                                         BinaryOp("+",Id("b"),NumberLiteral(1.0))
                                     ),
                                     Assign(
                                         Id("i"),
                                         BinaryOp("+", Id("i"), NumberLiteral(1.0))
                                     )
                                 ]
                             )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test32(self):
        input = """
        Function foo(a[5],b){
            Let i=0;
            While(i<5){
                a[i] = b + 1.0;
                i=i+1;
                If(i>3){
                    Continue;
                }
            }
        }"""
        expect = Program(
            [
                FuncDecl(Id('foo'),
                         [
                             VarDecl(Id("a"),[NumberLiteral(5.0)],NoneType(),None),
                             VarDecl(Id("b"),[],NoneType(),None)
                         ],
                         [
                             VarDecl(Id("i"),[],NoneType(),NumberLiteral(0.0)),
                             While(
                                 BinaryOp("<",Id("i"),NumberLiteral(5.0)),
                                 [
                                     Assign(
                                         ArrayAccess(Id("a"),[Id("i")]),
                                         BinaryOp("+",Id("b"),NumberLiteral(1.0))
                                     ),
                                     Assign(
                                         Id("i"),
                                         BinaryOp("+", Id("i"), NumberLiteral(1.0))
                                     ),
                                     If(
                                         [
                                             (BinaryOp(">",Id("i"),NumberLiteral(3.0)),[Continue()])
                                         ],
                                         []
                                     )
                                 ]
                             )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test33(self):
        input="""
        Function main(){
            Let x=10;
            Let y = "string",temp;
            Constant $a[1,2] = [];
            Let z:JSON = {name:"Khoan",age:18};
            temp = y+z{"name"};
        }"""
        expect = Program(
            [
                FuncDecl(Id("main"),[],
                         [
                             VarDecl(Id("x"),[],NoneType(),NumberLiteral(10.0)),
                             VarDecl(Id("y"), [], NoneType(), StringLiteral("string")),
                             VarDecl(Id("temp"), [], NoneType(), None),
                             ConstDecl(Id("$a"),[NumberLiteral(1.0),NumberLiteral(2.0)],NoneType(),ArrayLiteral([])),
                             VarDecl(Id("z"),[],JSONType(),JSONLiteral([(Id("name"),StringLiteral("Khoan")),(Id("age"),NumberLiteral(18.0))])),
                             Assign(Id("temp"),BinaryOp('+',Id("y"),JSONAccess(Id("z"),[StringLiteral("name")])))

                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test34(self):
        input="""
        Function fact(a[1,2]){
            Let name:String = "";
            For i Of {name:"Khoan",age:18}{
                Call(printLn,[i]);
            }
            While(name!=""){
                name = Call(read,[]);
            }
        }
        """
        expect = Program(
            [
                FuncDecl(Id("fact"),
                         [
                             VarDecl(Id("a"),[NumberLiteral(1.0),NumberLiteral(2.0)],NoneType(),None)
                         ],
                         [
                             VarDecl(Id("name"),[],StringType(),StringLiteral("")),
                             ForOf(
                                 Id("i"),
                                 JSONLiteral(
                                     [
                                         (Id("name"),StringLiteral("Khoan")),
                                         (Id("age"),NumberLiteral(18.0))
                                     ]
                                 ),
                                 [
                                     CallStmt(Id("printLn"),[Id("i")])
                                 ]
                             ),
                             While(
                                 BinaryOp('!=',Id("name"),StringLiteral("")),
                                 [
                                     Assign(Id("name"),CallExpr(Id("read"),[]))
                                 ]
                             )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test35(self):
        input = """
        Function main(){
            Let a[1,5],b[1];
            a[0,1] = Call(foo,[a[2]*b[1,2]+9]);
        }"""
        expect = Program(
            [
                FuncDecl(Id("main"),[],
                         [
                             VarDecl(Id("a"),[NumberLiteral(1.0),NumberLiteral(5.0)],NoneType(),None),
                             VarDecl(Id("b"),[NumberLiteral(1.0)],NoneType(),None),
                             Assign(
                                 ArrayAccess(Id("a"),[NumberLiteral(0.0),NumberLiteral(1.0)]),
                                 CallExpr(Id("foo"),
                                          [
                                              BinaryOp('+',
                                                       BinaryOp('*',
                                                                ArrayAccess(Id("a"),[NumberLiteral(2.0)]),
                                                                ArrayAccess(Id("b"), [NumberLiteral(1.0),NumberLiteral(2.0)])
                                                                ),
                                                       NumberLiteral(9.0)
                                                       )
                                          ]
                                          )
                             )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test36(self):
        input="""
        Function fact(){
            vol = (4.e3/(-3.e-1))*pi*r*r;
            ##result = Call(foo,[a[2]*b[1,2]+9])["hello"]["name"];##
        }
        """
        expect = Program(
            [
                FuncDecl(Id("fact"),[],
                         [
                             Assign(Id("vol"),
                                    BinaryOp('*',
                                             BinaryOp('*',
                                                      BinaryOp('*',
                                                               BinaryOp('/',NumberLiteral(4.e3),UnaryOp('-',NumberLiteral(3.e-1))),
                                                               Id("pi")
                                                               ),
                                                      Id("r")
                                                      ),
                                             Id("r")
                                             )
                                    )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test37(self):
        input="""
        Function fact(){
            result = Call(foo,[a[2]*b[1,2]+9]){"hello"}{"name"};
            Return result;
        }
        """
        expect = Program(
            [
                FuncDecl(Id("fact"),[],
                [
                Assign(
                    Id("result"),
                    JSONAccess(
                        CallExpr(Id("foo"),
                                 [
                                     BinaryOp('+',
                                              BinaryOp('*',
                                                       ArrayAccess(Id("a"), [NumberLiteral(2.0)]),
                                                       ArrayAccess(Id("b"), [NumberLiteral(1.0), NumberLiteral(2.0)])
                                                       ),
                                              NumberLiteral(9.0)
                                              )
                                 ]
                                 ),
                        [
                            StringLiteral("hello"),
                            StringLiteral("name")
                        ]
                    )
                ),
                Return(Id("result"))
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test38(self):
        input="""
        Function fact(){
            Return (!Call(foo,[a[2]*b[1,2]+9]){"hello"}{"name"})&&True;
        }
        """
        expect = Program(
            [
                FuncDecl(Id("fact"),[],
                [
                Return(
                    BinaryOp('&&',
                             UnaryOp('!',
                                     JSONAccess(
                                     CallExpr(Id("foo"),
                                              [
                                                  BinaryOp('+',
                                                           BinaryOp('*',
                                                                    ArrayAccess(Id("a"), [NumberLiteral(2.0)]),
                                                                    ArrayAccess(Id("b"), [NumberLiteral(1.0),
                                                                                          NumberLiteral(2.0)])
                                                                    ),
                                                           NumberLiteral(9.0)
                                                           )
                                              ]
                                              ),
                                     [
                                         StringLiteral("hello"),
                                         StringLiteral("name")
                                     ]
                                     )),
                             BooleanLiteral(True)
                                     )
                             )
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test39(self):
        input="""
        Function test(){
            Let a=0;
            a = 3*3;
            If(b!=True){
                If(a>=0){
                
                }Elif(a!=0){
                
                }
            }Else{
            
            }
        }"""
        expect = Program(
            [
                FuncDecl(Id("test"),[],
                         [
                             VarDecl(Id("a"),[],NoneType(),NumberLiteral(0.0)),
                             Assign(Id("a"),BinaryOp('*',NumberLiteral(3.0),NumberLiteral(3.0))),
                             If(
                                 [
                                     (
                                         BinaryOp('!=',Id("b"),BooleanLiteral(True)),
                                         [
                                             If(
                                                 [
                                                     (
                                                         BinaryOp('>=',Id('a'),NumberLiteral(0.0)),[]
                                                     ),
                                                     (
                                                         BinaryOp('!=', Id('a'), NumberLiteral(0.0)),[]
                                                     )
                                                 ],[]
                                             )
                                         ]
                                     )
                                 ],[]
                             )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test40(self):
        input="""
        Function tranposeOfMatrix(a[10,10],tranpose[10,10],r,c){
            For i In [0,r]{
                For j In [0,c]{
                    tranpose[j,i] = a[i,j];
                }
            }
            Return tranpose;
        }
        """
        expect = Program(
            [
                FuncDecl(Id("tranposeOfMatrix"),
                         [
                             VarDecl(Id("a"),[NumberLiteral(10.0),NumberLiteral(10.0)],NoneType(),None),
                             VarDecl(Id("tranpose"), [NumberLiteral(10.0), NumberLiteral(10.0)], NoneType(), None),
                             VarDecl(Id("r"),[],NoneType(),None),
                             VarDecl(Id("c"), [], NoneType(), None)
                         ],
                         [
                             ForIn(Id("i"),ArrayLiteral([NumberLiteral(0.0),Id("r")]),
                                   [
                                       ForIn(Id("j"), ArrayLiteral([NumberLiteral(0.0), Id("c")]),
                                             [
                                                 Assign(
                                                     ArrayAccess(Id("tranpose"),[Id("j"),Id("i")]),
                                                     ArrayAccess(Id("a"), [Id("i"), Id("j")])
                                                 )
                                             ]
                                             )
                                   ]
                                   ),
                             Return(Id("tranpose"))
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test41(self):
        input="""
        Function test(arr[100],n){
            Let res:Number;
            res = arr[0];
            For i In [0,n]{
                If(arr[i]>res){
                    res = arr[i];
                }
            }
            Return res;
        }
        """
        expect = Program(
            [
                FuncDecl(Id("test"),
                         [
                             VarDecl(Id("arr"), [NumberLiteral(100.0)], NoneType(), None),
                             VarDecl(Id("n"), [], NoneType(), None)
                         ],
                         [
                             VarDecl(Id("res"), [], NumberType(), None),
                             Assign(Id("res"),ArrayAccess(Id("arr"),[NumberLiteral(0.0)])),
                             ForIn(Id("i"),ArrayLiteral([NumberLiteral(0.0),Id("n")]),
                                   [
                                       If(
                                           [
                                               (BinaryOp('>',ArrayAccess(Id("arr"),[Id("i")]),Id("res")),
                                                [
                                                    Assign(Id("res"),ArrayAccess(Id("arr"),[Id("i")]))
                                                ]
                                                )
                                           ],[]
                                       )
                                   ]
                                   ),
                             Return(Id("res"))
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test42(self):
        input = """
        Constant $a = 10;
        Function foo(a[5], b) {
            Constant $b: String = "Story of Yanxi Place";
            Let i = 0;
            While (i < 5) {
                Let u:Number = i + 1;
                a[i] = (b + 1) * $a;
                If (a[u] == 10) {
                    Return $b;
                }
                i = i + 1;
            }
            Return $b + ": Done";
            }"""
        expect = Program(
            [
                ConstDecl(Id("$a"),[],NoneType(),NumberLiteral(10.0)),
                FuncDecl(Id("foo"),
                         [
                             VarDecl(Id("a"),[NumberLiteral(5.0)],NoneType(),None),
                             VarDecl(Id("b"), [], NoneType(), None)
                         ],
                         [
                             ConstDecl(Id("$b"), [], StringType(), StringLiteral("Story of Yanxi Place")),
                             VarDecl(Id("i"), [], NoneType(), NumberLiteral(0.0)),
                             While(
                                 BinaryOp('<',Id("i"),NumberLiteral(5.0)),
                                 [
                                     VarDecl(Id("u"), [], NumberType(), BinaryOp('+',Id("i"),NumberLiteral(1.0))),
                                     Assign(ArrayAccess(Id("a"),[Id("i")]),
                                            BinaryOp('*',
                                                     BinaryOp('+',Id('b'),NumberLiteral(1.0)),
                                                     Id("$a")
                                                     )
                                            ),
                                     If(
                                         [
                                             (
                                                 BinaryOp('==',ArrayAccess(Id("a"),[Id("u")]),NumberLiteral(10.0)),
                                                 [
                                                     Return(Id("$b"))
                                                 ]
                                             )
                                         ],[]
                                     ),
                                     Assign(Id("i"),BinaryOp('+',Id("i"),NumberLiteral(1.0)))
                                 ]
                                   ),
                             Return(BinaryOp('+',Id("$b"),StringLiteral(": Done")))
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test43(self):
        input="""
        Function gcd(a,b){
            If(b==0){
                Return a;
            }
            Return Call(gcd,[b,a%b]);
        }
        """
        expect = Program(
            [
                FuncDecl(Id("gcd"),
                         [
                             VarDecl(Id("a"), [], NoneType(), None),
                             VarDecl(Id("b"), [], NoneType(), None)
                         ],
                         [
                             If(
                                 [
                                     (
                                         BinaryOp('==',Id("b"),NumberLiteral(0.0)),
                                         [Return(Id("a"))]
                                     )
                                 ],[]
                             ),
                             Return(CallExpr(Id("gcd"),[Id("b"),BinaryOp("%",Id("a"),Id("b"))]))
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test44(self):
        input="""
        Function len(str){
            If (str==""){
                Return 0;
            }
            Return 1+Call(len,[str+1]);
        }
        """
        expect = Program(
            [
                FuncDecl(Id("len"),
                         [
                             VarDecl(Id("str"), [], NoneType(), None)
                         ],
                         [
                             If(
                                 [
                                     (
                                         BinaryOp('==', Id("str"), StringLiteral("")),
                                         [Return(NumberLiteral(0.0))]
                                     )
                                 ], []
                             ),
                             Return(
                                 BinaryOp('+',NumberLiteral(1.0),CallExpr(Id("len"),[BinaryOp('+',Id("str"),NumberLiteral(1.0))]))
                             )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test45(self):
        input="""
        Function main(){
            Let a[4];
            Call(read,[a]);
            For i In a{
                If((i%2)!=0){
                    Call(println,["Element is a odd number"]);
                }
            }
        }
        """
        expect = Program(
            [
                FuncDecl(Id("main"),[],
                         [
                             VarDecl(Id("a"), [NumberLiteral(4.0)], NoneType(), None),
                             CallStmt(Id("read"),[Id("a")]),
                             ForIn(Id("i"),Id("a"),
                                   [
                                       If(
                                           [
                                               (
                                                   BinaryOp('!=', BinaryOp('%',Id("i"),NumberLiteral(2.0)), NumberLiteral(0.0)),
                                                   [CallStmt(Id("println"),[StringLiteral("Element is a odd number")])]
                                               )
                                           ], []
                                       )
                                   ]
                                   )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test46(self):
        input="""
        Function printArray(n){
            If(n<0){
                Return;
            }
            Call(printArray,[n-1]);
            If(n==0){
                Call(println,[n]);
            }Else{
                Call(println,[", ",n]);
            }
        }
        """
        expect = Program(
            [
                FuncDecl(Id("printArray"),
                         [
                             VarDecl(Id("n"),[],NoneType(),None)
                         ],
                         [
                             If(
                                 [
                                     (BinaryOp('<',Id("n"),NumberLiteral(0.0)),[Return(None)])
                                 ],[]
                             ),
                             CallStmt(Id("printArray"),[BinaryOp('-',Id("n"),NumberLiteral(1.0))]),
                             If(
                                 [
                                     (BinaryOp('==', Id("n"), NumberLiteral(0.0)), [CallStmt(Id("println"),[Id("n")])])
                                 ],
                                 [
                                     CallStmt(Id("println"), [StringLiteral(", "),Id("n")])
                                 ]
                             )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test47(self):
        input="""
        Function findGCD(a,b){
            Let max,min;
            If(a>b){
                max=a;
                min=b;
            }Else{
                max=b;
                min=a;
            }
            If(min==0){
                Return max;
            }
            Return Call(findGCD,[min,max%min]);
        }
        """
        expect =Program(
            [
                FuncDecl(Id("findGCD"),
                         [
                             VarDecl(Id("a"),[],NoneType(),None),
                             VarDecl(Id("b"), [], NoneType(), None)
                         ],
                         [
                             VarDecl(Id("max"), [], NoneType(), None),
                             VarDecl(Id("min"), [], NoneType(), None),
                             If(
                                 [
                                     (BinaryOp(">",Id("a"),Id("b")),[Assign(Id("max"),Id("a")),Assign(Id("min"),Id("b"))])
                                 ],
                                 [
                                     Assign(Id("max"), Id("b")), Assign(Id("min"), Id("a"))
                                 ]
                             ),
                             If(
                                 [
                                     (BinaryOp("==", Id("min"), NumberLiteral(0.0)),
                                      [Return(Id("max"))])
                                 ],[]
                             ),
                             Return(CallExpr(Id("findGCD"),[Id("min"),BinaryOp('%',Id("max"),Id("min"))]))
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test48(self):
        input="""
        Function findGCD(a,b){
            Let max,min;
            If(a>b){
                max=a;
                min=b;
            }Else{
                max=b;
                min=a;
            }
            If(min==0){
                Return max;
            }
            Return Call(findGCD,[min,max%min]);
        }
        Function findLCM(a,b){
            Return (a*b)/Call(findGCD,[a,b]);
        }
        """
        expect = Program(
            [
                FuncDecl(Id("findGCD"),
                         [
                             VarDecl(Id("a"), [], NoneType(), None),
                             VarDecl(Id("b"), [], NoneType(), None)
                         ],
                         [
                             VarDecl(Id("max"), [], NoneType(), None),
                             VarDecl(Id("min"), [], NoneType(), None),
                             If(
                                 [
                                     (BinaryOp(">", Id("a"), Id("b")),
                                      [Assign(Id("max"), Id("a")), Assign(Id("min"), Id("b"))])
                                 ],
                                 [
                                     Assign(Id("max"), Id("b")), Assign(Id("min"), Id("a"))
                                 ]
                             ),
                             If(
                                 [
                                     (BinaryOp("==", Id("min"), NumberLiteral(0.0)),
                                      [Return(Id("max"))])
                                 ], []
                             ),
                             Return(CallExpr(Id("findGCD"), [Id("min"), BinaryOp('%', Id("max"), Id("min"))]))
                         ]
                         ),
                FuncDecl(Id("findLCM"),
                         [
                             VarDecl(Id("a"), [], NoneType(), None),
                             VarDecl(Id("b"), [], NoneType(), None)
                         ],
                         [
                             Return(
                                 BinaryOp('/',
                                          BinaryOp('*',Id("a"),Id("b")),
                                          CallExpr(Id("findGCD"),[Id("a"),Id("b")])
                                          )
                             )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test49(self):
        input="""
        Function decimalToBinary(decimal_number)
        {
            If (decimal_number == 0) {
                Return 0;
            }
            Else {
                Return decimal_number % 2 + 10 * Call(decimalToBinary,[decimal_number / 2]);
            }
        }
        """
        expect = Program(
            [
                FuncDecl(Id("decimalToBinary"),
                         [
                             VarDecl(Id("decimal_number"),[],NoneType(),None)
                         ],
                         [
                             If(
                                 [
                                     (BinaryOp("==", Id("decimal_number"), NumberLiteral(0.0)),
                                      [Return(NumberLiteral(0.0))])
                                 ],
                                 [
                                     Return(
                                         BinaryOp("+",
                                                  BinaryOp("%",Id("decimal_number"),NumberLiteral(2.0)),
                                                  BinaryOp("*",NumberLiteral(10.0),CallExpr(Id("decimalToBinary"),[BinaryOp("/",Id("decimal_number"),NumberLiteral(2.0))]))
                                                  )
                                     )
                                 ]
                             )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test50(self):
        input ="""
        Function partition (arr[], low,high)
        {
            Let pivot = arr[high];   
            Let left = low;
            Let right = high - 1;
            While(True){
                While((left <= right) && (arr[left] < pivot)){
                    left = left +1; 
                    }
                While((right >= left) && (arr[right] > pivot)){
                    right = right -1;
                    }
                If (left >= right){
                     Break; 
                }
                Call(swap,[arr[left], arr[right]]); 
                left = left +1; 
                right = right-1; 
            }
            Call(swap,[arr[left], arr[right]]);
            Return left;
        }
        """
        expect = Program(
            [
                FuncDecl(Id("partition"),
                         [
                             VarDecl(Id("arr"), [], NoneType(), None),
                             VarDecl(Id("low"), [], NoneType(), None),
                             VarDecl(Id("high"), [], NoneType(), None)
                         ],
                         [
                             VarDecl(Id("pivot"), [], NoneType(), ArrayAccess(Id("arr"),[Id("high")])),
                             VarDecl(Id("left"), [], NoneType(), Id("low")),
                             VarDecl(Id("right"), [], NoneType(), BinaryOp('-',Id("high"),NumberLiteral(1.0))),
                             While(
                                 BooleanLiteral(True),
                                 [
                                     While(
                                         BinaryOp("&&",
                                                  BinaryOp("<=", Id("left"), Id("right")),
                                                  BinaryOp("<", ArrayAccess(Id("arr"),[Id("left")]), Id("pivot"))
                                                  ),
                                         [Assign(Id("left"),BinaryOp("+",Id("left"),NumberLiteral(1.0)))]
                                     ),
                                     While(
                                         BinaryOp("&&",
                                                  BinaryOp(">=", Id("right"), Id("left")),
                                                  BinaryOp(">", ArrayAccess(Id("arr"), [Id("right")]), Id("pivot"))
                                                  ),
                                         [Assign(Id("right"), BinaryOp("-", Id("right"), NumberLiteral(1.0)))]
                                     ),
                                     If(
                                         [
                                             (BinaryOp(">=", Id("left"), Id("right")),[Break()])
                                         ],[]
                                     ),
                                     CallStmt(Id("swap"),[ArrayAccess(Id("arr"),[Id("left")]),ArrayAccess(Id("arr"),[Id("right")])]),
                                     Assign(Id("left"),BinaryOp("+",Id("left"),NumberLiteral(1.0))),
                                     Assign(Id("right"), BinaryOp("-", Id("right"), NumberLiteral(1.0)))
                                 ]
                             ),
                             CallStmt(Id("swap"),[ArrayAccess(Id("arr"), [Id("left")]), ArrayAccess(Id("arr"), [Id("right")])]),
                             Return(Id("left"))
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test51(self):
        input="""
        Function bubbleSort(arr,len){
          Let i,j;
        
          For i In [0,len]{
            For j In [len-1,i]{
              If(arr[j] < arr[j-1]){
                temp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = temp;
              }
            }
          }
          Return arr;
        }
        """
        expect = Program(
            [
                FuncDecl(Id("bubbleSort"),
                         [
                             VarDecl(Id("arr"), [], NoneType(), None),
                             VarDecl(Id("len"), [], NoneType(), None)
                         ],
                         [
                             VarDecl(Id("i"), [], NoneType(), None),
                             VarDecl(Id("j"), [], NoneType(), None),
                             ForIn(Id("i"),ArrayLiteral([NumberLiteral(0.0),Id("len")]),
                                 [
                                     ForIn(Id("j"), ArrayLiteral([BinaryOp('-',Id("len"),NumberLiteral(1.0)), Id("i")]),
                                         [
                                             If(
                                                 [
                                                     (
                                                         BinaryOp("<", ArrayAccess(Id("arr"),[Id("j")]), ArrayAccess(Id("arr"),[BinaryOp("-", Id("j"), NumberLiteral(1.0))])),
                                                        [
                                                            Assign(Id("temp"), ArrayAccess(Id("arr"), [Id("j")])),
                                                            Assign(ArrayAccess(Id("arr"), [Id("j")]),ArrayAccess(Id("arr"), [BinaryOp("-", Id("j"), NumberLiteral(1.0))])),
                                                            Assign(ArrayAccess(Id("arr"), [BinaryOp("-", Id("j"), NumberLiteral(1.0))]),Id("temp"))
                                                        ]
                                                     )
                                                 ],[]
                                             )

                                         ]
                                         )
                                 ]
                                 ),
                             Return(Id("arr"))
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test52(self):
        input="""
        Function gtc(n){
            If((n==0)||(n==1)){
                Return 1;
            }
            Return n*Call(gtc,[n-2]);
        }
        """
        expect = Program(
            [
                FuncDecl(Id("gtc"),[VarDecl(Id("n"),[],NoneType(),None)],
                         [
                             If(
                                 [
                                     (
                                         BinaryOp('||',BinaryOp("==", Id("n"), NumberLiteral(0.0)),BinaryOp("==", Id("n"), NumberLiteral(1.0))),
                                         [Return(NumberLiteral(1.0))]
                                     )
                                 ],[]
                             ),
                             Return(BinaryOp('*',Id("n"),CallExpr(Id("gtc"),[BinaryOp('-',Id("n"),NumberLiteral(2.0))])))
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test53(self):
        input = """
           Function fibonaci(n){
               If(n<0){
                   Return -1;
               }Elif((n==0)||(n==1)){
                   Return n;
               }Else{
                   Return Call(fibonaci,[n-1])+Call(fibonaci,[n-2]);
               }
           }
           """
        expect = Program(
            [
                FuncDecl(Id("fibonaci"),
                         [
                             VarDecl(Id("n"), [], NoneType(), None)
                         ],
                         [
                             If(
                                 [
                                     (
                                         BinaryOp("<", Id("n"), NumberLiteral(0.0)),
                                         [Return(UnaryOp('-', NumberLiteral(1.0)))]
                                     ),
                                     (
                                         BinaryOp("||",
                                                  BinaryOp("==", Id("n"), NumberLiteral(0.0)),
                                                  BinaryOp("==", Id("n"), NumberLiteral(1.0))),
                                         [Return(Id("n"))]
                                     )
                                 ],
                                 [
                                     Return(
                                         BinaryOp("+",
                                                  CallExpr(Id("fibonaci"),
                                                           [BinaryOp("-", Id("n"), NumberLiteral(1.0))]),
                                                  CallExpr(Id("fibonaci"), [BinaryOp("-", Id("n"), NumberLiteral(2.0))])
                                                  )
                                     )
                                 ]
                             )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test54(self):
        input = """
           Function string_reverse(str[]) {
               Let i, j, len;
               Let ch;

               j = Call(string_length,[str]) - 1;
               len=j;
               i = 0;

               While(i < j) {
                   ch = str[j];
                   str[j] = str[i];
                   str[i] = ch;
                   i=i+1;
                   j = j-1;
               }
           }
           """
        expect = Program(
            [
                FuncDecl(Id("string_reverse"),
                         [
                             VarDecl(Id("str"), [], NoneType(), None)
                         ],
                         [
                             VarDecl(Id("i"), [], NoneType(), None),
                             VarDecl(Id("j"), [], NoneType(), None),
                             VarDecl(Id("len"), [], NoneType(), None),
                             VarDecl(Id("ch"), [], NoneType(), None),
                             Assign(Id('j'),
                                    BinaryOp('-', CallExpr(Id('string_length'), [Id("str")]),NumberLiteral(1.0))
                                    ),
                             Assign(Id('len'), Id("j")),
                             Assign(Id('i'), NumberLiteral(0.0)),
                             While(
                                 BinaryOp("<", Id("i"), Id('j')),
                                 [
                                     Assign(Id("ch"), ArrayAccess(Id("str"), [Id("j")])),
                                     Assign(ArrayAccess(Id("str"), [Id("j")]), ArrayAccess(Id("str"), [Id("i")])),
                                     Assign(ArrayAccess(Id("str"), [Id("i")]), Id('ch')),
                                     Assign(Id("i"), BinaryOp('+', Id('i'), NumberLiteral(1.0))),
                                     Assign(Id("j"), BinaryOp('-', Id('j'), NumberLiteral(1.0)))
                                 ]
                             )

                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test55(self):
        input = """
           Constant $dec_10 = 10;
           Function totalDigitsOfNumber(n) {
               Let total = 0;
               While (n > 0){
                   total = total + n % $dec_10;
                   n = n / $dec_10;
               }
               Return total;
           }
           """
        expect = Program(
            [
                ConstDecl(Id('$dec_10'), [], NoneType(), NumberLiteral(10.0)),
                FuncDecl(Id("totalDigitsOfNumber"),
                         [
                             VarDecl(Id("n"), [], NoneType(), None)
                         ],
                         [
                             VarDecl(Id("total"), [], NoneType(), NumberLiteral(0.0)),
                             While(
                                 BinaryOp(">", Id("n"), NumberLiteral(0.0)),
                                 [
                                     Assign(Id('total'), BinaryOp('+',
                                                                  Id("total"),
                                                                  BinaryOp('%', Id("n"), Id('$dec_10')))

                                            ),
                                     Assign(Id('n'), BinaryOp('/',
                                                              Id("n"),
                                                              Id('$dec_10'))

                                            )
                                 ]
                             ),
                             Return(Id('total'))
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test56(self):
        input = """
           Constant $MAX = 1000;
           Function shellSort(){
               Let inner, outer;
               Let valueToInsert;
               Let interval = 1;
               Let elements = $MAX;
               Let i = 0;
               While(interval <= (elements / 3)) {
                   interval = interval * 3 + 1;
               }
               While(interval > 0) {
                   For outer In [interval,elements-1] {
                       valueToInsert = arr[outer];
                       inner = outer;

                       While((inner > (interval -1)) && (arr[inner - interval] >= valueToInsert)) {
                           arr[inner] = arr[inner - interval];
                           inner = inner - interval;
                       }

                       arr[inner] = valueToInsert;
                   }
                   interval = (interval -1) /3;
                   i = i+1;
               }
           }
           """
        expect = Program(
            [
                ConstDecl(Id('$MAX'), [], NoneType(), NumberLiteral(1000.0)),
                FuncDecl(Id("shellSort"),
                         [],
                         [
                             VarDecl(Id("inner"), [], NoneType(), None),
                             VarDecl(Id("outer"), [], NoneType(), None),
                             VarDecl(Id("valueToInsert"), [], NoneType(), None),
                             VarDecl(Id("interval"), [], NoneType(), NumberLiteral(1.0)),
                             VarDecl(Id("elements"), [], NoneType(), Id('$MAX')),
                             VarDecl(Id("i"), [], NoneType(), NumberLiteral(0.0)),
                             While(
                                 BinaryOp("<=", Id("interval"), BinaryOp('/', Id("elements"), NumberLiteral(3.0))),
                                 [
                                     Assign(Id('interval'), BinaryOp('+',
                                                                     BinaryOp('*', Id("interval"), NumberLiteral(3.0)),
                                                                     NumberLiteral(1.0))

                                            )
                                 ]
                             ),
                             While(
                                 BinaryOp(">", Id("interval"), NumberLiteral(0.0)),
                                 [
                                     ForIn(Id('outer'), ArrayLiteral(
                                         [Id('interval'), BinaryOp('-', Id("elements"), NumberLiteral(1.0))]),
                                           [
                                               Assign(Id("valueToInsert"), ArrayAccess(Id("arr"), [Id("outer")])),
                                               Assign(Id('inner'), Id("outer")),
                                               While(
                                                   BinaryOp("&&",
                                                            BinaryOp('>',
                                                                     Id("inner"),
                                                                     BinaryOp('-', Id("interval"), NumberLiteral(1.0))),
                                                            BinaryOp('>=',
                                                                     ArrayAccess(Id('arr'), [
                                                                         BinaryOp('-', Id("inner"), Id("interval"))]),
                                                                     Id("valueToInsert"))),
                                                   [
                                                       Assign(ArrayAccess(Id("arr"), [Id("inner")]),
                                                              ArrayAccess(Id("arr"), [
                                                                  BinaryOp('-', Id("inner"), Id("interval"))])),
                                                       Assign(Id('inner'), BinaryOp('-', Id("inner"), Id("interval")))
                                                   ]
                                               ),
                                               Assign(ArrayAccess(Id("arr"), [Id("inner")]), Id('valueToInsert'))

                                           ]
                                           ),
                                     Assign(Id('interval'), BinaryOp('/',
                                                                     BinaryOp('-', Id("interval"), NumberLiteral(1.0)),
                                                                     NumberLiteral(3.0))),
                                     Assign(Id('i'), BinaryOp('+',
                                                              Id("i"),
                                                              NumberLiteral(1.0)))

                                 ]
                             )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test57(self):
        input = """
           Constant $a=10;
            Function main(){
               Let b:JSON = {name:"Khoan",list : [1,2,3,4,5]};
               x = b{"list"};
               x[0] = 20;
               Return;
            }
           """
        expect = Program(
            [
                ConstDecl(Id('$a'), [], NoneType(), NumberLiteral(10.0)),
                FuncDecl(Id("main"), [],
                         [
                             VarDecl(Id('b'), [], JSONType(), JSONLiteral([(Id("name"), StringLiteral("Khoan")), (
                             Id('list'), ArrayLiteral(
                                 [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0), NumberLiteral(4.0),
                                  NumberLiteral(5.0)]))])),
                             Assign(Id("x"),JSONAccess(Id('b'), [StringLiteral("list")])),
                             Assign(ArrayAccess(Id('x'), [NumberLiteral(0.0)]),
                                    NumberLiteral(20.0)),
                             Return(None)
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test58(self):
        input = """
           Function main(){
               Let sum=0;
               Let a = {a_1:[1,2,3,4,5],a_2:[10,11,12]};
               For i Of a{
                   For j In i {
                       sum = sum + j;
                   }
               }
               Return sum;
           }
           """
        expect = Program([
            FuncDecl(Id('main'), [],
                     [
                         VarDecl(Id('sum'), [], NoneType(), NumberLiteral(0.0)),
                         VarDecl(Id('a'), [], NoneType(),
                                 JSONLiteral([(Id("a_1"), ArrayLiteral(
                                     [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0), NumberLiteral(4.0),
                                      NumberLiteral(5.0)])),
                                              (Id('a_2'), ArrayLiteral(
                                                  [NumberLiteral(10.0), NumberLiteral(11.0), NumberLiteral(12.0)]))])),
                         ForOf(Id('i'), Id('a'),
                               [
                                   ForIn(Id('j'), Id('i'),
                                         [
                                             Assign(Id('sum'), BinaryOp('+', Id('sum'), Id('j')))
                                         ]
                                         )
                               ]
                               ),
                         Return(Id('sum'))
                     ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test59(self):
        input="""
        Function main(){
            Let x = Call(foo,[])+Call(boo,[i]);
            Call(foo,[n]);
            }
        """
        expect = Program(
            [
                FuncDecl(Id("main"),[],
                         [
                             VarDecl(Id("x"),[],NoneType(),BinaryOp("+",CallExpr(Id("foo"),[]),CallExpr(Id("boo"),[Id("i")]))),
                             CallStmt(Id("foo"),[Id("n")])
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test60(self):
        input="""
        Function countSort(arr[100],n,exp){
            Let output[100];
            Let i,count[10] = arr[0];
            For i In [1,100]{
                count[(arr[i]/exp)%10] = count[(arr[i] / exp) % 10] + 1;
            }
            For i In [1,10]{
                count[i] = count[i - 1] + count[i];
            }
            For i In [10,0] {
                output[count[(arr[i] / exp)%10] - 1] = arr[i];
                count[(arr[i] / exp) % 10] = count[(arr[i] / exp) % 10] - 1;
            }

            For i In [0,10]{
                arr[i] = count[i];
            }
        }
        """
        expect = Program(
            [
                FuncDecl(Id("countSort"),
                         [
                             VarDecl(Id("arr"),[NumberLiteral(100.0)],NoneType(),None),
                             VarDecl(Id("n"),[],NoneType(),None),
                             VarDecl(Id("exp"), [], NoneType(), None)
                         ],
                         [
                             VarDecl(Id("output"),[NumberLiteral(100.0)],NoneType(),None),
                             VarDecl(Id("i"), [], NoneType(), None),
                             VarDecl(Id("count"), [NumberLiteral(10.0)], NoneType(), ArrayAccess(Id("arr"),[NumberLiteral(0.0)])),
                             ForIn(Id("i"),ArrayLiteral([NumberLiteral(1.0),NumberLiteral(100.0)]),
                                   [
                                       Assign(
                                           ArrayAccess(Id("count"),
                                                       [
                                                           BinaryOp('%',
                                                                    BinaryOp("/",
                                                                             ArrayAccess(Id("arr"),[Id("i")]),
                                                                             Id("exp")
                                                                             ),
                                                                    NumberLiteral(10.0)
                                                                    )
                                                       ]
                                                       ),
                                           BinaryOp("+",
                                                   ArrayAccess(Id("count"),
                                                               [
                                                                   BinaryOp('%',
                                                                            BinaryOp("/",
                                                                                     ArrayAccess(Id("arr"), [Id("i")]),
                                                                                     Id("exp")
                                                                                     ),
                                                                            NumberLiteral(10.0)
                                                                            )
                                                               ]
                                                               ),
                                                    NumberLiteral(1.0)
                                                    )
                                       )
                                   ]
                                   ),
                             ForIn(Id("i"), ArrayLiteral([NumberLiteral(1.0), NumberLiteral(10.0)]),
                                   [
                                       Assign(ArrayAccess(Id("count"),[Id("i")]),
                                              BinaryOp("+",
                                                       ArrayAccess(Id("count"), [BinaryOp("-",Id("i"),NumberLiteral(1.0))]),
                                                       ArrayAccess(Id("count"), [Id("i")])
                                                       )
                                              )

                                   ]
                             ),
                             ForIn(Id("i"), ArrayLiteral([NumberLiteral(10.0), NumberLiteral(0.0)]),
                                   [
                                       Assign(
                                           ArrayAccess(Id("output"),
                                                       [
                                                           BinaryOp("-",
                                                                    ArrayAccess(Id("count"),
                                                                                [
                                                                                    BinaryOp('%',
                                                                                             BinaryOp("/",
                                                                                                      ArrayAccess(Id("arr"),[Id("i")]),
                                                                                                      Id("exp")
                                                                                                      ),
                                                                                             NumberLiteral(10.0)
                                                                                             )
                                                                                ]
                                                                                ),
                                                                    NumberLiteral(1.0))
                                                       ]
                                                       ),
                                           ArrayAccess(Id("arr"), [Id("i")])

                                       ),
                                       Assign(
                                           ArrayAccess(Id("count"),
                                                       [
                                                           BinaryOp('%',
                                                                    BinaryOp("/",
                                                                             ArrayAccess(Id("arr"), [Id("i")]),
                                                                             Id("exp")
                                                                             ),
                                                                    NumberLiteral(10.0)
                                                                    )
                                                       ]
                                                       ),
                                           BinaryOp("-",
                                                    ArrayAccess(Id("count"),
                                                                [
                                                                    BinaryOp('%',
                                                                             BinaryOp("/",
                                                                                      ArrayAccess(Id("arr"),
                                                                                                  [Id("i")]),
                                                                                      Id("exp")
                                                                                      ),
                                                                             NumberLiteral(10.0)
                                                                             )
                                                                ]
                                                                ),
                                                    NumberLiteral(1.0))
                                       )
                                   ]
                             ),
                             ForIn(Id("i"), ArrayLiteral([NumberLiteral(0.0), NumberLiteral(10.0)]),
                                   [
                                       Assign(ArrayAccess(Id("arr"), [Id("i")]),ArrayAccess(Id("count"), [Id("i")]))
                                   ]
                                   )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test61(self):
        input="""
        Function search(arr[$MAX],x)
        {
            For i In arr{
                If (arr[i] == x){
                    Return i;
                }
                }
            Return -1;
        }
        """
        expect = Program(
            [
                FuncDecl(Id("search"),
                         [
                             VarDecl(Id("arr"),[Id("$MAX")],NoneType(),None),
                             VarDecl(Id("x"), [], NoneType(), None)
                         ],
                         [
                             ForIn(Id("i"),Id("arr"),
                                   [
                                       If(
                                           [
                                               (BinaryOp('==', ArrayAccess(Id("arr"),[Id("i")]), Id("x")),[Return(Id("i"))])
                                           ],[]
                                       )
                                   ]
                                   ),
                             Return(UnaryOp('-',NumberLiteral(1.0)))
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test61(self):
        input ="""
        Function binarySearch(arr[$MAX],l,r,x)
        {
            If (r >= l) {
                Let mid = l + (r - l) / 2;
                If (arr[mid] == x){
                    Return mid;
                }
                If (arr[mid] > x){
                    Return Call(binarySearch,[arr, l, mid - 1, x]);
                }
                Return Call(binarySearch,[arr, mid + 1, r, x]);
            }
            Return -1;
        }"""
        expect = Program(
            [
                FuncDecl(Id("binarySearch"),
                         [
                             VarDecl(Id("arr"), [Id("$MAX")], NoneType(), None),
                             VarDecl(Id("l"), [], NoneType(), None),
                             VarDecl(Id("r"), [], NoneType(), None),
                             VarDecl(Id("x"), [], NoneType(), None)
                         ],
                         [
                            If(
                                [
                                    (BinaryOp('>=',Id("r"),Id("l")),
                                     [
                                         VarDecl(Id("mid"),[],NoneType(),
                                                 BinaryOp('+',Id("l"),
                                                          BinaryOp('/',
                                                                   BinaryOp("-",Id("r"),Id("l")),
                                                                   NumberLiteral(2.0)
                                                                   )

                                                          )
                                                 ),
                                         If(
                                             [
                                                 (BinaryOp("==",ArrayAccess(Id("arr"),[Id("mid")]),Id("x")),
                                                  [
                                                      Return(Id("mid"))
                                                  ]
                                                  )
                                             ],[]
                                         ),
                                         If(
                                             [
                                                 (BinaryOp(">", ArrayAccess(Id("arr"), [Id("mid")]), Id("x")),
                                                  [
                                                      Return(CallExpr(Id("binarySearch"),[Id("arr"),Id("l"),BinaryOp("-",Id("mid"),NumberLiteral(1.0)),Id("x")]))
                                                  ]
                                                  )
                                             ], []
                                         ),
                                         Return(CallExpr(Id("binarySearch"), [Id("arr"),BinaryOp("+", Id("mid"),NumberLiteral(1.0)), Id("r"), Id("x")]))
                                     ]
                                     )
                                ],[]
                            ),
                             Return(UnaryOp("-",NumberLiteral(1.0)))
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test62(self):
        input="""
        Function jumpSearch(arr[$MAX],x,n)
        {
            Let step = Call(sqrt,[n]);
            Let prev = 0;
            While (arr[Call(min,[step, n])-1] < x)
            {
                prev = step;
                step =step+ Call(sqrt,[n]);
                If (prev >= n){
                    Return -1;
                    }
            }
         
            While (arr[prev] < x)
            {
                prev = prev +1;
         
                If (prev == Call(min,[step, n])){
                    Return -1;
                    }
            }
            If (arr[prev] == x){
                Return prev;
                }
         
            Return -1;
        }"""
        expect = Program(
            [
                FuncDecl(Id("jumpSearch"),
                         [
                             VarDecl(Id("arr"), [Id("$MAX")], NoneType(), None),
                             VarDecl(Id("x"), [], NoneType(), None),
                             VarDecl(Id("n"), [], NoneType(), None),
                         ],
                         [
                             VarDecl(Id("step"), [], NoneType(), CallExpr(Id("sqrt"),[Id("n")])),
                             VarDecl(Id("prev"), [], NoneType(), NumberLiteral(0.0)),
                             While(
                                 BinaryOp("<",
                                     ArrayAccess(
                                         Id("arr"),
                                         [
                                            BinaryOp('-',
                                                     CallExpr(Id("min"),[Id("step"),Id("n")]),
                                                     NumberLiteral(1.0)
                                                     )
                                         ]
                                     ),
                                          Id("x")
                                 ),
                                 [
                                     Assign(Id("prev"),Id("step")),
                                     Assign(Id("step"),BinaryOp("+",Id("step"),CallExpr(Id("sqrt"),[Id("n")]))),
                                     If(
                                         [
                                             (
                                                 BinaryOp(">=",Id("prev"),Id("n")),
                                                 [Return(UnaryOp("-",NumberLiteral(1.0)))]
                                             )
                                         ],[]
                                     )
                                 ]

                             ),
                             While(
                                 BinaryOp("<",
                                          ArrayAccess(Id("arr"),[Id("prev")]),
                                          Id("x")
                                          ),
                                 [
                                     Assign(Id("prev"), BinaryOp("+", Id("prev"), NumberLiteral(1.0))),
                                     If(
                                         [
                                             (
                                                 BinaryOp("==", Id("prev"),
                                                          CallExpr(Id("min"),[Id("step"),Id("n")])
                                                          ),
                                                 [Return(UnaryOp("-",NumberLiteral(1.0)))]
                                             )
                                         ], []
                                     )
                                 ]

                             ),
                             If(
                                 [
                                     (
                                         BinaryOp("==",
                                                  ArrayAccess(Id("arr"), [Id("prev")]),
                                                  Id("x")
                                                  ),
                                         [Return(Id("prev"))]
                                     )
                                 ],[]
                             ),
                             Return(UnaryOp("-", NumberLiteral(1.0)))

                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test63(self):
        input="""
        Constant $a = 10;
        Let b[2] = [[],[2,2]];
        """
        expect = Program([
            ConstDecl(Id("$a"),[],NoneType(),NumberLiteral(10.0)),
            VarDecl(Id("b"),[NumberLiteral(2.0)],NoneType(),ArrayLiteral([ArrayLiteral([]),ArrayLiteral([NumberLiteral(2.0),NumberLiteral(2.0)])]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test64(self):
        input="""
        Function main(){
            Constant $a = 10;
            Let b[2] = [[],[2,2]];
            b[$a] = {name:"Khoan"};
        }
        """
        expect = Program([
            FuncDecl(Id("main"),[],[
                ConstDecl(Id("$a"),[],NoneType(),NumberLiteral(10.0)),
                VarDecl(Id("b"),[NumberLiteral(2.0)],NoneType(),ArrayLiteral([ArrayLiteral([]),ArrayLiteral([NumberLiteral(2.0),NumberLiteral(2.0)])])),
                Assign(ArrayAccess(Id("b"),[Id("$a")]),JSONLiteral([(Id("name"),StringLiteral("Khoan"))]))
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test65(self):
        input="""
        Function main(){
            Constant $a = 10;
            Let b[2] = [[],[2,2]];
            b[$a] = {name:"Khoan"};
            Constant $n = [];
        }
        """
        expect = Program([
            FuncDecl(Id("main"),[],[
                ConstDecl(Id("$a"),[],NoneType(),NumberLiteral(10.0)),
                VarDecl(Id("b"),[NumberLiteral(2.0)],NoneType(),ArrayLiteral([ArrayLiteral([]),ArrayLiteral([NumberLiteral(2.0),NumberLiteral(2.0)])])),
                Assign(ArrayAccess(Id("b"),[Id("$a")]),JSONLiteral([(Id("name"),StringLiteral("Khoan"))])),
                ConstDecl(Id("$n"),[],NoneType(),ArrayLiteral([]))
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test66(self):
        input="""
        Let a = [1,2]+ ["String"];
        """
        expect = Program(
            [
                VarDecl(Id("a"),[],NoneType(),BinaryOp('+',ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0)]),ArrayLiteral([StringLiteral("String")])))
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test67(self):
        input = """
        Let a = [1,2]+ a{"name"}+a[0];
        """
        expect = Program(
            [
                VarDecl(Id("a"), [], NoneType(),
                        BinaryOp("+",
                            BinaryOp('+', ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)]),
                                                          JSONAccess(Id("a"),[StringLiteral("name")])),
                                 ArrayAccess(Id("a"),[NumberLiteral(0.0)])
                                 )
                        )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test68(self):
        input="""
        Function main(a[],b){
            Break;
            Continue;
            Return;    
        }
        """
        expect = Program([
            FuncDecl(Id("main"),
                     [
                         VarDecl(Id("a"),[],NoneType(),None),
                         VarDecl(Id("b"),[],NoneType(),None)
                     ],
                     [
                         Break(),
                         Continue(),
                         Return(None)
                     ]
                     )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test69(self):
        input="""
        Function main_1(a){
            Return;    
        }
        Function main_2(a){
            Return;    
        }
        Function main(){
            Call(main_1,[2]);
            }  
        """
        expect = Program([
            FuncDecl(Id("main_1"),
                     [
                         VarDecl(Id("a"), [], NoneType(), None),
                     ],
                     [
                         Return(None)
                     ]
                     ),
            FuncDecl(Id("main_2"),
                     [
                         VarDecl(Id("a"), [], NoneType(), None),
                     ],
                     [
                         Return(None)
                     ]
                     ),
            FuncDecl(Id("main"),[],
                     [
                         CallStmt(Id("main_1"),[NumberLiteral(2.0)])
                     ]
                     )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test70(self):
        input = """
            Function main(){
                If (True){}
                While(True){}
                }
        """
        expect = Program(
            [
                FuncDecl(Id("main"),[],
                         [
                             If([(BooleanLiteral(True),[])],[]),
                             While(BooleanLiteral(True),[])
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test71(self):
        input = """
        Function main(){
            Call(foo,[Call(foo,[])]);
            }
        """
        expect =Program(
            [
                FuncDecl(Id("main"),[],
                         [
                             CallStmt(Id("foo"),[CallExpr(Id("foo"),[])])
                         ])
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test72(self):
        input="""
        Function main(){
            Let a="Le Duc Khoan";
            Let b = 1.234e+1;
        }
        """
        expect = Program([
            FuncDecl(Id("main"),[],
                     [
                         VarDecl(Id("a"),[],NoneType(),StringLiteral("Le Duc Khoan")),
                         VarDecl(Id("b"),[],NoneType(),NumberLiteral(1.234e+1))
                     ]
                     )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test73(self):
        input = """
        Function main(){
        }
        """
        expect = Program([FuncDecl(Id("main"),[],[])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test74(self):
        input = """
        Let a:Number = a;
        """
        expect = Program([VarDecl(Id("a"),[],NumberType(),Id("a"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test75(self):
        input = """
        Let a:Number=0,b:String="Khoan",c:Boolean = True;
        """
        expect = Program(
            [
                VarDecl(Id("a"),[],NumberType(),NumberLiteral(0.0)),
                VarDecl(Id("b"), [], StringType(), StringLiteral("Khoan")),
                VarDecl(Id("c"), [], BooleanType(), BooleanLiteral(True))
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test76(self):
        input = """
        Function main(){
            a["hello"[1]]=0;
            }
        """
        expect = Program(
            [
                FuncDecl(Id("main"),[],
                         [
                             Assign(ArrayAccess(Id("a"),[ArrayAccess(StringLiteral("hello"),[NumberLiteral(1.0)])]),NumberLiteral(0.0))
                         ])
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test77(self):
        input = """
        Function main(){
            a[True[1]]=0;
            }
        """
        expect = Program(
            [
                FuncDecl(Id("main"),[],
                         [
                             Assign(ArrayAccess(Id("a"),[ArrayAccess(BooleanLiteral(True),[NumberLiteral(1.0)])]),NumberLiteral(0.0))
                         ])
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test78(self):
        input="""
        Function main(){
            Call(foo,[])[1]=2;
        }
        """
        expect = Program([
            FuncDecl(Id("main"),[],
                     [
                         Assign(ArrayAccess(CallExpr(Id("foo"),[]),[NumberLiteral(1.0)]),NumberLiteral(2.0))
                     ]
                     )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test79(self):
        input="""
        Function main(){
            Call(foo,[a+2])[1,"String"]=2;
        }
        """
        expect = Program([
            FuncDecl(Id("main"),[],
                     [
                         Assign(ArrayAccess(CallExpr(Id("foo"),[BinaryOp('+',Id("a"),NumberLiteral(2.0))]),[NumberLiteral(1.0),StringLiteral("String")]),NumberLiteral(2.0))
                     ]
                     )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test80(self):
        input="""
        Function main(){
            Call(foo,[a+2]){"String"}{2}=2;
        }
        """
        expect = Program([
            FuncDecl(Id("main"),[],
                     [
                         Assign(JSONAccess(CallExpr(Id("foo"),[BinaryOp('+',Id("a"),NumberLiteral(2.0))]),[StringLiteral("String"),NumberLiteral(2.0)]),NumberLiteral(2.0))
                     ]
                     )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test81(self):
        input="""
        Function main(){
            Call(foo,[a+2]){"String"}{2}={};
        }
        """
        expect = Program([
            FuncDecl(Id("main"),[],
                     [
                         Assign(JSONAccess(CallExpr(Id("foo"),[BinaryOp('+',Id("a"),NumberLiteral(2.0))]),[StringLiteral("String"),NumberLiteral(2.0)]),JSONLiteral([]))
                     ]
                     )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test82(self):
        input = """
        Function test_call(){
            a = Call(foo, [2 + x + y, 4 / y])[0];
            b = Call(goo, []){b};
            Return 2+x;
        }
        """
        expect = Program(
            [
                FuncDecl(Id("test_call"), [],
                         [
                             Assign(Id("a"),ArrayAccess(CallExpr(Id("foo"), [BinaryOp("+", BinaryOp('+', NumberLiteral(2.0), Id("x")), Id("y")),
                                                  BinaryOp('/', NumberLiteral(4.0), Id("y"))]),[NumberLiteral(0.0)])),
                             Assign(Id("b"),JSONAccess(CallExpr(Id("goo"), []),[Id("b")])),
                             Return(BinaryOp("+", NumberLiteral(2.0), Id("x")))
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test83(self):
        input="""
        ##Chuong trinh nay khong co gi test dau##
        """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test84(self):
        input="""
        Let a = True||True&&False||(!True);
        """
        expect = Program([
            VarDecl(Id("a"),[],NoneType(),
                    BinaryOp("||",
                             BinaryOp("&&",
                                      BinaryOp("||",
                                               BooleanLiteral(True),
                                               BooleanLiteral(True)
                                               ),
                                      BooleanLiteral(False)
                                      ),
                             UnaryOp("!", BooleanLiteral(True)))
                             )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test85(self):
        input="""
        Let x:Number,y:Number;
        Function main(x,a[5]){
            ##Let a = "Le Duc Khoan";##    
        }
        """
        expect = Program([
            VarDecl(Id("x"),[],NumberType(),None),
            VarDecl(Id("y"),[],NumberType(),None),
            FuncDecl(Id("main"),[
                VarDecl(Id("x"), [], NoneType(), None),
                VarDecl(Id("a"), [NumberLiteral(5.0)], NoneType(), None)
            ],[])
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test86(self):
        input = """
            Function fact(x,y){
                Let x =1,y:Number = 10;
                Let a[5,1] = [],b[1];
            }
        """
        expect = Program(
            [
                FuncDecl(Id("fact"),
                         [
                             VarDecl(Id("x"), [], NoneType(), None),
                             VarDecl(Id("y"), [], NoneType(), None)
                         ],
                         [
                             VarDecl(Id("x"), [], NoneType(), NumberLiteral(1.0)),
                             VarDecl(Id("y"), [], NumberType(), NumberLiteral(10.0)),
                             VarDecl(Id("a"), [NumberLiteral(5.0),NumberLiteral(1.0)], NoneType(), ArrayLiteral([])),
                             VarDecl(Id("b"), [NumberLiteral(1.0)], NoneType(), None)
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test87(self):
        input = """
            Function area(x,y){
                Return x*y;
            }
        """
        expect = Program(
            [
                FuncDecl(Id("area"),
                         [
                             VarDecl(Id("x"),[],NoneType(),None),
                             VarDecl(Id("y"), [], NoneType(), None)
                         ],
                         [
                             Return(BinaryOp('*',Id("x"),Id("y")))
                         ])
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test88(self):
        input = """
            Function area(x,y){
                If (y==0){
                    a = !a;
                }
                Return x*y;
            }
        """
        expect = Program(
            [
                FuncDecl(Id("area"),
                         [
                             VarDecl(Id("x"),[],NoneType(),None),
                             VarDecl(Id("y"), [], NoneType(), None)
                         ],
                         [
                             If(
                                 [
                                     (
                                         BinaryOp('==',Id("y"),NumberLiteral(0.0)),
                                         [Assign(Id("a"),UnaryOp('!',Id("a")))]
                                     )
                                 ],[]
                             ),
                             Return(BinaryOp('*',Id("x"),Id("y")))
                         ])
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test89(self):
        input = """
        Function main(){
            g = !Call(foo,[])[5,6] - 1.e-9 &&True;
            }
        """
        expect = Program([
            FuncDecl(Id("main"),[],
                     [
                         Assign(Id("g"),
                                BinaryOp("&&",
                                         BinaryOp('-',
                                                  UnaryOp("!",
                                                          ArrayAccess(CallExpr(Id("foo"),[]),[NumberLiteral(5.0),NumberLiteral(6.0)])
                                                          ),
                                                  NumberLiteral(1.e-9)
                                                  ),
                                         BooleanLiteral(True)
                                         ),

                                )
                     ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test90(self):
        input="""
        Let a = 10;
        Function main(){
            Call(foo,[a{"Khoan"}[12]{"name"}])[1]{"class"} = a{123}[1]{"Khoan"}; 
        }
        """
        expect=Program(
            [
                VarDecl(Id("a"),[],NoneType(),NumberLiteral(10.0)),
                FuncDecl(Id("main"),[],
                         [
                             Assign(
                                 JSONAccess(
                                      ArrayAccess(
                                          CallExpr(
                                              Id("foo"),
                                              [
                                                  JSONAccess(
                                                      ArrayAccess(
                                                          JSONAccess(
                                                              Id("a"),
                                                              [StringLiteral("Khoan")]
                                                          )
                                                          ,
                                                      [NumberLiteral(12.0)]
                                                      )
                                                      ,
                                                  [StringLiteral("name")]
                                                  )
                                              ]
                                          )
                                          ,
                                            [NumberLiteral(1.0)]
                                      )
                                     ,
                                    [StringLiteral("class")]
                                 )

                                 ,
                                 JSONAccess(
                                     ArrayAccess(
                                         JSONAccess(Id("a"),
                                                    [NumberLiteral(123.0)]
                                                    ),
                                         [NumberLiteral(1.0)]
                                     ),
                                     [StringLiteral("Khoan")]
                                 )
                             )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test91(self):
        input="""
        Function main(a[1,2,"Khoan"],b,n){
            Let a[1,2]:JSON =[{name:"Khoan",class:[{age:18},{faculty:"KHMT",arr:[1,2,3]}]},{}];
            a[0]{"class"}[1]{"arr"}[0] = 10;
        }
        """
        expect = Program(
            [
                FuncDecl(Id("main"),
                         [
                             VarDecl(Id("a"),[NumberLiteral(1.0),NumberLiteral(2.0),StringLiteral("Khoan")],NoneType(),None),
                             VarDecl(Id("b"),[],NoneType(),None),
                             VarDecl(Id("n"),[],NoneType(),None)
                         ],
                         [
                             VarDecl(Id("a"),[NumberLiteral(1.0),NumberLiteral(2.0)],JSONType(),
                                     ArrayLiteral(
                                         [
                                             JSONLiteral(
                                                 [
                                                     (Id("name"),StringLiteral("Khoan")),
                                                     (Id("class"),
                                                        ArrayLiteral(
                                                            [
                                                                JSONLiteral([(Id("age"),NumberLiteral(18.0))]),
                                                                JSONLiteral(
                                                                    [
                                                                        (Id("faculty"),StringLiteral("KHMT")),
                                                                        (Id("arr"),ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0)]))
                                                                    ]
                                                                )
                                                            ]
                                                        )
                                                      )
                                                 ]
                                             ),
                                             JSONLiteral([])
                                         ]
                                     )
                                     ),
                             Assign(
                                 ArrayAccess(
                                     JSONAccess(
                                         ArrayAccess(
                                             JSONAccess(
                                                 ArrayAccess(
                                                     Id("a")
                                                     ,
                                                 [NumberLiteral(0.0)]
                                                 )
                                                 ,
                                             [StringLiteral("class")]
                                             )
                                             ,
                                         [NumberLiteral(1.0)]
                                         )
                                         ,
                                     [StringLiteral("arr")]
                                     )
                                     ,
                                 [NumberLiteral(0.0)]
                                 )
                                 ,
                             NumberLiteral(10.0)
                             )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test92(self):
        input = """
        Function main(a[1,2,"Khoan"],b,n){
            Let a[1,2]:JSON =[{name:"Khoan",class:[{age:18},{faculty:"KHMT",arr:[1,2,3]}]},{}];
            a[0]{"class"}[1]{"arr"}[0] = a{"class"}{"arr"}[1] + a[2,2,3]{"faculty"};
        }
        """
        expect = Program([
            FuncDecl(Id("main"),
                     [
                         VarDecl(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0), StringLiteral("Khoan")], NoneType(),
                                 None),
                         VarDecl(Id("b"), [], NoneType(), None),
                         VarDecl(Id("n"), [], NoneType(), None)
                     ],
                     [
                         VarDecl(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0)], JSONType(),
                                 ArrayLiteral(
                                     [
                                         JSONLiteral(
                                             [
                                                 (Id("name"), StringLiteral("Khoan")),
                                                 (Id("class"),
                                                  ArrayLiteral(
                                                      [
                                                          JSONLiteral([(Id("age"), NumberLiteral(18.0))]),
                                                          JSONLiteral(
                                                              [
                                                                  (Id("faculty"), StringLiteral("KHMT")),
                                                                  (Id("arr"), ArrayLiteral(
                                                                      [NumberLiteral(1.0), NumberLiteral(2.0),
                                                                       NumberLiteral(3.0)]))
                                                              ]
                                                          )
                                                      ]
                                                  )
                                                  )
                                             ]
                                         ),
                                         JSONLiteral([])
                                     ]
                                 )
                                 ),
                         Assign(
                             ArrayAccess(
                                 JSONAccess(
                                     ArrayAccess(
                                         JSONAccess(
                                             ArrayAccess(
                                                 Id("a")
                                                 ,
                                                 [NumberLiteral(0.0)]
                                             )
                                             ,
                                             [StringLiteral("class")]
                                         )
                                         ,
                                         [NumberLiteral(1.0)]
                                     )
                                     ,
                                     [StringLiteral("arr")]
                                 )
                                 ,
                                 [NumberLiteral(0.0)]
                             )
                             ,

                             BinaryOp("+",
                                      ArrayAccess(
                                              JSONAccess(
                                                  Id("a")
                                                  ,
                                                  [StringLiteral("class"),StringLiteral("arr")]
                                              )
                                          ,
                                          [NumberLiteral(1.0)]
                                      )
                                      ,
                                          JSONAccess(
                                              ArrayAccess(
                                                  Id("a")
                                                  ,
                                                  [NumberLiteral(2.0),NumberLiteral(2.0),NumberLiteral(3.0)]
                                              )
                                              ,
                                              [StringLiteral("faculty")]
                                          )
                                      )
                         )
                     ]
                     )
        ])
        self.assertTrue((TestAST.checkASTGen(input,expect,392)))

    def test93(self):
        input = """
        Function main(a[1,2,"Khoan"],b,n){
            Let a[1,2]:JSON =[{name:"Khoan",class:[{age:18},{faculty:"KHMT",arr:[1,2,3]}]},{}];
            a[0]{"class"}[1]{"arr"}{"arr"}[0] = a{"class"}{"arr"}[1] + a[2,2,3]{"faculty"};
        }
        """
        expect = Program([
            FuncDecl(Id("main"),
                     [
                         VarDecl(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0), StringLiteral("Khoan")], NoneType(),
                                 None),
                         VarDecl(Id("b"), [], NoneType(), None),
                         VarDecl(Id("n"), [], NoneType(), None)
                     ],
                     [
                         VarDecl(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0)], JSONType(),
                                 ArrayLiteral(
                                     [
                                         JSONLiteral(
                                             [
                                                 (Id("name"), StringLiteral("Khoan")),
                                                 (Id("class"),
                                                  ArrayLiteral(
                                                      [
                                                          JSONLiteral([(Id("age"), NumberLiteral(18.0))]),
                                                          JSONLiteral(
                                                              [
                                                                  (Id("faculty"), StringLiteral("KHMT")),
                                                                  (Id("arr"), ArrayLiteral(
                                                                      [NumberLiteral(1.0), NumberLiteral(2.0),
                                                                       NumberLiteral(3.0)]))
                                                              ]
                                                          )
                                                      ]
                                                  )
                                                  )
                                             ]
                                         ),
                                         JSONLiteral([])
                                     ]
                                 )
                                 ),
                         Assign(
                             ArrayAccess(
                                 JSONAccess(
                                     ArrayAccess(
                                         JSONAccess(
                                             ArrayAccess(
                                                 Id("a")
                                                 ,
                                                 [NumberLiteral(0.0)]
                                             )
                                             ,
                                             [StringLiteral("class")]
                                         )
                                         ,
                                         [NumberLiteral(1.0)]
                                     )
                                     ,
                                     [StringLiteral("arr"),StringLiteral("arr")]
                                 )
                                 ,
                                 [NumberLiteral(0.0)]
                             )
                             ,

                             BinaryOp("+",
                                      ArrayAccess(
                                              JSONAccess(
                                                  Id("a")
                                                  ,
                                                  [StringLiteral("class"),StringLiteral("arr")]
                                              )
                                          ,
                                          [NumberLiteral(1.0)]
                                      )
                                      ,
                                          JSONAccess(
                                              ArrayAccess(
                                                  Id("a")
                                                  ,
                                                  [NumberLiteral(2.0),NumberLiteral(2.0),NumberLiteral(3.0)]
                                              )
                                              ,
                                              [StringLiteral("faculty")]
                                          )
                                      )
                         )
                     ]
                     )
        ])
        self.assertTrue((TestAST.checkASTGen(input,expect,393)))

    def test94(self):
        input = """
        Function main(a[1,2,"Khoan"],b,n){
            Let a[1,2]:JSON =[{name:"Khoan",class:[{age:18},{faculty:"KHMT",arr:[1,2,3]}]},{}];
            a[0]{"class" +. "arr"}[1+2]{"arr"}{"arr"}[0] = a{"class"}{"arr"}[1] + a[2,2,3]{"faculty"};
        }
        """
        expect = Program([
            FuncDecl(Id("main"),
                     [
                         VarDecl(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0), StringLiteral("Khoan")], NoneType(),
                                 None),
                         VarDecl(Id("b"), [], NoneType(), None),
                         VarDecl(Id("n"), [], NoneType(), None)
                     ],
                     [
                         VarDecl(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0)], JSONType(),
                                 ArrayLiteral(
                                     [
                                         JSONLiteral(
                                             [
                                                 (Id("name"), StringLiteral("Khoan")),
                                                 (Id("class"),
                                                  ArrayLiteral(
                                                      [
                                                          JSONLiteral([(Id("age"), NumberLiteral(18.0))]),
                                                          JSONLiteral(
                                                              [
                                                                  (Id("faculty"), StringLiteral("KHMT")),
                                                                  (Id("arr"), ArrayLiteral(
                                                                      [NumberLiteral(1.0), NumberLiteral(2.0),
                                                                       NumberLiteral(3.0)]))
                                                              ]
                                                          )
                                                      ]
                                                  )
                                                  )
                                             ]
                                         ),
                                         JSONLiteral([])
                                     ]
                                 )
                                 ),
                         Assign(
                             ArrayAccess(
                                 JSONAccess(
                                     ArrayAccess(
                                         JSONAccess(
                                             ArrayAccess(
                                                 Id("a")
                                                 ,
                                                 [NumberLiteral(0.0)]
                                             )
                                             ,
                                             [BinaryOp("+.",StringLiteral("class"),StringLiteral("arr"))]
                                         )
                                         ,
                                         [BinaryOp("+",NumberLiteral(1.0),NumberLiteral(2.0))]
                                     )
                                     ,
                                     [StringLiteral("arr"),StringLiteral("arr")]
                                 )
                                 ,
                                 [NumberLiteral(0.0)]
                             )
                             ,

                             BinaryOp("+",
                                      ArrayAccess(
                                              JSONAccess(
                                                  Id("a")
                                                  ,
                                                  [StringLiteral("class"),StringLiteral("arr")]
                                              )
                                          ,
                                          [NumberLiteral(1.0)]
                                      )
                                      ,
                                          JSONAccess(
                                              ArrayAccess(
                                                  Id("a")
                                                  ,
                                                  [NumberLiteral(2.0),NumberLiteral(2.0),NumberLiteral(3.0)]
                                              )
                                              ,
                                              [StringLiteral("faculty")]
                                          )
                                      )
                         )
                     ]
                     )
        ])
        self.assertTrue((TestAST.checkASTGen(input,expect,394)))

    def test95(self):
        input="""
        Function main(){
            Let a;
            true{True}{False} = "Khoan"{True} + [1,2,2]{2} + {name:"Khoan"}[1,2,3];
            }
        """
        expect =Program([
            FuncDecl(Id("main"),[],
                     [
                         VarDecl(Id("a"),[],NoneType(),None),
                         Assign(
                             JSONAccess(Id("true"),[BooleanLiteral(True),BooleanLiteral(False)])
                             ,
                             BinaryOp("+",
                                BinaryOp("+",
                                    JSONAccess(StringLiteral("Khoan"),[BooleanLiteral(True)])
                                         ,
                                    JSONAccess(ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(2.0)]),[NumberLiteral(2.0)])
                                         ),
                                    ArrayAccess(JSONLiteral([(Id("name"),StringLiteral("Khoan"))]),[NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0)])
                                )
                            )
                     ]
                     )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test96(self):
        input="""
        Function main(){
            Let a;
            true{True}{False} = "Khoan"{True} + [1,2,2]{2} + (-1+{name:"Khoan"})[1,2,3];
            }
        """
        expect = Program([
            FuncDecl(Id("main"), [],
                     [
                         VarDecl(Id("a"), [], NoneType(), None),
                         Assign(
                             JSONAccess(Id("true"), [BooleanLiteral(True), BooleanLiteral(False)])
                             ,
                             BinaryOp("+",
                                      BinaryOp("+",
                                               JSONAccess(StringLiteral("Khoan"), [BooleanLiteral(True)])
                                               ,
                                               JSONAccess(ArrayLiteral(
                                                   [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(2.0)]),
                                                          [NumberLiteral(2.0)])
                                               ),
                                      ArrayAccess(BinaryOp("+",UnaryOp("-",NumberLiteral(1.0)),JSONLiteral([(Id("name"), StringLiteral("Khoan"))])),
                                                  [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)])
                                      )
                         )
                     ]
                     )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test97(self):
        input="""
        Function main(){
            Let a;
            Call(main,[]){True}{False} = Call(main,[]){True} + [1,2,2]{2} + (-1+{name:"Khoan"})[1,2,3];
            }
        """
        expect = Program([
            FuncDecl(Id("main"), [],
                     [
                         VarDecl(Id("a"), [], NoneType(), None),
                         Assign(
                             JSONAccess(CallExpr(Id("main"),[]), [BooleanLiteral(True), BooleanLiteral(False)])
                             ,
                             BinaryOp("+",
                                      BinaryOp("+",
                                               JSONAccess(CallExpr(Id("main"),[]), [BooleanLiteral(True)])
                                               ,
                                               JSONAccess(ArrayLiteral(
                                                   [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(2.0)]),
                                                          [NumberLiteral(2.0)])
                                               ),
                                      ArrayAccess(BinaryOp("+",UnaryOp("-",NumberLiteral(1.0)),JSONLiteral([(Id("name"), StringLiteral("Khoan"))])),
                                                  [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)])
                                      )
                         )
                     ]
                     )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test98(self):
        input="""
        Function test_json(arr[1000],n){
            Let x = {
                        name: "Khoan",
                        age: 45,
                        married: True,
                        children: ["A", "B"],
                        pets: [ "Dog","cat" ],
                        cars: [
                            {model: "Audi A1", mpg: 15.1},
                            {model: "Lamborghini", mpg: 18.1}
                        ]
                        };
        }
        """
        expect = Program(
            [
                FuncDecl(Id("test_json"),
                         [
                            VarDecl(Id("arr"),[NumberLiteral(1000.0)],NoneType(),None),
                            VarDecl(Id("n"),[],NoneType(),None)
                         ],
                         [
                             VarDecl(Id("x"),[],NoneType(),
                                     JSONLiteral(
                                         [
                                             (Id("name"),StringLiteral("Khoan")),
                                             (Id("age"),NumberLiteral(45.0)),
                                             (Id("married"), BooleanLiteral(True)),
                                             (Id("children"),ArrayLiteral([StringLiteral("A"),StringLiteral("B")])),
                                             (Id("pets"), ArrayLiteral([StringLiteral("Dog"), StringLiteral("cat")])),
                                             (
                                                 Id("cars"),ArrayLiteral(
                                                     [
                                                         JSONLiteral([
                                                             (Id("model"),StringLiteral("Audi A1")),
                                                             (Id("mpg"),NumberLiteral(15.1))
                                                         ]),
                                                         JSONLiteral([
                                                             (Id("model"), StringLiteral("Lamborghini")),
                                                             (Id("mpg"), NumberLiteral(18.1))
                                                         ])
                                                     ]
                                                 )
                                             )
                                         ]
                                     )
                                     )
                         ]
                         )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test99(self):
        input="""
        Function main(){
            If(a!=0){
                If(a!=0){
                }Elif(a!=0){
                }Else{}   
            }Elif(a!=0){
                If(a!=0){
                }Elif(a!=0){
                }Else{}
            }Else{
                If(a!=0){
                }Elif(a!=0){
                }Else{}
            }
        }
        """
        expect = Program([
                FuncDecl(Id("main"),[],
                         [
                             If(
                                 [
                                     (
                                         BinaryOp("!=",Id("a"),NumberLiteral(0.0)),
                                         [
                                             If(
                                                 [
                                                     (BinaryOp("!=", Id("a"), NumberLiteral(0.0)),[]),
                                                     (BinaryOp("!=", Id("a"), NumberLiteral(0.0)), [])
                                                 ],[]
                                             )
                                         ]
                                     ),
                                     (
                                         BinaryOp("!=", Id("a"), NumberLiteral(0.0)),
                                         [
                                             If(
                                                 [
                                                     (BinaryOp("!=", Id("a"), NumberLiteral(0.0)), []),
                                                     (BinaryOp("!=", Id("a"), NumberLiteral(0.0)), [])
                                                 ], []
                                             )
                                         ]
                                     )
                                 ],
                                 [
                                     If(
                                         [
                                             (BinaryOp("!=", Id("a"), NumberLiteral(0.0)), []),
                                             (BinaryOp("!=", Id("a"), NumberLiteral(0.0)), [])
                                         ], []
                                     )
                                 ]
                             )
                         ]
                         )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))
