import ply.yacc as yacc
from lexer import tokens

def p_function(p):
    'function : DEF ID LPAREN params RPAREN COLON'
    print("✅ Valid Function Definition")

# params can be empty or a list of parameters
def p_params_empty(p):
    'params : '
    p[0] = []

def p_params_nonempty(p):
    'params : ID param_tail'
    p[0] = [p[1]] + p[2]

def p_param_tail_empty(p):
    'param_tail : '
    p[0] = []

def p_param_tail_nonempty(p):
    'param_tail : COMMA ID param_tail'
    p[0] = [p[2]] + p[3]

def p_error(p):
    print("❌ Syntax error!")

parser = yacc.yacc()

