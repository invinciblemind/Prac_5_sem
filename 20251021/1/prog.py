def fib(m, n):
    lst = [1, 1]
    for i in range(m + n - 2):
        lst.append(lst[-1] + lst[-2])
    for i in range(m, m + n):
        yield lst[i]


import sys
exec(sys.stdin.read())
