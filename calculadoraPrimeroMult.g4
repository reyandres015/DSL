grammar calculadoraPrimeroMult;

prog: stat+;

stat: expr NEWLINE # Expression | NEWLINE # blank;

expr:
	SHOW '(' expr ')'								# printExpr
	| expr op = ('*' | '/') expr					# MulDiv
	| expr op = ('+' | '-') expr					# AddSub
	| expr '^' expr									# Pow
	| matrix ('+' matrix)+							# MatrixAdd
	| matrix ('-' matrix)+							# MatrixSubtract
	| matrix ('*' matrix)+							# MatrixMultiply
	| INVERSE '(' matrix ')'						# MatrixInverse
	| TRANSPOSED '(' matrix ')'						# MatrixTransposed
	| matrix										# idMatrix
	| FLOAT											# float
	| INT											# int
	| ID											# id
	| ID '=' expr									# assign
	| '(' expr ')'									# parens
	| SIN '(' expr ')'								# sin
	| COS '(' expr ')'								# cos
	| TAN '(' expr ')'								# tan
	| expr MOD expr									# Mod
	| RAIZ ('(' expr ')' | '(' expr ',' expr ')')	# raiz
	| IF '(' cond ')' '->' block (ELSE '->' block)?	# conditionalIf;

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
ID: [a-zA-Z]+; // Coincide con identificadores
INT: '-'? [0-9]+; // Coincide con enteros
FLOAT: '-'? [0-9]+ '.' [0-9]+; // Coincide con flotantes
NEWLINE:
	'\r'? '\n'; // Retorna nuevas líneas al analizador (es una señal de fin de declaración)
WS: [ \t]+ -> skip; // Ignora los espacios en blanco