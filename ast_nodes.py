# Onyx Abstract Syntax Tree (AST)
# Part 3 - Programming Languages Project

class ASTNode:
    """Base class for all Onyx AST nodes."""
    pass


class ProgramNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"ProgramNode({self.statements!r})"


class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = int(value)

    def __repr__(self):
        return f"NumberNode({self.value})"


class VariableNode(ASTNode):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"VariableNode({self.name!r})"


class BinaryOpNode(ASTNode):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def __repr__(self):
        return (
            f"BinaryOpNode({self.operator!r}, "
            f"{self.left!r}, {self.right!r})"
        )


class AssignmentNode(ASTNode):
    def __init__(self, variable, expression, declaration=True):
        self.variable = variable
        self.expression = expression
        self.declaration = declaration

    def __repr__(self):
        kind = "let" if self.declaration else "assign"
        return f"AssignmentNode({kind!r}, {self.variable!r}, {self.expression!r})"


class PrintNode(ASTNode):
    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return f"PrintNode({self.expression!r})"


def print_ast(node, indent=0):
    """Print the AST in a readable tree format."""
    prefix = " " * indent

    if isinstance(node, ProgramNode):
        print(prefix + "ProgramNode")
        for statement in node.statements:
            print_ast(statement, indent + 2)

    elif isinstance(node, NumberNode):
        print(prefix + f"NumberNode({node.value})")

    elif isinstance(node, VariableNode):
        print(prefix + f"VariableNode({node.name})")

    elif isinstance(node, BinaryOpNode):
        print(prefix + f"BinaryOpNode({node.operator})")
        print_ast(node.left, indent + 2)
        print_ast(node.right, indent + 2)

    elif isinstance(node, AssignmentNode):
        kind = "let" if node.declaration else "assign"
        print(prefix + f"AssignmentNode({kind})")
        print_ast(node.variable, indent + 2)
        print_ast(node.expression, indent + 2)

    elif isinstance(node, PrintNode):
        print(prefix + "PrintNode")
        print_ast(node.expression, indent + 2)
