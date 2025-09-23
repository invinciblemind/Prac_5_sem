matrix = []
while s := input():
    matrix.append(list(eval(s)))
if all(len(matrix[i]) == len(matrix) for i in range(len(matrix))):
    print('matrix is square')
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in matrix:
        print(*i)
else:
    print("matrix isn't square!")
