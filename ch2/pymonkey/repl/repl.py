from lexer import lexer
from token import token

PROMPT = ">> "


def start():
    while True:
        print(PROMPT, flush=True, end='')
        line = input()
        if not line:
            return
        lex = lexer.Lexer(line)
        while True:
            tok = lex.next_token()
            print(tok, flush=True)
            if tok.type == token.TokenType.EOF:
                break
