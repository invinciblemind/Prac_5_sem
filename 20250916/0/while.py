a = int(input())
n = 0
i = 1
while a != 0:
    if a == i:
        n += 1
    i += 1
    a = int(input())
print(n)
