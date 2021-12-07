from token import token


class Lexer:
    def __init__(self, input: str, position: int = 0, read_position: int = 0, ch: str = ''):
        """
        :param input:
        :param position: current position in input (points to current char)
        :param read_position: current reading position in input (after current char)
        :param ch: current char under examination
        """
        self.input = input
        self.position = position
        self.read_position = read_position
        self.ch = ch
        self.read_char()

    def read_char(self):
        if self.read_position >= len(self.input):
            self.ch = ""
        else:
            self.ch = self.input[self.read_position]
        self.position = self.read_position
        self.read_position += 1

    def skip_whitespace(self):
        while self.ch in (' ', '\t', '\n', '\r'):
            self.read_char()

    def peak_char(self) -> str:
        if self.read_position >= len(self.input):
            return ''
        else:
            return self.input[self.read_position]

    def next_token(self) -> token.Token:
        self.skip_whitespace()
        if self.ch == '=':
            # next char is =, recognized as token '=='
            if self.peak_char() == '=':
                self.read_char()
                tok = token.Token(type=token.TokenType.EQ, literal='==')
            else:
                tok = token.Token(type=token.TokenType.ASSIGN, literal='=')
        elif self.ch == '+':
            tok = token.Token(token.TokenType.PLUS, self.ch)
        elif self.ch == '-':
            tok = token.Token(token.TokenType.MINUS, self.ch)
        elif self.ch == '*':
            tok = token.Token(token.TokenType.ASTERISK, self.ch)
        elif self.ch == '/':
            tok = token.Token(token.TokenType.SLASH, self.ch)
        elif self.ch == '<':
            tok = token.Token(token.TokenType.LT, self.ch)
        elif self.ch == '>':
            tok = token.Token(token.TokenType.GT, self.ch)
        elif self.ch == ',':
            tok = token.Token(token.TokenType.COMMA, self.ch)
        elif self.ch == ';':
            tok = token.Token(token.TokenType.SEMICOLON, self.ch)
        elif self.ch == '{':
            tok = token.Token(token.TokenType.LBRACE, self.ch)
        elif self.ch == '}':
            tok = token.Token(token.TokenType.RBRACE, self.ch)
        elif self.ch == '(':
            tok = token.Token(token.TokenType.LPAREN, self.ch)
        elif self.ch == ')':
            tok = token.Token(token.TokenType.RPAREN, self.ch)
        elif self.ch == '!':
            if self.peak_char() == '=':
                self.read_char()
                tok = token.Token(token.TokenType.NOT_EQ, '!=')
            else:
                tok = token.Token(token.TokenType.BANG, self.ch)
        elif self.ch == '':
            tok = token.Token(token.TokenType.EOF, '')
        else:
            if self.is_letter(self.ch):
                literal = self.read_identifier()
                tok = token.Token(token.lookup_indent(literal), literal)
                # must return, already call readchar in read_identifier
                return tok
            elif self.is_digit(self.ch):
                literal = self.read_number()
                tok = token.Token(token.TokenType.INT, literal)
                return tok
            else:
                tok = token.Token(token.TokenType.ILLEGAL, self.ch)
        self.read_char()
        return tok

    @staticmethod
    def is_letter(ch) -> bool:
        return ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or (ch == '_')

    @staticmethod
    def is_digit(ch) -> bool:
        return '0' <= ch <= '9'

    def read_number(self) -> str:
        position = self.position
        while self.is_digit(self.ch):
            self.read_char()
        return self.input[position:self.position]

    def read_identifier(self) -> str:
        position = self.position
        while self.is_letter(self.ch):
            self.read_char()
        return self.input[position:self.position]
