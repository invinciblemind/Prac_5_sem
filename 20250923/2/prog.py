m = list(map(int, input().split(',')))
for i in range(len(m) - 1):
    for j in range(i + 1, len(m)):
        if m[i] ** 2 % 100 > m[j] ** 2 % 100:
            m[i], m[j] = m[j], m[i]
print(m)
