grammar calculadoraPrimeroMult;

prog: stat+;

stat:
	expr NEWLINE			# printExpr
	| ID '=' expr NEWLINE	# assign
	| NEWLINE				# blank;

expr:
	expr op = ('*' | '/') expr		# MulDiv
	| expr op = ('+' | '-') expr	# AddSub
	| FLOAT							# float
	| INT							# int
	| ID							# id
	| '(' expr ')'					# parens
	| SIN '(' expr ')'				# sin
	| COS '(' expr ')'				# cos
	| TAN '(' expr ')'				# tan;

NOT: '!';
INCREMENT: '++';
DECREMENT: '--';

MUL:
	'*'; // Asigna un nombre de token a '*' utilizado anteriormente en la gramática
DIV: '/';
ADD: '+';
SUB: '-';
SIN: 'sin';
COS: 'cos';
TAN: 'tan';
ID: [a-zA-Z]+; // Coincide con identificadores
INT: [0-9]+; // Coincide con enteros
FLOAT: [0-9]+ '.' [0-9]+; // Coincide con flotantes
NEWLINE:
	'\r'? '\n'; // Retorna nuevas líneas al analizador (es una señal de fin de declaración)
WS: [ \t]+ -> skip; // Ignora los espacios en blanco