from decimal import Decimal


def esum(N, one):
    n0 = 1
    if type(one) == float:
        e = 1.0
        for i in range(1, N + 1):
            n0 *= i
            e += 1 / n0
    else:
        e = Decimal('1.0')
        for i in range(1, N + 1):
            n0 *= i
            e += Decimal(1 / n0)
    return e


print(esum(100, 1.0))
print(esum(100, Decimal(1)))
