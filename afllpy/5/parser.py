import ply.yacc as yacc
from lexer import tokens

# for_loop → FOR ( TYPE ID = NUMBER ; ID < NUMBER ; ID ++ ) { ID << ID ; }

def p_for_loop(p):
    '''for_loop : FOR LPAREN declaration SEMICOLON condition SEMICOLON increment RPAREN LBRACE statement RBRACE'''
    print("✅ Valid C++ For Loop")

def p_declaration(p):
    '''declaration : TYPE ID ASSIGN NUMBER'''
    pass

def p_condition(p):
    '''condition : ID LT NUMBER'''
    pass

def p_increment(p):
    '''increment : ID INCREMENT'''
    pass

def p_statement(p):
    '''statement : ID STREAM ID SEMICOLON'''
    pass

def p_error(p):
    print("❌ Syntax error!")

parser = yacc.yacc()

