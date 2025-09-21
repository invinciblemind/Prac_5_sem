n = int(input())
s = 0
while n > 0:
    s += n
    if s > 21:
        print(s)
        break
    n = int(input())
else:
    print(n)
