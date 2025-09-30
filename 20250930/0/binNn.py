def binN(n, ones, base=1):
    if n == 0 and ones == 0:
        print(base)
        return 0
    if n > 0 and ones > 0:
        binN(n - 1, ones - 1, base * 2 + 1)
    if n > 0:
        binN(n - 1, ones, base * 2)

m = eval(input())
binN(m[0] - 1, m[1] - 1)
