import unittest
from lexer import Lexer
from parser import Parser  # Assumes your group's parser file is named parser.py
from ast_nodes import (
    ProgramNode,
    NumberNode,
    VariableNode,
    BinaryOpNode,
    AssignmentNode,
    PrintNode
)

class TestOnyxParser(unittest.TestCase):
    
    def test_operator_precedence(self):
        """1. Operator precedence: 2 + 3 * 4 -> Verify + node is root and * is its right child."""
        lexer = Lexer("2 + 3 * 4;")
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Root statement should be the + BinaryOpNode
        stmt = ast.statements[0]
        self.assertIsInstance(stmt, BinaryOpNode)
        self.assertEqual(stmt.operator, "+")
        
        # Left child of + should be 2
        self.assertIsInstance(stmt.left, NumberNode)
        self.assertEqual(stmt.left.value, 2)
        
        # Right child of + should be the * BinaryOpNode
        self.assertIsInstance(stmt.right, BinaryOpNode)
        self.assertEqual(stmt.right.operator, "*")
        self.assertEqual(stmt.right.left.value, 3)
        self.assertEqual(stmt.right.right.value, 4)

    def test_variable_assignment(self):
        """2. Variable assignment: let x = 10; -> Verify AssignmentNode with VariableNode("x") and NumberNode(10)."""
        lexer = Lexer("let x = 10;")
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        stmt = ast.statements[0]
        self.assertIsInstance(stmt, AssignmentNode)
        self.assertEqual(stmt.variable, "x")
        self.assertIsInstance(stmt.expression, NumberNode)
        self.assertEqual(stmt.expression.value, 10)

    def test_print_statement(self):
        """3. Print statement: print(x + 5); -> Verify PrintNode whose expression is a BinaryOpNode("+", ...)."""
        lexer = Lexer("print(x + 5);")
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        stmt = ast.statements[0]
        self.assertIsInstance(stmt, PrintNode)
        self.assertIsInstance(stmt.expression, BinaryOpNode)
        self.assertEqual(stmt.expression.operator, "+")
        self.assertIsInstance(stmt.expression.left, VariableNode)
        self.assertEqual(stmt.expression.left.name, "x")
        self.assertIsInstance(stmt.expression.right, NumberNode)
        self.assertEqual(stmt.expression.right.value, 5)

    def test_parentheses_precedence(self):
        """4. Parentheses: let result = (2 + 3) * 4; -> Verify + is nested underneath *."""
        lexer = Lexer("let result = (2 + 3) * 4;")
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        stmt = ast.statements[0]
        self.assertIsInstance(stmt, AssignmentNode)
        self.assertEqual(stmt.variable, "result")
        
        # Expression should be BinaryOpNode(*) with left as BinaryOpNode(+)
        expr = stmt.expression
        self.assertIsInstance(expr, BinaryOpNode)
        self.assertEqual(expr.operator, "*")
        
        left_child = expr.left
        self.assertIsInstance(left_child, BinaryOpNode)
        self.assertEqual(left_child.operator, "+")
        self.assertEqual(left_child.left.value, 2)
        self.assertEqual(left_child.right.value, 3)

    def test_syntax_error(self):
        """5. Syntax error: let x = ; -> Verify invalid syntax triggers an exception."""
        lexer = Lexer("let x = ;")
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        
        with self.assertRaises((SyntaxError, Exception)):
            parser.parse()

if __name__ == "__main__":
    unittest.main()