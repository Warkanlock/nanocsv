import re

def tokenize(query):
    tokens = []
    token_specification = [
        ('ADD', r'add'),          # 'add' keyword
        ('REMOVE', r'remove'),    # 'remove' keyword
        ('SEARCH', r'search'),    # 'search' keyword
        ('ROW', r'row'),          # 'row' keyword
        ('NUMBER', r'\d+'),       # Integer
        ('COLON', r':'),          # Colon ':'
        ('COMMA', r','),          # Comma ','
        ('VALUE', r'[^,\s]+'),    # Any sequence except comma and whitespace
        ('SKIP', r'\s+'),         # Skip over spaces
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    for mo in re.finditer(tok_regex, query):
        kind = mo.lastgroup
        value = mo.group()
        if kind != 'SKIP':
            tokens.append((kind, value))
    return tokens
