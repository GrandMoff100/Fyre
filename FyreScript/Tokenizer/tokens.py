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
    '^': 'OP'
}

class Token:
    def __init__(self, text: str, type: str, coords):
        self.type = type
        self.text = text
        self.line_index, self.char_index = coords
    
    def __repr__(self):
        return ' '.join(
            [self.type, self.text]
        )
    
    def __str__(self):
        return self.text