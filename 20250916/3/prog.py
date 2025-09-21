n = int(input())
i = n
while i <= n + 2:
    j = n
    while j <= n + 2:
        s = i * j
        print(i, '*', j, '=', end=' ')
        s_c = 0
        while s > 0:
            s_c += s % 10
            s //= 10
        if s_c == 6:
            print(':=)', end=' ')
        else:
            print(i * j, end=' ')
        j += 1
    print()
    i += 1
