import random
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

def wylosuj_liczby():
    return [random.randint(1, 1000000) for _ in range(1000000)]

liczby = wylosuj_liczby()

sortuj(liczby, 0, len(liczby) - 1)

with open('wyniki_3.txt', 'w') as file:
    for liczba in liczby:
        file.write(f"{liczba}\n")

print("Proces zakończony. Liczby zostały zapisane do pliku 'wyniki_3.txt'.")