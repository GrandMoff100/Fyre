from .tokens import Token, LEX_TABLE, STRING_INDICATORS
from FyreScript.Core.errors.base import RAISE_ERROR, Syntax_Error
import time

def is_string(text):
    for indicator in STRING_INDICATORS:
        if text.startswith(indicator) and text.endswith(indicator):
            return True
    return False



class Tokenizer:
    def __init__(self):
        pass

    def tokenize(self, lines):
        line_count = len(lines)
        # Iterate through each line, and line number
        for line, line_num in zip(lines, range(1, line_count + 1)):
            # Check if the line is an empty line
            if not Tokenizer.is_empty_line(line):
                yield from self.tokenize_line(line, line_num)

    def tokenize_line(self, line, line_num):
        temp_string = ''
        previous_char = None

        def previous_token(string, y):
            _type = 'NAME'
            _type = _type if string not in LEX_TABLE else LEX_TABLE[string]
            _type = 'NUMBER' if string.isdecimal() else _type
            _type = 'STRING' if is_string(string) else _type
            yield Token(
                    string, 
                    _type, 
                    y
                )
        
        for char in list(line):
            if char in LEX_TABLE:
                if temp_string != '':
                    yield from previous_token(temp_string, line_num)
                    temp_string = ''
                
                yield Token(
                    char, 
                    LEX_TABLE[char],
                    line_num
                )
            elif char == ' ':
                if temp_string != '':
                    yield from previous_token(temp_string, line_num)
                    temp_string = ''
            else:
                temp_string += char
        if temp_string != '':
            yield from previous_token(temp_string, line_num)

    

            
        
            

    @staticmethod
    def is_empty_line(line):
        # If the line is just a newline character or full of spaces.
        if not(line == '\n' or ' ' * len(line) + '\n' == line):
            return False
        else:
            return True