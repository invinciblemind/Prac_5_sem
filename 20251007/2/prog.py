from math import sin

def scale(a, b, A, B, x):
    return A + (x - a) / (b - a) * (B - A)

m = input().split()
W, H, A, B = map(int, m[:4])
f = m[4]
screen = [[' '] * W for i in range(H)]
mnmx = []
for line in range(0, W):
    x = scale(0, W - 1, A, B, line)
    y = eval(f)
    if mnmx == []:
        mnmx = [y, y]
    else:
        mnmx = [min(mnmx[0], y), max(mnmx[1], y)]
for line in range(0, W):
    x = scale(0, W - 1, A, B, line)
    y = eval(f)
    k = round(scale(round(mnmx[0]), round(mnmx[1]), 0, H - 1, y))
    screen[H - k - 1][line] = '*'
for i in range(H - 1):
    for j in range(W):
        if screen[i][j] == '*':
            if j > 0 and any(screen[k][j - 1] == '*' for k in range(i + 1, H)):
                k = i
                while screen[min(H - 1, k + 1)][j - 1] != '*':
                    k += 1
                    screen[k][j] = '*'
            if j < W - 1 and any(screen[k][j + 1] == '*' for k in range(i + 1, H)):
                k = i
                while screen[min(H - 1, k + 1)][j + 1] != '*':
                    k += 1
                    screen[k][j] = '*'

print('\n'.join([''.join(line) for line in screen]))
