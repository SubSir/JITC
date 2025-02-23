grammar llvm;

// 程序定义
module: (function | function_declare |  globalvariable | string_declare | typedelcare)* ;

// 类型
type: 'i32' | 'ptr' | 'void' | 'i1';

// 整数
INTEGER: '-'?[0-9]+ ;

// 标签
Label: '.'[a-zA-Z_] [a-zA-Z0-9_]*  ;

// 标识符
Identifier: [a-zA-Z_] [a-zA-Z0-9_]* ;

Privatevariable: '%' Identifier ;

Global_var: '@' (~[@ \r\n(),])+;

// 字符串字面量
StringLiteral: '"' (~["])+ '"';

// 空白符
WS: [ \t\r\n]+ -> skip ;


// 函数声明
function_declare: 'declare' type Global_var '(' types? ')' ;

// 函数定义
function: 'define' type Global_var '(' params? ')' '{' basic_block+ '}' ;

// 自定义类型
typedelcare: Privatevariable '=' 'type' '{' types? '}' ;

// 全局变量声明
globalvariable: Global_var '=' 'global'type (constant|string_constant) ;

// 字符串声明
string_declare: Global_var '=' 'global' '['INTEGER 'x' 'i8' ']' 'c' StringLiteral ;

// 参数列表
params: (parameter (',' parameter)*) ;

types: (type (',' type)*);

// 参数定义
parameter: type Privatevariable | type Global_var | type constant;

// 基本块
basic_block: Label':' instruction+ ;

// 指令
instruction
    : ret
    | call
    | binary_op
    | branch
    | load
    | store
    | getelementptr
    | compare
    | phi
    ;

// 返回指令
ret: 'ret' type value? ;

// 调用指令
call: 'call' type Global_var '(' params? ')' | Privatevariable '=' 'call' type Global_var '(' params ?')';

// 二元操作
binary_op: Privatevariable'=' bin_op type value ','value ;

// 操作符
bin_op: 'add' | 'sub' | 'mul' | 'sdiv' | 'srem' | 'shl' | 'ashr' | 'and' | 'or' | 'xor';

// 跳转指令
branch: 'br' 'label' '%' Label | 'br' 'i1' value ',' 'label' '%' Label ',' 'label' '%' Label ;

// 加载指令
load: Privatevariable '='  'load' type  ',' 'ptr' var ; 

var: (Privatevariable | Global_var);

// 存储指令
store: 'store' type value ',' 'ptr' var ;

// 取指针指令
getelementptr: Privatevariable '=' 'getelementptr' ptrtype ',' 'ptr' var ',' 'i32' value |
 Privatevariable '=' 'getelementptr' ptrtype ',' 'ptr' var ',' 'i32' INTEGER ',' 'i32' value ;

ptrtype:type | Privatevariable;

// 比较指令
compare: Privatevariable '=' 'icmp' cond type value ',' value  ;

cond: 'eq' | 'ne' | 'slt' | 'sgt' | 'sle' | 'sge';

// phi
phi: Privatevariable '=' 'phi' type '[' value ',' '%' Label ']'( ',' '['value ',' '%' Label ']')+;

// 值
value:Privatevariable | constant | Global_var;

// 常量
constant: INTEGER |'null';

string_constant: Global_var;
