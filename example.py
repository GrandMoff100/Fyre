from FyreScript.Tokenizer.tokenize import Tokenizer

tokenizer = Tokenizer()

with open("example.fys", 'r') as fys:
    lines = fys.readlines()

for token in tokenizer.tokenize(lines):
    pass