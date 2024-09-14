import re

class TokenType:
    ADD = "ADD"
    REMOVE = "REMOVE"
    SEARCH = "SEARCH"
    ROW = "ROW"
    NUMBER = "NUMBER"
    COLON = "COLON"
    COMMA = "COMMA"
    VALUE = "VALUE"
    SKIP = "SKIP"

def tokenize(query):
    tokens = []
    token_specification = [
        (TokenType.ADD, r'add'),          # 'add' keyword
        (TokenType.REMOVE, r'remove'),    # 'remove' keyword
        (TokenType.SEARCH, r'search'),    # 'search' keyword
        (TokenType.ROW, r'row'),          # 'row' keyword
        (TokenType.NUMBER, r'\d+'),       # Integer
        (TokenType.COLON, r':'),          # Colon ':'
        (TokenType.COMMA, r','),          # Comma ','
        (TokenType.VALUE, r'[^,\s]+'),    # Any sequence except comma and whitespace
        (TokenType.SKIP, r'\s+'),         # Skip over spaces
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    for mo in re.finditer(tok_regex, query):
        kind = mo.lastgroup
        value = mo.group()
        if kind != TokenType.SKIP:
            tokens.append((kind, value))
    return tokens
