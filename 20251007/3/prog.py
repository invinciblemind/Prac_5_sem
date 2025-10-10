m = []
s0 = input()[:-1]
s = input()[:-1]
gas, liq = 0, 0
w, h = len(s) - 2, 0
while list(set(list(s))) != ['#']:
    h += 1
    if s[1]  == '.':
        gas += len(s) - 2
    else:
        liq += len(s) - 2
    s = input()[:-1]
print('#' * (h + 2))
c_liq = (liq + h - 1) // h
c_gas = w - c_liq
for i in range(c_gas):
    print('#' + '.' * h + '#')
for i in range(c_liq):
    print('#' + '~' * h + '#')
print('#' * (h + 2))
if gas >= liq:
    s0 = '.' * 20 + f' {gas}/{w * h}'
    print(s0)
    s1 = f'{liq}/{w * h}'
    print('~' * round(20 * liq / gas) + f'{s1:>{len(s0) - round(20 * liq / gas)}}')
else:
    s1 = '~' * 20 + f' {liq}/{w * h}'
    s0 = f'{gas}/{w * h}'
    print('.' * round(20 * gas / liq) + f'{s0:>{len(s1) - round(20 * gas / liq)}}')
    print(s1)
