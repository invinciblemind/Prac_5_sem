from math import sin

def scale(a, b, A, B, x):
    return A + (x - a) / (b - a) * (B - A)


W, H = 100, 50
A, B = -5, 5
screen = [[' '] * W for i in range(H)]
for line in range(0, W):
    x = scale(0, W - 1, A, B, line)
    y = sin(x)
    k = round(scale(-1, 1, 0, H - 1, y))
    screen[H - k - 1][line] = '*'
print('\n'.join([''.join(line) for line in screen]))
