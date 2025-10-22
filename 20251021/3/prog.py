from itertools import product


print(*filter(lambda x: x.count('TOR') == 2, list(map(lambda y: ''.join(y), list(product('ORT', repeat=int(input())))))), sep = ', ')
