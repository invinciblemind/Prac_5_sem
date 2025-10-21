from itertools import *


def gen():
    sm = 0
    i = 1
    while True:
        sm += 1 / (i ** 2)
        yield sm
        i += 1

print(list(islice(dropwhile(lambda x: x <= 1.6, gen()), 10)))
