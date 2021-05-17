import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    def test_1(self):
        input = """
        Let x;
        Function main(){
            x = 10;
            a[3[2==2],5]=2;
            Call(fact,[x]);
        }
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 201))

    def test_2(self):
        input = """
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
        }"""
        self.assertTrue(TestParser.checkParser(input, "successful", 202))

    def test3_var_integer_decimal(self):
        input = """Let a = 1, b=2123, c=0;"""
        self.assertTrue(TestParser.checkParser(input, "successful", 203))

    def test4_var_integer(self):
        input = """Let abc:Number =  1.e+12,    x___asdyz = -0.12E12;"""
        self.assertTrue(TestParser.checkParser(input, "successful", 204))

    def test_5(self):
        input = """Let aaa,    x___asdyz = 1234, x, khoan:String, ne = "Hello";"""
        self.assertTrue(TestParser.checkParser(input, "successful", 205))

    def test_6(self):
        input = """Let abc = "Khoan",    x___asdyz:JSON;"""
        self.assertTrue(TestParser.checkParser(input, "successful", 206))

    def test7_var_json(self):
        input = """Let a:JSON = {name:"Khoan"};"""
        self.assertTrue(TestParser.checkParser(input, "successful", 207))

    def test8_var_integer_oct(self):
        input = """Let adada   =0.121, dadAA__:JSON = {name:"Khoan",age:18};"""
        self.assertTrue(TestParser.checkParser(input, "successful", 208))

    def test9_var_integer_oct2(self):
        input = """Let a:JSON = {aa:10,bb:{a:"name"}},b:Array = [[10,10,10]];"""
        self.assertTrue(TestParser.checkParser(input, "successful", 209))

    def test_10(self):
        input = """Constant $Abc:number = 30;"""
        self.assertTrue(TestParser.checkParser(input, "Error on line 1 col 14: number", 210))

    def test_11(self):
        input = """Let a = 112.0e3, a__2, c=12.e+0;"""
        self.assertTrue(TestParser.checkParser(input, "successful", 211))

    def test_12(self):
        input = """Let a:String = "hello world", a__2:JSON, c:Number=12.e+0;"""
        self.assertTrue(TestParser.checkParser(input, "successful", 212))

    def test_13(self):
        input = """
        Let x:Number,y:Number;
        Function main(x,a[5]){
        }
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 213))

    def test_14(self):
        input = """Let x:Number,y:Number;
        Function main(x,a[3]){
            Let i = 0;
            a[3+Call(foo,[2])] = a[b[2,3]]+4;
        }
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 214))

    def test_15(self):
        input = """
        Function main(x,a[3]){
            Let i:Number=0;
            a[3+Call(foo,[1,2,3])] = a[b[2,3]]+4;
            Return i;
        }
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 215))

    def test_16(self):
        input = """Let a,b,c;
        Function main(a,$b){
            Constant $b:Number =20;
            a["hello"] =  a[20,2,2,2];
        }
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 216))

    def test_17(self):
        input = """Function main(x,a[3],b[2,3,2]){
                Let i:Number = 0;
                a[3+Call(foo,[2])] = a[b[2,3],5]+4;
                x[2][3][3];
        }
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 20: [", 217))

    def test_18(self):
        input = """Function main(x,a[3],b[2,3,2]){
            Let  i=0;
            a[3+Call(foo,[2])] = a[b[2,3]]+4;
            x[2,3,3] = [[1,2,3],[2,3,4,[1,2,3,[3,4]]]];
            }
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 218)
                        )

    def test_19(self):
        input = """Function main(x,a[3],b[2,3,2]){
                    Let d = e[Call(foo,[2]),a[5,Call(foo,[2])]];
                    x[2,3,3] = [1,2,[1,2]];
        }
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 219))

    def test_20(self):
        input = """Function main(x,a[3],b[2,3,3]){
                Let d = e[Call(foo,[2]),a[5,Call(foo,[2])]];
                x[2,3,3] = [1,2,[1,2]];
                a[3+Call(foo,[2])] = a[b[2,3]]+4;
                x[2,3,3] = [[1,2,3],[2,3,4,[1,2,3,[3,4]]]];
                Let x;
            }
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 220))

    def test_21(self):
        input = """Function main(x,a[3],b[2,3,3]){
                Let d = e[Call(foo,[2]),a[5,Call(foo,[2])]];
                x[2,3,3] = [1,2,[1,2]];
                a[3+Call(foo,[2])] = a[b[2,3]]+4;
                x[2,3,3] = [[1,2,3],[2,3,4,[1,2,3,[3,4]]]];
            }
            Let i:Number = 10;
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 221))

    def test_22(self):
        input = """Function main(x,a[3],b[2,3,3]){
                    Let i:Number = 0;
                    a[3+ Call(foo,[2])] = a[b[2,3]]+4;
                    x[2,3,3] = [1,2,[1,2]];
                    d = e[Call(foo,[2]),a[5,Call(foo,[2])]];
                    g = d[4,b[5,5]];
                }
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 222))

    def test_23(self):
        self.assertTrue(
            TestParser.checkParser("""Let b[2,3]:Array = [1,2,[1],[2,3,4],[4,5,6],1,2];""", "successful", 223))

    def test_24(self):
        self.assertTrue(TestParser.checkParser("""Let a[3] = [[]];""", "successful", 224))

    def test_25(self):
        self.assertTrue(TestParser.checkParser("""Let Hello[3] = [[]];""", "H", 225))

    def test_26(self):
        self.assertTrue(TestParser.checkParser("""Let a[3] = If a==2 Then c=2;""", "Error on line 1 col 11: If", 226))

    def test_27(self):
        self.assertTrue(TestParser.checkParser("""Let c, d = 6, e, f;""", "successful", 227))

    def test_28(self):
        self.assertTrue(TestParser.checkParser("""Let m, n[10], $abc;""", "Error on line 1 col 14: $abc", 228))

    def test_29(self):
        self.assertTrue(TestParser.checkParser("""Let a[];""", "successful", 229))

    def test_30(self):
        self.assertTrue(TestParser.checkParser("""Constant A_[0];""", "A", 230))

    def test_31(self):
        input = r"""Function foo(a,b,c){
            Let i:Number = 0;
            Break;
            Continue;
            If (a==0){
                d = a/b[5];
            }
        }
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 231))

    def test_32(self):
        input = r"""Function foo(a[5],b){
            Let i=0;
            While(i<5){
                a[i] = b + 1.0;
                i=i+1;
            }
        }
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 232))

    def test_33(self):
        input = r"""Function foo(a[5],b){
            Let i=0;
            While(i<5){
                a[i] = b + 1.0;
                i=i+1
            }
        }
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 6 col 12: }", 233))

    def test_34(self):
        input = r"""Function foo(a[5],b){
            Let i=0;
            While(i<5){
                a[i] = b + 1.0;
                i=i+1;
                If(i==4){
                    Break;
                }
            }
        }
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 234))

    def test_35(self):
        self.assertTrue(TestParser.checkParser("""Let a[1]=2""", "Error on line 1 col 10: <EOF>", 235))

    def test_36(self):
        self.assertTrue(TestParser.checkParser("""Let: a[1]=2;""", "Error on line 1 col 3: :", 236))

    def test_37(self):
        self.assertTrue(TestParser.checkParser("""Let: a[1]= ;""", "Error on line 1 col 3: :", 237))

    def test_38(self):
        input = """Function fact(x,y){
            z;
        }
                """
        self.assertTrue(TestParser.checkParser(input, "Error on line 2 col 13: ;", 238))

    def test_39(self):
        input = """Function fact(x,y){

        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 239))

    def test_40(self):
        input = """##Set new value for name in object a##
Function test(){
    Let b: String = a["name"] + a["address"];
    a["name"] = "Qianqing Palace";

}
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 240))

    def test_41(self):
        input = """Function main(){
            Let x=10;
            Let y = "string",temp;
            Constant $a[1,2] = [];
            Let z:JSON = {name:"Khoan",age:18};
            temp = y+z["name"];
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 241))

    def test_42(self):
        input = """Function fact(){
            Let a:Number = 10,n:String;
            Let arr:Array = [[1,2,3],[2,[1,2,3]]],js:JSON = {name:"Khoan"};
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 242))

    def test_43(self):
        input = """Function fact(){
            Let a:Number = 10,n:String;
            Let arr:Array = [[1,2,3],[2,[1,2,3]]],js:JSON = {name:"Khoan"};
            For i In arr{
                Call(printLn,[i]);
            }
            }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 243))

    def test_44(self):
        input = """Function fact(x,y){
            Let x +=1,y:Number = 10;
            Let a[5,1] = [],b[1];
        }
                """
        self.assertTrue(TestParser.checkParser(input, "Error on line 2 col 18: +", 244))

    def test_45(self):
        input = """Function fact(a[1,2]){
            Let name:String = "";
            For i Of {name:"Khoan",age:18}{
                Call(printLn,[i]);
            }
            While(name!=""){
                name = Call(read,[]);
            }
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 245))

    def test_46(self):
        input = """Function fact(a[1,2]+12){
            Let name:String = "";
            For i Of {name:"Khoan",age:18}{
                Call(printLn,[i]);
            }
            While(name!=""){
                name = Call(read,[]);
            }
        }
                """
        self.assertTrue(TestParser.checkParser(input, "Error on line 1 col 20: +", 246))

    def test_47(self):
        input = """Function fact(a[1,2];){
            Let name:String = "";
            For i Of {name:"Khoan",age:18}{
                Call(printLn,[i]);
            }
            While(name!=""){
                name = Call(read,[]);
            }
        }
                """
        self.assertTrue(TestParser.checkParser(input, "Error on line 1 col 20: ;", 247))

    def test_48(self):
        input = """Function fact(x[1,2],y){
            Let x=1,y=2;
            Let a[1,5]:Array,b[1];
            a[1,2] = x+y*z; 
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 248))

    def test_49(self):
        input = """Function fact(x[1,2],y){
            Let x=1,y=2;
            Let a[1,5]:Array,b[1];
            a[1,2] = x+y*z; 
            a[1,1] = Call(read,[]);
            b[1] = "String"+ "String";
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 249))

    def test_50(self):
        input = """Function fact(x[1,2],y){
            Let x=1,y=2;
            Let a[1,5]:Array,b[1];
            a[1,2] = x+y*z; 
            a[1,1] = Call(read,[]);
            b[1] = "String"+ "String";
            c = Call(foo,[a[2]*b[1,2]+9]);
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 250))

    def test_51(self):
        input = """Let ar[2,3]=[[5,7,8],[6,2,2]];
                    Let ar[1], ar[1]=[1,1,1], ar, ar[11,2];
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 251))

    def test_52(self):
        input = """Let ar[2,3];
                    Let ar[1], ar[1]=[1,1,1], ar, ar[11,2];
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 252))

    def test_53(self):
        input = r"""Function fact(){
            Let x=1,y=2;
            Let a[2,1],b[1];
            vol = (4.e3/(-3.e-1))*pi*r*r;
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 253))

    def test_54(self):
        input = r"""Function fact(){
            Let x=1,y=2;
            Let a[2,1],b[1];
            vol = (4.e3/(-3.e-1))*pi*r*r;
            result = Call(foo,[a[2]*b[1,2]+9])["hello"]["name"];
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 254))

    def test_55(self):
        input = r"""Function fact(){
            Let x=1,y=2;
            Let a[2,1],b[1];
            vol = (4.e3/(-3.e-1))*pi*r*r;
            result = Call(foo,[a[2]*b[1,2]+9])["hello"]["name"];
            res = -Call(Call(foo,[]),[a[2]*b[1,2]+9]);
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 255))

    def test_56(self):
        input = r"""Function fact(){
            Let x=1,y=2;
            Let a[2,1],b[1];
            vol = (4.e3/(-3.e-1))*pi*r*r;
            result = Call(foo,[a[2]*b[1,2]+9])["hello"]["name"];
            res = result - Call(Call(foo,[]),[a[2]*b[1,2]+9]);
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 256))

    def test_57(self):
        input = r"""Function fact(){
            Let x=1,y=2;
            Let a[2,1],b[1];
            vol = (4.e3/(-3.e-1))*pi*r*r;
            result = Call(foo,[a[2]*b[1,2]+9])["hello"]["name"];
            res = -Call(Call(foo,[]),[a[2]*b[1,2]+9]);
            x = -Call(Call(foo,[]),[]) + arr[2,3,Call(foo,[])];
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 257))

    def test_58(self):
        input = r"""Function fact(){
            Let x=1,y=2;
            Let a[2,1],b[1];
            vol = (4.e3/(-3.e-1))*pi*r*r;
            result = Call(foo,[a[2]*b[1,2]+9])["hello"]["name"];
            res = -Call(Call(foo,[]),[a[2]*b[1,2]+9]);
            x = -Call(Call(foo,[]),[]) + arr[Call(foo,[])]["hello"];
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 258))

    def test_59(self):
        input = r"""Function fact(){
            Let x=1,y=2;
            Let a[2,1],b[1];
            vol = (4.e3/(-3.e-1))*pi*r*r;
            result = Call(foo,[a[2]*b[1,2]+9]);
            x = -Call(Call(foo,[]),[]);
            a[] = 12;
        }
                """
        self.assertTrue(TestParser.checkParser(input, "Error on line 7 col 14: ]", 259))

    def test_60(self):
        input = r"""Function fact(){
            Let x=1,y=2;
            Let a[2,1],b[1];
            vol = (4.e3/(-3.e-1))*pi*r*r;
            x = -Call(foo,[]) + arr[a+9-Call(foo,[3])[3,1]];
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 260))

    def test_61(self):
        input = r"""Function fact(){
            Let x=1,y=2;
            Let a[2,1],b[1];
            vol = (4.e3/(-3.e-1))*pi*r*r;
            g = !Call(foo,[])[5,6] - 1.e-9 &&True;
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 261))

    def test_62(self):
        input = r"""Function fact(){
            Let x=1,y=2;
            Let a[2,1],b[1];
            vol = (4.e3/(-3.e-1))*pi*r*r;
            g = !Call(foo,[[5,6]]);
            Ax = True + False;
        }
                """
        self.assertTrue(TestParser.checkParser(input, "A", 262))

    def test_63(self):
        input = r"""Function test(){
            Let a=0;
            9 = 3*3;
        }
                """
        self.assertTrue(TestParser.checkParser(input, "Error on line 3 col 12: 9", 263))

    def test_64(self):
        input = r"""Function test(){
            Let a=0;
            a = 3*3;
            If(b!=True){}
            If(a==False){}
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 264))

    def test_65(self):
        input = r""" Function countSort(arr[100],n,exp){
            Let output[100];
            Let i,count[10] = [0];
            For i In [1,100]{
                count[(arr[i]/exp)%10] = countcount[(arr[i] / exp) % 10] + 1;
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
        self.assertTrue(TestParser.checkParser(input, "successful", 265))

    def test_66(self):
        input = r"""Function partition(start,end){
            Let size,i,j;
            Let p;
            size = end-start;
            i=1;
            j = size - 1;
            p = start[0];
            While(True){
                While(start[i]<p){
                    If(i==size - 1){
                        Break;
                    }
                }
                While(start[j]>p){
                    If(j==0){
                        Break;
                    }
                }
                If(i>j){
                    Break;
                }
                Call(swap,[start[i],start[j]]);
            }
            Call(swap,[start[0],start[j]]);
            Return start[j];
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 266))

    def test_67(self):
        input = r"""Function read_json(){
            Let data:JSON = {
                            president :  {
                                name :  "Nguyen Duy Hieu" ,
                                age :  "20"
                            }
                        };
            Let str:String = data["President"]["name"] + data["President"]["age"];
            For i Of data{
                Call(print,[i]);
            }
            Return str;
        }
        Function main(){
            Let result = Call(read_json,[]);
            Call(printLn,[result]);
            Return 0;
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 267))

    def test_68(self):
        input = r"""Function tranposeOfMatrix(a[10,10],tranpose[10,10],r,c){
            For i In [0,r]{
                For j In [0,c]{
                    tranpose[j,i] = a[i,j];
                }
            }
            Return tranpose;
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 268))

    def test_69(self):
        input = r"""Function test(arr[100],n){
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
        self.assertTrue(TestParser.checkParser(input, "successful", 269))

    def test_70(self):
        input = r"""Function test_json(arr[1000],n){
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
        self.assertTrue(TestParser.checkParser(input, "successful", 270))

    def test_71(self):
        input = r"""Function bublesort(arr[100],n){
            Let swaped:Boolean = False;
            For i In [0,n-1]{
                For j In [0,n-i-1]{
                    If(arr[j]>arr[j+1]){
                        Call(swap,[arr[j],arr[j+1]]);
                        swaped = True;
                    }
                }
                If(swaped==True){
                    Break;
                }
            }
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 271))

    def test_72(self):
        input = r"""Function test_if(){
            Let a:Number;
            a = Call(read,[]);
            If(a<7){
                Call(printLn,["Child"]);
            }Elif(a>=7&& (a<18)){
                Call(printLn,["Under age"]);
            }
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 272))

    def test_73(self):
        input = r"""Function bublesort(arr[100],n){
            Let swaped:Boolean = False;
            For i In [0,n-1]{
                For j In [0,n-i-1]{
                    If(arr[j]>arr[j+1]){
                        Call(swap,[arr[j],arr[j+1]]);
                        swaped = True;
                    }
                }
                If(swaped==True){
                    Break;
                } Elif
            }
        }
                """
        self.assertTrue(TestParser.checkParser(input, "Error on line 13 col 12: }", 273))

    def test_74(self):
        input = r"""Function fact(n){
            If (n==1){
                Return 1;
            }Else{
                Return n*Call(fact,[n-1]);
            }
            }
            ##
            main
            # tinh n!
            #
            ##
            Function main(){
                Let n:Number;
                n = Call(read,[]);
                Call(printLn,[Call(fact,[n])]);
            }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 274))

    def test_75(self):
        input = r"""Function fact(n){
            If (n==1){
                Return 1;
            }Else{
                Return n*Call(fact,[n-1]);
            } Else{

            }
            }
            ##
            main
            # tinh n!
            #
            ##
            Function main(){
                Let n:Number;
                n = Call(read,[]);
                Call(printLn,[Call(fact,[n])]);
            }
                """
        self.assertTrue(TestParser.checkParser(input, "Error on line 6 col 14: Else", 275))

    def test_76(self):
        input = r"""Function fact(n){
            If (n==1){
                Return 1;
            }Else{
                Return n*Call(fact,[n-1]);
            }
            }
            ##
            main
            # tinh n!
            #
            ##
            Let x:Number;
            Constant $a:Number = 10;
            Function main(){
                Let n:Number;
                n = Call(read,[]);
                Call(printLn,[Call(fact,[n])]);
            }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 276))

    def test_77(self):
        input = r"""Function fact(n[]){
            If (n==1){
                Return 1;
            }Else{
                Return n*Call(fact,[n-1]);
            }
            }
            ##
            main
            # tinh n!
            #
            ##
            Let x:Number;
            Constant $a:Number = 10;
            Function main(){
                Let n:Number;
                n = Call(read,[]);
                Call(printLn,[Call(fact,[n])]);
            }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 277))

    def test_78(self):
        input = r"""Function main(){
                Let n:Number;
                n = Call(read,[]);
                Call(printLn,[Call(fact,[n])])
            }
            """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 12: }", 278))

    def test_79(self):
        input = r"""Function main(){
                Let n:Number;
                n = Call(read,[]);
                Call(printLn,[Call(fact,[n])]);"""
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 47: <EOF>", 279))

    def test_80(self):
        input = r"""Function foo(a[2],b){
            Let i=0;
            While(a[i]>b){
                Call(printLn,[a[i]]);
                i=i+1;
            }
        }
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 280))

    def test_81(self):
        input = r"""Function foo(a[2],b,c[9,]){
            Let i=0;
            While(a[i]>b){
                Call(printLn,[a[i]]);
                i=i+1;
            }
        }
                """
        self.assertTrue(TestParser.checkParser(input, "Error on line 1 col 24: ]", 281))

    def test_82(self):
        input = """Let a = -1, b:JSON={};"""
        self.assertTrue(TestParser.checkParser(input, "successful", 282))

    def test_83(self):
        input = """Let cef =  [1,2],    n_a = 123;"""
        self.assertTrue(TestParser.checkParser(input, "successful", 283))

    def test_84(self):
        input = """Let khoan =; """
        self.assertTrue(TestParser.checkParser(input, "Error on line 1 col 11: ;", 284))

    def test_85(self):
        input = """let x=2;"""
        self.assertTrue(TestParser.checkParser(input, "Error on line 1 col 0: let", 285))

    def test_86(self):
        input = r"""Function ____
                """
        self.assertTrue(TestParser.checkParser(input, "_", 286))

    def test_87(self):
        input = r"""Function add()"""
        self.assertTrue(TestParser.checkParser(input, "Error on line 1 col 14: <EOF>", 287))

    def test_288(self):
        input = r"""Function add(){};
                """
        self.assertTrue(TestParser.checkParser(input, "Error on line 1 col 16: ;", 288))

    def test_89(self):
        input = r"""Let a = 5;
        Let b[2,3] = [[2,3,4],[4,5,6]];
        Let c, d = 6, e, z;
        Let m = 1, n[2] = [   2   ,   3   ];
                """
        self.assertTrue(TestParser.checkParser(input, "successful", 289))

    def test_90(self):
        input = """ Let x= Call(foo,[2]); """
        self.assertTrue(TestParser.checkParser(input, "successful", 290))

    def test_91(self):
        input = r"""##Le Duc Khoan##"""
        self.assertTrue(TestParser.checkParser(input, "successful", 291))

    def test_92(self):
        input = r"""Let nGuyEn, duC, k__Hoa__N, a[1,0], x0; Let continue;"""
        self.assertTrue(TestParser.checkParser(input, "successful", 292))

    def test_93(self):
        input = r"""Let x=0, aBc=0.123, a_i=12, a[1,0] = [[]], x0 = "x";
        Let continue = True; Let break = False;
        Let i = a_i;"""
        self.assertTrue(TestParser.checkParser(input, "successful", 293))

    def test_94(self):
        input = r"""Let ##meant to be empty##;"""
        self.assertTrue(TestParser.checkParser(input, "Error on line 1 col 25: ;", 294))

    def test_95(self):
        input = r"""Let a[-1];"""
        self.assertTrue(TestParser.checkParser(input, "Error on line 1 col 6: -", 295))

    def test_96(self):
        input = r"""Let o = [], o = [["["]]];"""
        self.assertTrue(TestParser.checkParser(input, "Error on line 1 col 23: ]", 296))

    def test_97(self):
        input = r"""Let a[1,3,3,777,1];"""
        self.assertTrue(TestParser.checkParser(input, "successful", 297))

    def test_98(self):
        input = r"""Let x = -2e3;"""
        self.assertTrue(TestParser.checkParser(input, "successful", 298))

    def test_99(self):
        input = r"""Constant $a = 10;
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
        self.assertTrue(TestParser.checkParser(input, "successful", 299))

    def test_100(self):
        input = r"""Function foo(a[5], b) {
            Let i = 0;
            While (i < 5) {
                Let u: Number = i + 1;
                a[i] = b + 1;
                If (a[u] == 10) {
                    Return a[i];
                    }
                }
            Return -1;
            }"""
        self.assertTrue(TestParser.checkParser(input, "successful", 300))
