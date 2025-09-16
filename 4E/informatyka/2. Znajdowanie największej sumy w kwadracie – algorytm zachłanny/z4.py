def wczytaj_macierz(filename):
    macierz = []
    with open(filename, 'r') as file:
        for line in file:
            macierz.append(list(map(int, line.split())))
    return macierz


def znajdz_maximalna_sume(macierz):
    max_suma = 0
    indeksy = []
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j] > max_suma:
                max_suma = macierz[i][j]
                indeksy = [(i, j)]
            elif macierz[i][j] == max_suma:
                indeksy.append((i, j))
    return max_suma, indeksy


macierz = wczytaj_macierz('macierz.txt')
max_suma, indeksy = znajdz_maximalna_sume(macierz)

print(max_suma)
for i, j in indeksy:
    print(i, j)