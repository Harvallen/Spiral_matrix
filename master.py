n, m = [int(num) for num in input().split()]                                        # row, col
matrix = [[0] * m for _ in range(n)]
dir_row, dir_col = 0, 1
k = 1
i, j = 0, 0
for _ in range(n * m):
    matrix[i][j] = k
    k += 1
    new_i = i + dir_row
    new_j = j + dir_col
    if (0 <= (new_i) < n) and (0 <= new_j < m) and matrix[new_i][new_j] == 0:
        i = new_i
        j = new_j
    else:
        dir_row, dir_col = dir_col, -dir_row
        i += dir_row
        j += dir_col
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()                                                                         # without ljust



    # no slices