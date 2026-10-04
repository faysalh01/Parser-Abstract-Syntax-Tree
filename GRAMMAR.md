# Onyx Part 3 – Updated Parser Grammar

The following grammar describes the subset implemented by the Part 3 parser.
The complete Onyx language grammar from Parts 1 and 2 remains the overall
language specification.

<program> ::= { <statement> }

<statement> ::= <assignment>
              | <print-statement>

<assignment> ::= "let" <identifier> "=" <expression> ";"
               | <identifier> "=" <expression> ";"

<print-statement> ::= "print" "(" <expression> ")" ";"

<expression> ::= <term> { ("+" | "-") <term> }

<term> ::= <factor> { ("*" | "/") <factor> }

<factor> ::= <number>
           | <identifier>
           | "(" <expression> ")"

<identifier> ::= [a-zA-Z_] { [a-zA-Z0-9_] }

<number> ::= [0-9] { [0-9] }

The separate <expression>, <term>, and <factor> levels enforce precedence:
multiplication and division bind more tightly than addition and subtraction.
Parentheses allow the normal precedence to be overridden.
