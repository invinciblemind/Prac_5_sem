def gen(n):
    sm = 0
    for i in range(1, n + 1):
        sm += 1 / (i ** 2)
        yield sm
