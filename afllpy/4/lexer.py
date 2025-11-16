import ply.lex as lex

# List of token names
tokens = (
    'OPEN_TAG',
    'CLOSE_TAG',
    'TEXT'
)

# Token definitions
def t_OPEN_TAG(t):
    r'<[a-zA-Z][a-zA-Z0-9]*>'
    # extract tag name only (e.g., from "<p>" → "p")
    t.value = t.value[1:-1]
    return t

def t_CLOSE_TAG(t):
    r'</[a-zA-Z][a-zA-Z0-9]*>'
    # extract tag name only (e.g., from "</p>" → "p")
    t.value = t.value[2:-1]
    return t

def t_TEXT(t):
    r'[^<]+'
    t.value = t.value.strip()
    return t

# Ignore whitespace between tokens
t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

