from lexer import lexer
from parser import parser

while True:
    data = input("Enter a C if-else statement: ")
    if not data:
        break
    parser.parse(data, lexer=lexer)
