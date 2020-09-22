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

        

    @staticmethod
    def is_empty_line(line):
        # If the line is just a newline character or full of spaces.
        if not(line == '\n' or ' ' * len(line) == line):
            return False
        else:
            return True