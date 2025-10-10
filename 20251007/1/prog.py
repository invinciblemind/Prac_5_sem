from fractions import Fraction


m = list(map(Fraction, input().split(', ')))
s = m[0]
w = m[1]
del m[0]
del m[0]
i = 0
num = Fraction(0, 1)
denom = Fraction(0, 1)
i = 1
for j in range(int(m[0]), -1, -1):
    num += m[i] * s ** j
    i += 1
st = i
i += 1
for j in range(int(m[st]), -1, -1):
    denom += m[i] * s ** j
    i += 1
print(denom != 0 and num / denom == w)
