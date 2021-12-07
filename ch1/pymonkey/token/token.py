import typing
from enum import Enum


class TokenType(Enum):
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"

    # Identifiers + literals
    IDENT = "IDENT"  # add, foobar, x, y, ...
    INT = "INT"  # 1343456

    # Operators
    ASSIGN = "="
    PLUS = "+"
    MINUS = "-"
    BANG = "!"
    ASTERISK = "*"
    SLASH = "/"

    LT = "<"
    GT = ">"

    EQ = "=="
    NOT_EQ = "!="

    # Delimiters
    COMMA = ","
    SEMICOLON = ";"

    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"

    # Keywords
    FUNCTION = "FUNCTION"
    LET = "LET"
    TRUE = "TRUE"
    FALSE = "FALSE"
    IF = "IF"
    ELSE = "ELSE"
    RETURN = "RETURN"


class Token:
    def __init__(self, type: TokenType, literal: str):
        self.type = type
        self.literal = literal

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "{} {}".format(self.type.name, self.literal)


keywords: typing.Dict[str, TokenType] = {
    "fn": TokenType.FUNCTION,
    "let": TokenType.LET,
    "true": TokenType.TRUE,
    "false": TokenType.FALSE,
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "return": TokenType.RETURN
}


def lookup_indent(ident: str) -> TokenType:
    tok = keywords.get(ident)
    if tok is not None:
        return tok
    return TokenType.IDENT

