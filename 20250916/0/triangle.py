a, b, c = eval(input())
print("yes" if (a > 0) and (b > 0) and (c > 0) and (2 * max(a, b, c) < a + b + c) else 'no')
