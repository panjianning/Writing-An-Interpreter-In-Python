## Chapter 1: Lexing

``` bash
D:\Writing-An-Interpreter-In-Python\ch1\pymonkey>python lexer_test.py
LET let
IDENT five
ASSIGN =
INT 5
SEMICOLON ;
LET let
IDENT ten
ASSIGN =
INT 10
SEMICOLON ;
LET let
IDENT add
ASSIGN =
FUNCTION fn
LPAREN (
IDENT x
COMMA ,
IDENT y
RPAREN )
LBRACE {
IDENT x
PLUS +
IDENT y
SEMICOLON ;
RBRACE }
SEMICOLON ;
LET let
IDENT result
ASSIGN =
IDENT add
LPAREN (
IDENT five
COMMA ,
IDENT ten
RPAREN )
SEMICOLON ;
BANG !
MINUS -
SLASH /
ASTERISK *
INT 5
SEMICOLON ;
INT 5
LT <
INT 10
GT >
INT 5
SEMICOLON ;
IF if
LPAREN (
INT 5
LT <
INT 10
RPAREN )
LBRACE {
RETURN return
TRUE true
SEMICOLON ;
RBRACE }
ELSE else
LBRACE {
RETURN return
FALSE false
SEMICOLON ;
RBRACE }
INT 10
EQ ==
INT 10
SEMICOLON ;
INT 10
NOT_EQ !=
INT 9
SEMICOLON ;
EOF

```

``` bash
D:\Writing-An-Interpreter-In-Python\ch1\pymonkey>python main.py
>> 1+1
INT 1
PLUS +
INT 1
EOF
>> if (a=1) b = 2+2
IF if
LPAREN (
IDENT a
ASSIGN =
INT 1
RPAREN )
IDENT b
ASSIGN =
INT 2
PLUS +
INT 2
EOF
>>
```

