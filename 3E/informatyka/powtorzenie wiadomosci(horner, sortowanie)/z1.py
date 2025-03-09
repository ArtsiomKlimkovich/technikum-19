import random
def scal(tab, lewy, srodek, prawy):
    i = lewy
    j = srodek+1
    k = lewy

    while i <= srodek and j <= prawy:
        if tab[i] < tab[j]:
            pom[k] = tab[i]
            i += 1
        else:
            pom[k] = tab[j]
            j += 1
        k += 1

    while i <= srodek:
        pom[k] = tab[i]
        i += 1
        k += 1

    while j <= prawy:
        pom[k] = tab[j]
        j += 1
        k += 1

    for i in range(lewy, prawy+1):
        tab[i] = pom[i]

def sortuj(tab, lewy, prawy):
    if lewy < prawy:
        srodek = (lewy+prawy) // 2
        sortuj(tab, lewy, srodek)
        sortuj(tab, srodek+1, prawy)
        scal(tab, lewy, srodek, prawy)

def losuj_liczby():
    return [random.randint(1, 1000000) for _ in range(1000000)]

liczby = losuj_liczby()

n = len(liczby)
pom = [0] * n
sortuj(liczby, 0, n-1)

with open("wyniki.txt", "w") as file:
    for liczba in liczby:
        file.write(f"{liczba}\n")