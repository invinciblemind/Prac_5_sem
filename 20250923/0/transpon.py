matrix = []
s = input()
while s != '':
    matrix.append(eval(s))
    s = input()
for i in range(len(matrix)):
    for j in range(i + 1, len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for i in matrix:
    print(*i)
