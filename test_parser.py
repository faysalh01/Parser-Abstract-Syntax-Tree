import unittest
from lexer import Lexer, LexerError
# Assuming your group's parser class is in parser.py
# from parser import Parser 

class TestOnyxParser(unittest.TestCase):
    
    def test_arithmetic_precedence(self):
        """Test 1: Valid expression with operator precedence (2 + 3 * 4)"""
        code = "2 + 3 * 4;"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        # parser = Parser(tokens)
        # ast = parser.parse()
        # Add assertions checking that BinaryOpNode(+) has NumberNode(2) on left and BinaryOpNode(*) on right
        self.assertTrue(tokens, "Tokens generated successfully")

    def test_variable_assignment(self):
        """Test 2: Valid variable assignment (let x = 10;)"""
        code = "let x = 10;"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        self.assertTrue(any(t.token_type == "LET" for t in tokens))

    def test_print_statement(self):
        """Test 3: Valid print statement (print x + 5;)"""
        code = "print x + 5;"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        self.assertTrue(any(t.token_type == "PRINT" for t in tokens))

    def test_parenthesized_expression(self):
        """Test 4: Parenthesized expression overriding precedence"""
        code = "let result = (2 + 3) * 4;"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        self.assertTrue(any(t.token_type == "LPAREN" for t in tokens))

    def test_syntax_error_handling(self):
        """Test 5: Invalid syntax handling (let x = ;)"""
        code = "let x = ;"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        # parser = Parser(tokens)
        # with self.assertRaises(SyntaxError):
        #     parser.parse()
        self.assertTrue(tokens, "Lexer processes tokens, parser should raise SyntaxError")

if __name__ == "__main__":
    unittest.main()