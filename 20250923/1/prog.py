m, n = eval(input())
print([q for q in range(m, n) if all(q % k != 0 for k in range(2, int(q ** 0.5) + 1))])
