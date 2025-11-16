import ply.yacc as yacc
from lexer import tokens

# Grammar rules
def p_if_else(p):
    '''statement : IF LPAREN condition RPAREN block ELSE block'''
    print("✅ Valid if-else statement")

def p_condition(p):
    '''condition : ID GT NUMBER'''
    pass

def p_block(p):
    '''block : LBRACE PRINTF LPAREN STRING RPAREN SEMICOLON RBRACE'''
    pass

def p_error(p):
    print("❌ Syntax error!")

# Build parser
parser = yacc.yacc()

