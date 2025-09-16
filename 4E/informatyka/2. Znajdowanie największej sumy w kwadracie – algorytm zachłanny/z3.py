def algorytm_zachlanny(M):
    n = len(M)
    m = len(M[0])
    suma = 0
    i, j = 0, 0
    while i < n and j < m:
        suma += M[i][j]
        if i + 1 < n and j + 1 < m:
            if M[i + 1][j] > M[i][j + 1]:
                i += 1
            else:
                j += 1
        elif i + 1 < n:
            i += 1
        elif j + 1 < m:
            j += 1
        else:
            break
    return suma

M_a = [
    [3, 7, 2, 6, 4],
    [5, 1, 9, 3, 8],
    [6, 2, 4, 7, 1],
    [8, 3, 5, 2, 9],
    [4, 6, 1, 5, 7]
]

M_b = [
    [2, 5, 4, 3, 4],
    [5, 4, 3, 3, 8],
    [4, 3, 4, 8, 2],
    [3, 3, 2, 2, 9],
    [7, 6, 1, 9, 7]
]


for row in M_a:
    print("\t".join(map(str, row)))

suma = algorytm_zachlanny(M_a)
print(f"\nMaksymalna suma: {suma}")

print()

for row in M_b:
    print("\t".join(map(str, row)))

suma = algorytm_zachlanny(M_b)
print(f"\nMaksymalna suma: {suma}")