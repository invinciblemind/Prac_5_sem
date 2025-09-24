m = list(map(int, input().split(',')))
mm1, mm2 = [m], []
l = len(m)
for i in range(l - 1):
    mm1.append(list(map(int, input().split(','))))
for i in range(l):
    mm2.append(list(map(int, input().split(','))))
mmx = []
for i in range(l):
    mx = [0] * l
    for j in range(l):
        for k in range(l):
            mx[j] += mm1[i][k] * mm2[k][j]
    mmx.append(mx)
for i in mmx:
    print(','.join(list(map(str, i))))
