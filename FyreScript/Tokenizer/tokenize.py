from .tokens import Token


class Tokenizer:
    def __init__(self):
        pass

    def tokenize(self, lines):
        for line in Tokenizer.clear_empty_lines(lines):
            print(line)
            temp_string = ''
            print(*list(line), sep=',')
            for char in list(line):
                if char != ' ':
                    temp_string += char
                    is_token, token_type = Tokenizer.is_token(temp_string)
                    if is_token:
                        yield self.convert_to_token(temp_string)
                        temp_string = ''
                    else:
                        yield
                else:
                    yield temp_string
                    temp_string = ''

    def convert_to_token(self, token_string: str):
        pass

    @staticmethod
    def clear_empty_lines(lines):
        for line in lines:
            if not(line == '\n' or ' ' * len(line) == line):
                yield line

    @staticmethod
    def is_token(potential_token: str):
        token_attrs = [obj for obj in Token().__dict__.values()]
        token_methods = [method for method in token_attrs if callable(method)]
        is_methods = [method for method in token_methods if method.__name__.startswith('_is_')]

        token_type = None
        for is_method in is_methods:
            if is_method(potential_token):
                token_type = is_method.__name__.replace('_is_', '', 1)
                return True, token_type
        return False, token_type
