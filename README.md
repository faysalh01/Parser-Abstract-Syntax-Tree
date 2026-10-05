# Onyx Compiler - Part 3: Parser & Abstract Syntax Tree (AST)

## Project Overview
Part 3 of the Onyx compiler project implements a recursive descent parser that converts tokens from the lexer into a structured Abstract Syntax Tree (AST). It enforces operator precedence (multiplication/division over addition/subtraction), handles variable declarations, assignments, print statements, and catches syntax errors.

## File Structure
- `lexer.py`: Tokenizes the source code string.
- `ast_nodes.py`: Defines AST node classes (`ProgramNode`, `BinaryOpNode`, `NumberNode`, etc.) and tree traversal.
- `GRAMMAR.md`: Contains the updated EBNF grammar specifications.
- `AST_OUTPUT.txt`: Contains captured AST outputs for required test programs.
- `test_parser.py`: Unit test suite for the parser and error handling.

## How to Run Tests
To execute the test suite, run the following command in your terminal:
```bash
python -m unittest test_parser.py