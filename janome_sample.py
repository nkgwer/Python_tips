from janome.tokenizer import Tokenizer

t = Tokenizer()
for token in t.tokenize('すもももももももものうち'):
    print(token)

for token in t.tokenize('すもももももももものうち',wakati=True):
    print(token)

for token in t.tokenize('バスガス爆発'):
    print(token)