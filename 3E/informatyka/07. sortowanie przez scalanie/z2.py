def scal(tab, left, middle, right):
    temp = [0] * (right - left + 1)
    i = left
    j = middle + 1
    k = 0
    while i <= middle and j <= right:
        if tab[i] < tab[j]:
            temp[k] = tab[i]
            i += 1
        else:
            temp[k] = tab[j]
            j += 1
        k += 1

    while i <= middle:
        temp[k] = tab[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = tab[j]
        j += 1
        k += 1

    for i in range(len(temp)):
        tab[left + i] = temp[i]

def sortuj(tab, left, right):
    if left < right:
        middle = (left + right) // 2
        sortuj(tab, left, middle)
        sortuj(tab, middle + 1, right)
        scal(tab, left, middle, right)

def wczytaj_dane():
    with open('ciagi.txt', 'r') as file:
        ciagi = file.readlines()

    ciag1 = list(map(int, ciagi[0].split()))
    ciag2 = list(map(int, ciagi[1].split()))

    return ciag1, ciag2

ciag1, ciag2 = wczytaj_dane()

polaczony_ciag = ciag1 + ciag2

sortuj(polaczony_ciag, 0, len(polaczony_ciag) - 1)

print("Posortowany ciąg:", ' '.join(map(str, polaczony_ciag)))

with open('wyniki_2.txt', 'w') as file:
    file.write(' '.join(map(str, polaczony_ciag)) + '\n')