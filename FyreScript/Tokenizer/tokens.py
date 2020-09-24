LEX_TABLE = {
    ':': 'COLON',
    ',': 'COMMA',
    ';': 'SEMICOLON',
    '[': 'LBRACKET',
    ']': 'RBRACKET',
    '{': 'LCURlY',
    '}': 'RCURLY',
    '+': 'OP',
    '-': 'OP',
    '*': 'OP',
    '/': 'OP',
    '!=': 'LOGIC',
    '==': 'LOGIC',
    '>=': 'LOGIC',
    '>': 'LOGIC',
    '<': 'LOGIC',
    '<=': 'LOGIC',
    '(': 'LPAR',
    ')': 'RPAR',
    '.': 'PERIOD',
    '**': 'OP',
    '//': 'OP',
    '%': 'MOD',
    '\n': 'NEWLINE',
}

class Token:
    def __init__(self, text: str, type: str, line_index: int):
        self.type = type
        self.text = text
        self.line_index = line_index
    
    def __repr__(self):
        return ' '.join(
            [self.type, repr(self.text)]
        )
    
    def __str__(self):
        return self.text