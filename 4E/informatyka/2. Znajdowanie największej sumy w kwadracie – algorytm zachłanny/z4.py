def wczytaj_macierz(nazwa_pliku):
    with open(nazwa_pliku, "r") as plik:
        return [list(map(int, linia.strip().split())) for linia in plik]

def znajdz_najwieksza_sume(M, n):
    i, j = 0, 0
    suma = M[0][0]
    sciezka = [(0, 0)]

    while i < n - 1 or j < n - 1:
        if i == n - 1:
            j += 1
        elif j == n - 1:
            i += 1
        elif M[i + 1][j] > M[i][j + 1]:
            i += 1
        else:
            j += 1
        suma += M[i][j]
        sciezka.append((i, j))

    return suma, sciezka

M = wczytaj_macierz("macierz.txt")
n = len(M)
suma, sciezka = znajdz_najwieksza_sume(M, n)

print(suma)
for i, j in sciezka:
    print(i, j)
