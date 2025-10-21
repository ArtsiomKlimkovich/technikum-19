with open("macierz.txt", "r") as f:
    matrix = [list(map(int, line.strip().split())) for line in f if line.strip()]

if not matrix:
    print("Macierz jest pusta")
else:
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    col_sums = []
    for col in range(num_cols):
        s = 0
        for row in range(num_rows):
            s += matrix[row][col]
        col_sums.append(s)

    max_sum = max(col_sums)
    max_index = col_sums.index(max_sum)

    print(max_sum, max_index)