//1913832
grammar CSEL;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options{
	language=Python3;
}

program: (declares)* EOF ;
//Var declare
declares: var_declare|function_declare;
var_declare: normal_declare|const_declare;

normal_declare: LET var_list ';';
var_list: var_part (',' var_part)*;
var_part: var_normal (':' LIT_TYPE)? ('=' exp)?;
var_normal: VAR_IDENTIFIERS ('[' (exp (',' exp)*)? ']')?;
//change NUMBER to exp
const_declare: CONSTANT var_list_const ';';
var_list_const: var_part_const (',' var_part_const)*;
var_part_const: var_const (':' LIT_TYPE)? ('=' exp);
var_const: CON_IDENTIFIERS ('[' (exp (',' exp)*)? ']')?;
//change NUMBER to exp

//var: (CON_IDENTIFIERS|VAR_IDENTIFIERS) ('[' (NUMBER (',' NUMBER)*)? ']')?;
//Function declare
var: var_normal;//|var_const;
function_declare: FUNCTION VAR_IDENTIFIERS parameters func_body;
parameters: '(' (param_list|) ')';
param_list: var ','param_list|var;
func_body: '{' func_body_stm* '}';
func_body_stm: var_declare|stm;

stm: assign_stm|if_stm|for_stm|while_stm|break_stm|continue_stm|call_stm|return_stm;
assign_stm: (VAR_IDENTIFIERS|index_exp|key_exp) '=' exp ';';

index_exp:(VAR_IDENTIFIERS)  index_op ;
index_op: '[' index ']';
index: exp ',' index|exp;

key_exp: (VAR_IDENTIFIERS) key_op;
key_op : ('{' exp '}')|('{' exp '}') key_op;

if_stm: IF '(' exp ')' func_body  stm_else_if* (ELSE func_body)?;
stm_else_if: ELIF '(' exp ')' func_body;

for_stm: for_in|for_of;//type_for func_body ;
//type_for: for_in|for_of;
for_in: FOR VAR_IDENTIFIERS IN (array|VAR_IDENTIFIERS|CON_IDENTIFIERS) func_body;
for_of: FOR VAR_IDENTIFIERS OF (json|VAR_IDENTIFIERS|CON_IDENTIFIERS) func_body;

while_stm: WHILE '(' exp ')' func_body;

break_stm: BREAK ';';

continue_stm: CONTINUE ';';

call_stm: call ';';
call: CALL '(' (VAR_IDENTIFIERS) ',' pass_param ')';
pass_param: '[' (params|) ']';
params:  param ',' params | param;
param: exp;

return_stm: RETURN exp? ';';

exp: exp1 (RELATION_OP_STR|PLUS_OP_STR) exp1|exp1;
exp1: exp2 RELATION_OP exp2|exp2;
exp2: exp2 LOGIC_BINARY_OP exp3|exp3;
exp3: exp3 (PLUS_OP|MINUS_OP) exp4|exp4;
exp4: exp4 MULTIPLYING_OP exp5|exp5;
exp5: LOGICAL_UNARY_OP exp5|exp6;
exp6: MINUS_OP exp6|exp7;
exp7: exp7 (index_operator|key_operator)|exp8;
index_operator: index_op;
key_operator: key_op;
exp8: operands;
operands: '('exp')'|lit|VAR_IDENTIFIERS|CON_IDENTIFIERS|call;


COMMENT: '##' .*? '##' -> skip;

// lit_type: 'Number'|'Boolean'|'Array'|'JSON'|'String';
lit: NUMBER|BOOLEAN|STRINGLIT|json|array;

json: '{' (key_value (',' key_value)*)? '}';
key_value: (VAR_IDENTIFIERS) ':' lit;
//key_value:  value ',' key_value | value;

array: '[' (element (',' element)*)? ']';
element: lit|exp;
//array_part: element ',' array_part |element;

LIT_TYPE: 'Number'|'Boolean'|'Array'|'JSON'|'String';

NUMBER: INT_PART DECIMAL_PART? EXP_PART?;
fragment INT_PART: [0-9]+;
fragment DECIMAL_PART: '.' [0-9]*;
fragment EXP_PART: ('e'|'E')('+'|'-')? [0-9]+;

