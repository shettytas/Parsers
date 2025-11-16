# Compiler Components Overview

## lexer.py
- Implements the lexer (tokenizer) that converts raw source text into a stream of tokens such as identifiers, numbers, operators, and keywords.
- Uses regular expressions and finite automata concepts.
- Categorizes lexemes into token types and attaches values (e.g., converting digits to integers).
- Output is passed to the parser.

## parser.py
- Consumes tokens from the lexer and checks if they match the language grammar.
- Builds a Parse Tree or Abstract Syntax Tree (AST).
- Works with context-free grammar using LL/LR parsing techniques or tools like PLY/ANTLR.

## main.py
- Entry point of the program.
- Connects the full pipeline:  
  **source → tokens (lexer) → AST (parser) → execute/emit**
- Handles CLI arguments, error reporting, and overall orchestration.

---

# Code Examples

## 1. C: Variable Declaration
```c
int a, b, c;
float pi;
```
## 2.Python: Function Definition 
```c
def greet(name):
    print("Hello", name)
```
## 3.C: If–Else Statement
```c
if (x > 0)
{
    printf("pos");
}
else
{
    printf("non-pos");
}
```
## 4.HTML: Basic Tag
```c
<p>Hello World</p>
```
## 5.C++: For Loop
```c
for (int i = 0; i < 5; i++)
{
    cout << i;
}
```


