def scal(tab, left, middle, right):
    i = left
    j = middle + 1
    k = left
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

    for i in range(left, right + 1):
        tab[i] = temp[i]


def sortuj(tab, left, right):
    if left < right:
        middle = (left + right) // 2
        sortuj(tab, left, middle)
        sortuj(tab, middle + 1, right)
        scal(tab, left, middle, right)


ciag = list(map(int, input("Input ciag: ").split(" ")))
n = len(ciag)
temp = [0] * n
sortuj(ciag, 0, n - 1)
print(ciag)