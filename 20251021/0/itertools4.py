import itertools


print(*itertools.starmap(str.__add__, itertools.product('ABCDEFGH', '12345678')))
