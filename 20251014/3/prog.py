w = int(input())
s = input()
word = ''
dct = {}
while len(s) != 1:
    for sym in s:
        if sym.isalpha():
            word += sym.lower()
        else:
            if len(word) == w:
                if word not in dct.keys():
                    dct[word] = 1
                else:
                    dct[word] += 1
            word = ''
    s = input()
max_words = []
max_count = 0
for word in dct.keys():
    if dct[word] > max_count:
        max_count = dct[word]
        max_words = [word]
    elif dct[word] == max_count:
        max_words.append(word)
print(*sorted(max_words))
