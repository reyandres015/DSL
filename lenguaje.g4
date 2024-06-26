grammar lenguaje;

prog: stat+;

stat: expr NEWLINE # Expression | NEWLINE # blank;

expr:
	SHOW '(' expr ')'										# printExpr
	| expr op = ('*' | '/') expr							# MulDiv
	| expr op = ('+' | '-') expr							# AddSub
	| expr '^' expr											# Pow
	| matrix ('+' matrix)+									# MatrixAdd
	| matrix ('-' matrix)+									# MatrixSubtract
	| matrix ('*' matrix)+									# MatrixMultiply
	| INVERSE '(' matrix ')'								# MatrixInverse
	| TRANSPOSED '(' matrix ')'								# MatrixTransposed
	| matrix												# idMatrix
	| CADENA												# cadena
	| FLOAT													# float
	| INT													# int
	| ID													# id
	| ID '=' expr											# assign
	| '(' expr ')'											# parens
	| SIN '(' expr ')'										# sin
	| COS '(' expr ')'										# cos
	| TAN '(' expr ')'										# tan
	| expr MOD expr											# Mod
	| RAIZ ('(' expr ')' | '(' expr ',' expr ')')			# raiz
	| IF '(' cond ')' '->' block (ELSE '->' block)?			# conditionalIf
	| FOR '(' ID '=' expr ';' ID '=' expr ')' '->' block	# for
	| WHILE '(' cond ')' '->' block							# while
	| PAINT '(' expr ',' expr ')'							# paint
	| PAINTBALL '(' expr ',' expr ')'						# paintBall
	| PAINTBARS '(' expr ',' expr ')'						# paintBars
	| BROWNIE '(' expr ')'									# paintBrownie
	| LEER '(' expr ')'										# leer
	| ESCRIBIR '(' expr ',' expr ')'						# escribir;

block: '{' NEWLINE (expr NEWLINE)* NEWLINE* '}';

cond:
	expr '<' expr		# lessThan
	| expr '>' expr		# greaterThan
	| expr '<=' expr	# lessEqualThan
	| expr '>=' expr	# greaterEqualThan
	| expr '==' expr	# equal
	| expr '!=' expr	# notEqual
	| cond '&&' cond	# and
	| cond '||' cond	# or
	| '!' cond			# not
	| '(' cond ')'		# parensCond;

IF: 'if';
ELSE: 'else';
SHOW: 'show';

FOR: 'for';
WHILE: 'while';

PAINT: 'paint';
PAINTBALL: 'paintball';
PAINTBARS: 'paintbars';
BROWNIE: 'brownie';

LEER: 'leer';
ESCRIBIR: 'escribir';

matrix: '[' expr (',' expr)* ']';
INVERSE: 'inverse';
TRANSPOSED: 'transposed';

MUL: '*';
DIV: '/';
ADD: '+';
SUB: '-';
SIN: 'sin';
COS: 'cos';
TAN: 'tan';
MOD: '%';
RAIZ: 'root';
CADENA: '"' (~["\r\n])* '"';
ID: [a-zA-Z]+; // Coincide con identificadores
INT: '-'? [0-9]+; // Coincide con enteros
FLOAT: '-'? [0-9]+ '.' [0-9]+; // Coincide con flotantes
NEWLINE:
	'\r'? '\n'; // Retorna nuevas líneas al analizador (es una señal de fin de declaración)
WS: [ \t]+ -> skip; // Ignora los espacios en blanco