import ply.yacc as yacc
from lexer import tokens

def p_declaration(p):
    'declaration : TYPE var_list SEMICOLON'
    print(f"✅ Valid Declaration → Type: {p[1]}, Variables: {p[2]}")
    p[0] = ("declaration", p[1], p[2])

def p_var_list_single(p):
    'var_list : ID'
    p[0] = [p[1]]

def p_var_list_multiple(p):
    'var_list : ID COMMA var_list'
    p[0] = [p[1]] + p[3]

def p_error(p):
    print("❌ Syntax error in input!")

parser = yacc.yacc()

