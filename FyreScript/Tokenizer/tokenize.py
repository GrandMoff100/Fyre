from .tokens import Token, KEYWORDS
from FyreScript.Core.errors.base import RAISE_ERROR, Syntax_Error



class Tokenizer:
    def __init__(self):
        pass

    def tokenize(self, lines):
        line_count = len(lines)
        # Iterate through each line, and line number
        for line, line_num in zip(lines, range(1, line_count + 1)):
            # Check if the line is an empty line
            if Tokenizer.is_empty_line(line):
                # Skips the rest of the current iteration.
                continue
            # Clear newline character at end if there is one.
            if line.endswith('\n'):
                line = line[:-1]
            yield from self.tokenize_line(line, line_num)

    def tokenize_line(self, line, line_num):
        temp_string = ''
        scope = []






    def convert_to_token(self, token_string: str):
        pass

    @staticmethod
    def is_empty_line(line):
        # If the line is just a newline character or full of spaces.
        if not(line == '\n' or ' ' * len(line) == line):
            return False
        else:
            return True

    @staticmethod
    def is_token(potential_token: str):
        # Token object attributes list
        token_attrs = [obj for obj in Token.__dict__.values()]
        # Filters the non-callable attributes of Token
        token_methods = [method for method in token_attrs if callable(method)]
        # Filters the methods that dont start with _is_, in order to get the is <type> methods.
        is_methods = [method for method in token_methods if method.__name__.startswith('_is_')]

        # Checks if any of the is <type> methods are true.
        token_type = None
        for is_method in is_methods:
            if is_method(potential_token):
                # If it is of the type, return True, and the type of the token.
                token_type = is_method.__name__.replace('_is_', '', 1)
                return True, token_type
        for TOKEN in KEYWORDS:
            pass
        return False, token_type
