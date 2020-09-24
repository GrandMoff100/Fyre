from FyreScript.Tokenizer.tokenize import Tokenizer

tokenizer = Tokenizer()

open('text.txt', 'w').close()

with open("example.fys", 'r') as fys:
    lines = fys.readlines()

for token in tokenizer.tokenize(lines):
    print(repr(token))