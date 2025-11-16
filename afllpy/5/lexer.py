import ply.lex as lex

# Reserved keywords
reserved = {
    'for': 'FOR',
    'int': 'TYPE'
}

tokens = [
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'ID', 'NUMBER', 'ASSIGN', 'LT', 'SEMICOLON',
    'INCREMENT', 'STREAM'
] + list(reserved.values())

# Simple tokens
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_ASSIGN    = r'='
t_LT        = r'<'
t_SEMICOLON = r';'
t_INCREMENT = r'\+\+'
t_STREAM    = r'<<'

# Identifier or reserved keyword
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignore spaces
t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
