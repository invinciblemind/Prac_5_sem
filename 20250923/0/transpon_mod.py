matrix = []
while s := input():
    matrix.append(list(eval(s)))
if len(matrix) == len(matrix[0]) and all(len(matrix[i]) == len(matrix[i + 1]) for i in range(len(matrix) - 1)):
    print('matrix is square')
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in matrix:
        print(*i)
else:
    print("matrix isn't square!")
