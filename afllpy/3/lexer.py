import ply.lex as lex

# Reserved words
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'printf': 'PRINTF'
}

# List of token names
tokens = [
    'ID',
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'GT',
    'STRING',
    'SEMICOLON'
] + list(reserved.values())

# Regular expressions for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_GT = r'>'
t_SEMICOLON = r';'

# String literal (like "pos")
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

# Identifier or reserved keyword
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Number literal
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters (spaces, tabs, newlines)
t_ignore = ' \t\n'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build lexer
lexer = lex.lex()
