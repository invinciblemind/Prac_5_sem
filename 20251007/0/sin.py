from math import sin

def scale(a, b, A, B, x):
    return A + (x - a) / (b - a) * (B - A)


W, H = eval(input())
A, B = eval(input())
for line in range(0, H):
    x = scale(0, H - 1, A, B, line)
    y = sin(x)
    k = round(scale(-1, 1, 0, W - 1, y))
    print(' ' * k, '*')
