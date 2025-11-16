import ply.yacc as yacc
from lexer import tokens

# Grammar:
# element : OPEN_TAG TEXT CLOSE_TAG
def p_element(p):
    'element : OPEN_TAG TEXT CLOSE_TAG'
    if p[1] == p[3]:
        print("✅ Valid HTML Tag Declaration")
    else:
        print(f"❌ Tag mismatch: <{p[1]}> ... </{p[3]}>")

def p_error(p):
    print("❌ Syntax error!")

parser = yacc.yacc()

