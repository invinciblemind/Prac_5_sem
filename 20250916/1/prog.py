n = int(input())
s = 'A '
if n % 50 == 0:
    s += '+ B - '
elif n % 25 == 0:
    s += '- B + '
else:
    s += '- B - '
if n % 8 == 0:
    s += 'C +'
else:
    s += 'C -'
print(s)
