from lexer import lexer
from parser import parser

while True:
    data = input("Enter a declaration: ")
    if not data:
        break
    lexer.input(data)
    result = parser.parse(data)
