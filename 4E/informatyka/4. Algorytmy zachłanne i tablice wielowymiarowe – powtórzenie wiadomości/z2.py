with open("macierz.txt", "r") as f:
    matrix = [list(map(int, line.strip().split())) for line in f if line.strip()]

rows = len(matrix)
cols = len(matrix[0])

i, j = 0, 0
path = []
total_sum = matrix[i][j]

while i < rows - 1 or j < cols - 1:
    if i == rows - 1:
        j += 1
        path.append('P')
    elif j == cols - 1:
        i += 1
        path.append('D')
    else:
        right = matrix[i][j+1]
        down = matrix[i+1][j]
        if down >= right:
            i += 1
            path.append('D')
        else:
            j += 1
            path.append('P')
    total_sum += matrix[i][j]

print(total_sum)
print(''.join(path))