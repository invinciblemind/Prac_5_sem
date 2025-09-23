a, b = eval(input())
for n in range(a, b + 1):
    if n % 2 == 1 and '3' not in str(n):
        print(n)
