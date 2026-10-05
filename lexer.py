class LexerError(Exception):
    """Custom error for invalid characters or malformed tokens in Onyx source code."""
    pass


class Token:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        if self.value is not None:
            return f"{self.token_type}({self.value})"
        return self.token_type


class Lexer:
    # Onyx keywords
    KEYWORDS = {
        "let": "LET",
        "print": "PRINT",
        "if": "IF",
        "else": "ELSE",
        "while": "WHILE",
        "def": "DEF",
        "return": "RETURN"
    }

    # Single-character tokens
    SINGLE_CHAR_TOKENS = {
        "+": "PLUS",
        "-": "MINUS",
        "*": "MULTIPLY",
        "/": "DIVIDE",
        "=": "ASSIGN",
        "<": "LESS_THAN",
        ">": "GREATER_THAN",
        "(": "LPAREN",
        ")": "RPAREN",
        "{": "LBRACE",
        "}": "RBRACE",
        "[": "LBRACKET",
        "]": "RBRACKET",
        ",": "COMMA",
        ";": "SEMICOLON"
    }

    def __init__(self, source):
        self.source = source
        self.position = 0
        self.tokens = []

    def current_char(self):
        if self.position >= len(self.source):
            return None
        return self.source[self.position]

    def advance(self):
        self.position += 1

    def peek(self):
        next_position = self.position + 1
        if next_position >= len(self.source):
            return None
        return self.source[next_position]

    def tokenize(self):
        while self.position < len(self.source):
            char = self.current_char()

            # Ignore whitespace
            if char.isspace():
                self.advance()
                continue

            # Identifier or keyword
            if char.isalpha() or char == "_":
                self.read_identifier()
                continue

            # Integer number
            if char.isdigit():
                self.read_number()
                continue

            # Two-character comparison operators
            if char == "=" and self.peek() == "=":
                self.tokens.append(Token("EQUAL_EQUAL"))
                self.advance()
                self.advance()
                continue

            if char == "!" and self.peek() == "=":
                self.tokens.append(Token("NOT_EQUAL"))
                self.advance()
                self.advance()
                continue

            if char == "<" and self.peek() == "=":
                self.tokens.append(Token("LESS_EQUAL"))
                self.advance()
                self.advance()
                continue

            if char == ">" and self.peek() == "=":
                self.tokens.append(Token("GREATER_EQUAL"))
                self.advance()
                self.advance()
                continue

            # Single-character tokens
            if char in self.SINGLE_CHAR_TOKENS:
                token_type = self.SINGLE_CHAR_TOKENS[char]
                self.tokens.append(Token(token_type))
                self.advance()
                continue

            # Invalid character
            raise LexerError(
                f"Lexical error: invalid character '{char}' "
                f"at position {self.position}."
            )

        return self.tokens

    def read_identifier(self):
        start = self.position

        while (
            self.current_char() is not None
            and (
                self.current_char().isalnum()
                or self.current_char() == "_"
            )
        ):
            self.advance()

        value = self.source[start:self.position]

        if value in self.KEYWORDS:
            self.tokens.append(Token(self.KEYWORDS[value]))
        else:
            self.tokens.append(Token("ID", value))

    def read_number(self):
        start = self.position

        while (
            self.current_char() is not None
            and self.current_char().isdigit()
        ):
            self.advance()

        # Check for invalid identifier starting with digits
        # Example: 123var
        if (
            self.current_char() is not None
            and (
                self.current_char().isalpha()
                or self.current_char() == "_"
            )
        ):
            raise LexerError(
                f"Lexical error: invalid identifier starting with "
                f"digits at position {start}."
            )

        value = self.source[start:self.position]
        self.tokens.append(Token("NUMBER", value))


if __name__ == "__main__":
    source_code = "let x = 10 + 5;"
    lexer = Lexer(source_code)

    try:
        tokens = lexer.tokenize()

        for token in tokens:
            print(token)

    except LexerError as error:
        print(error)