BOOLEAN: TRUE|FALSE;
fragment TRUE: 'True';
fragment FALSE: 'False';

//IDENTIFIERS: CON_IDENTIFIERS|VAR_IDENTIFIERS;
CON_IDENTIFIERS: ('$') ([A-Z]|[a-z]|'_'|[0-9])+;
VAR_IDENTIFIERS: [a-z] ([A-Z]|[a-z]|'_'|[0-9])*;

RELATION_OP: '=='|'!='|'<'|'>'|'<='|'>=';
LOGIC_BINARY_OP: '&&'|'||';
PLUS_OP: '+';
MINUS_OP: '-';
MULTIPLYING_OP :'*'|'/'|'%';
LOGICAL_UNARY_OP: '!';
PLUS_OP_STR: '+.';
RELATION_OP_STR: '==.';

BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELIF: 'Elif';
ELSE: 'Else';
WHILE: 'While';
FOR: 'For';
OF: 'Of';
IN: 'In';
CALL: 'Call';
RETURN: 'Return';
FUNCTION: 'Function';
LET: 'Let';
CONSTANT: 'Constant';


STR2NUM: 'str2num';
NUM2STR: 'num2str';
STR2BOOL: 'str2bool';
BOOL2STR: 'bool2str';

PRINT: 'print';
PRINTLN: 'printLn';
READ: 'read';

//built_in_func: STR2BOOL|NUM2STR|STR2NUM|BOOL2STR|PRINT|PRINTLN|READ;

STRINGLIT: '"' CHAR_STRING* '"'
{
    y = str(self.text)
	self.text = y[1:-1]
};
fragment CHAR_STRING:  ~[\r\n\\"'] | '\'"'| ('\\' [bftrn'\\]);

SEP: '('|')'|'['|']'|'{'|'}'|':'|';'|','|'.';
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .
    {
    raise ErrorToken(self.text)
    };

UNCLOSE_STRING: '"' CHAR_STRING* ( [\b\t\r\n\f] | EOF)
    {
		text = str(self.text)
		if (text[-1] is '\r') or (text[-1] is '\n') or (text[-1] is '\b') or (text[-1] is '\t') or (text[-1] is '\f'):
			raise UncloseString(text[1:-1])
		else:
			raise UncloseString(text[1:])
	}
	;

ILLEGAL_ESCAPE: '"' CHAR_STRING* ('\\' ~[btnfr'\\] | '\''~["])
    {
        raise IllegalEscape(str(self.text)[1:])
    }
    ;

UNTERMINATED_COMMENT: '##' .*?
    {
        raise UnterminatedComment()
    }
    ;


/*Let a,b,c;
Function main(a,$b){
    Constant $b:Number =20;
    a["hello"] =  a[20,2,2,2];

}
Constant $c:Number = 10;
Let a = { name:"Khoan",
          age:10,
         class:20,
          faculty:{khoa:"CSE",
                   nganh:"KHMT"}
          };
Let arr = [{test:"hello"},{train:12}, [1,2]];

Let a = {
    name: "Yanxi Place",
    address: "Chinese Forbidden City",
    surface: 10.2,
   people: ["Empress Xiaoxianchun", "Yongzheng Emperor"]
};

##Set new value for name in object a##
Function test(){
    Let b: String = a["name"] + a["address"];
    a["name"] = "Qianqing Palace";

}
Function test_if(){
    If(a==0){
        If(b!=0) {
            a=0;
        }
        Elif (b>0) {
            a["name"] = 10;
        }
        Else {
            c = 0;
        }
    }
}

Function test_json(){
    For i In [1,2,3,[1,2,3]]{
        If(b!=0) {
            a=0;
        }
    }
    For j Of {  name:"Khoan",
                class:"KHO2",
                faculty:"CSE",
                age: 20
              } {
      If(b!=0) {
         a=0;
      }
    }
}
Function test_call(){
    Call(foo, [2 + x, 4 / y]);
    Call(goo, []);
    Return 2+x;
}
*/