import ply.lex as lex

# Reserved keywords
reserved = {
    'def': 'DEF'
}

# Token list
tokens = ['ID', 'LPAREN', 'RPAREN', 'COLON', 'COMMA'] + list(reserved.values())

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_COMMA = r','

# Identifier (check if reserved)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # If it's 'def', make it DEF
    return t

# Ignore spaces, tabs, and newlines
t_ignore = ' \t\n'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
