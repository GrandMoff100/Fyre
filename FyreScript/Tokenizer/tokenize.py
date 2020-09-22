from .tokens import Token
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

            # Declare the variable that represents the current part
            # of the line its analyzing.
            temp_string = ''
            for char in list(line):
                if char != ' ':
                    # If the character isn't a space
                    temp_string += char
                    print(temp_string)
                    # is_token: bool, token_type: str
                    is_token, token_type = Tokenizer.is_token(temp_string)
                    # If the token_string is actually a token.
                    if is_token:
                        # Yield the token object of the token string and reset the token_string.
                        yield self.convert_to_token(temp_string)
                        temp_string = ''
                    else:
                        # Raise a Syntax error.
                        RAISE_ERROR(Syntax_Error(line, line_num))
                else:
                    # Else yield the current potential token string and reset it.
                    yield temp_string
                    temp_string = ''
                print()

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
        # Else return False, and the type (None)
        return False, token_type
