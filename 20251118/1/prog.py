import sys

b = sys.stdin.buffer.readline()
N = int(b[0])
L = len(b[1:])
lst = []
for i in range(N):
    lst.append(b[1 + i * L // N:1 + (i + 1) * L // N])
lst.sort()
b2 = b[0:1]
for b_i in lst:
    b2 += b_i
sys.stdout.buffer.write(b2)
