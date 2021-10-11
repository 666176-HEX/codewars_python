ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

def high(x):
    words = []
    for ch in x.split(' '):
        words.append(sum([ascii_lowercase.find(i)+1 for i in ch]))
    return x.split(' ')[words.index(max(words))]