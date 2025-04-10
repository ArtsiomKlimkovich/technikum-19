with open("liczby.txt", "r") as file:
    liczby = list()
    for line in file:
        liczby.append(int(line))

def sortowanie_szybkie(ciag, lewy, prawy):
    pivot = ciag[(lewy + prawy) // 2]
    i = lewy
    j = prawy
    while i <= j:
        while ciag[i] < pivot:
            i += 1
        while ciag[j] > pivot:
            j -= 1
        if i <= j:
            ciag[i], ciag[j] = ciag[j], ciag[i]
            i += 1
            j -= 1

    if lewy < j:
        sortowanie_szybkie(ciag, lewy, j)
    if i < prawy:
        sortowanie_szybkie(ciag, i, prawy)


n = len(liczby)
sortowanie_szybkie(liczby, 0, n - 1)

print(' '.join(map(str, liczby)))