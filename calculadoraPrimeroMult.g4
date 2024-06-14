grammar calculadoraPrimeroMult;

prog: stat+;

stat:
	expr NEWLINE			# printExpr
	| ID '=' expr NEWLINE	# assign
	| NEWLINE				# blank;

expr:
	expr op = ('*' | '/') expr						# MulDiv
	| expr op = ('+' | '-') expr					# AddSub
	| matrix '+' matrix ('+' matrix)*				# MatrixAdd
	| matrix										# idMatrix
	| FLOAT											# float
	| INT											# int
	| ID											# id
	| '(' expr ')'									# parens
	| SIN '(' expr ')'								# sin
	| COS '(' expr ')'								# cos
	| TAN '(' expr ')'								# tan
	| expr MOD expr									# Modh
	| RAIZ ('(' expr ')' | '(' expr ',' expr ')')	# raiz;

matrix: '[' expr (',' expr)* ']';

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
INT: [0-9]+; // Coincide con enteros
FLOAT: [0-9]+ '.' [0-9]+; // Coincide con flotantes
NEWLINE:
	'\r'? '\n'; // Retorna nuevas líneas al analizador (es una señal de fin de declaración)
WS: [ \t]+ -> skip; // Ignora los espacios en blanco