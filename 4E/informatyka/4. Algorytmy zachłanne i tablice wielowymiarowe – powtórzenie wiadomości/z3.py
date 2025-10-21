with open("macierz.txt", "r") as f:
    matrix = []
    for line in f:
        line = line.strip()
        if line:
            row = list(map(int, line.split()))
            matrix.append(row)

for row in matrix:
    if len(row) > 4:
        row[2], row[4] = row[4], row[2]

for row in matrix:
    formatted_row = []
    for num in row:
        if 0 <= num <= 9:
            formatted_row.append(f" {num}")
        else:
            formatted_row.append(str(num))
    print(' '.join(formatted_row))