from lexer import lexer
from parser import parser

while True:
    data = input("Enter an HTML tag declaration: ")
    if not data:
        break
    parser.parse(data, lexer=lexer)
