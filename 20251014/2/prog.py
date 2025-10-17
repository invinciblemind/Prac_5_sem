from math import *


s = input()[:-1].split(' ')
c = 0
st = {'quit'}
dct = {'quit': ['s.format(x, y)', None, {'s':''}]}
while True:
    if s[0][0] == ':':
        dct[s[0][1:]] = [s[-1], None, {i:0 for i in s[1:-1]}]
        c += 1
        st.add(s[0][1:])
    else:
        if len(dct[s[0]][2]) == 1:
            s = [s[0], ' '.join(s[1:])]
        j = 1
        for i in list(dct[s[0]][2].keys()):
            dct[s[0]][2][i] = eval(s[j])
            j += 1
        c += 1
        if s[0] == 'quit':
            dct[s[0]][2]['x'] = len(st)
            dct[s[0]][2]['y'] = c
        print(eval(dct[s[0]][0], dct[s[0]][1], dct[s[0]][2]))
        if s[0] == 'quit':
            break
    s = input()[:-1].split(' ')
