def f(N):
    if N == 0:
        return 0
    return 1 + f(N - 1)


print(f(10))
