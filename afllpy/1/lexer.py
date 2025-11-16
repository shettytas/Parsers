import ply.lex as lex

# List of token names
tokens = (
    'TYPE',
    'ID',
    'COMMA',
    'SEMICOLON'
)

# Regular expression rules for simple tokens
t_COMMA = r','
t_SEMICOLON = r';'

# 🔧 FIXED: use word boundaries so 'int' isn't matched as an ID
def t_TYPE(t):
    r'\b(int|float|char|double)\b'
    return t

# Identifier rule (must come AFTER t_TYPE)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Ignored characters (spaces, tabs, newlines)
t_ignore = ' \t\n'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
