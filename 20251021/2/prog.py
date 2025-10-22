from itertools import islice, tee


def slide(seq, n):
    i = 0
    while seq[i:]:
        yield from islice(seq, i, i + n)
        i += 1


import sys
exec(sys.stdin.read())
