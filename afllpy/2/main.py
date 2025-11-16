from lexer import lexer
from parser import parser

while True:
    data = input("Enter a Python function header: ")
    if not data:
        break
    parser.parse(data, lexer=lexer)   # <-- pass lexer here

