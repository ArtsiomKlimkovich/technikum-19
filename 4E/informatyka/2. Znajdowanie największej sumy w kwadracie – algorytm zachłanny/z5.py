import random

def generuj_macierz(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

def znajdz_maximalna_sume(macierz):
    max_suma = 0
    indeksy = []

    for i in range(len(macierz)):
        max_wiersz = max(macierz[i])
        max_suma += max_wiersz
        max_index = macierz[i].index(max_wiersz)
        indeksy.append((i, max_index))

    return max_suma, indeksy

def wyswietl_macierz(macierz):
    for wiersz in macierz:
        print("\t".join(map(str, wiersz)))


n = int(input("Podaj liczbę całkowitą n (rozmiar macierzy): "))

macierz = generuj_macierz(n)

print("\nWygenerowana macierz:")
wyswietl_macierz(macierz)

max_suma, indeksy = znajdz_maximalna_sume(macierz)

print("\nNajwiększa suma:", max_suma)
print("Indeksy komórek z największymi wartościami:")
for i, j in indeksy:
    print(i, j)