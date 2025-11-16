## lexer.py
- Implements the lexer (tokenizer) that converts raw source text into a stream of tokens like identifiers, numbers, operators, and keywords, usually using regular expressions and finite automata concepts. ​
- The lexer recognizes lexemes and categorizes them into token types, often attaching values (e.g., converting a digit sequence into an integer) before handing them to the parser.
## parser.py
- Implements the parser that consumes the token stream and checks whether it matches the language grammar, building a parse tree or abstract syntax tree (AST) that represents the program’s structure.​
- Parsers operate at the grammatical level (context-free grammar), unlike lexers which operate at the token/regular-language level, and may use strategies like LL/LR or libraries like PLY/ANTLR.​
## main.py
- Serves as the program’s entry point that ties components together: reads input (file/stdin), initializes the lexer, feeds tokens to the parser, and then triggers subsequent stages (interpretation, code generation, or pretty-printing). ​
-Often handles CLI arguments, error reporting, and orchestrates the pipeline: source → tokens (lexer) → AST (parser) → execute/emit.​

# 1.
(C :Variable Declaration) 
int a, b, c; 
float pi;  
# 2. 
(Python :Function Definition)  
def greet(name):     
    print("Hello", name)  
# 3.
(C : If-else statement) 
if (x > 0) 
{ 
printf("pos");
} 
else 
{ 
printf("non-pos"); 
} 
# 4.
(HTML : Tag Declaration) 
<p>Hello World</p>
# 5.
(C++ : For Loop) 
for (int i = 0; i < 5; i++) 
{     
   cout << i; 
}
