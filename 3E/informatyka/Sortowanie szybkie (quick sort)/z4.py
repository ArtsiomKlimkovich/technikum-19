with open("liczby.txt", "r") as file:
    liczby = [int(line.strip()) for line in file]

def sortuj_szybko(d, lewy, prawy):
    if lewy < prawy:
        pivot = d[prawy]
        d[prawy] = d[lewy]
        d[lewy] = pivot
        j = lewy

        for i in range(lewy, prawy):
            if d[i] >= pivot:
                d[i], d[j] = d[j], d[i]
                j += 1

        d[prawy] = d[j]
        d[j] = pivot

        if lewy < j - 1:
            sortuj_szybko(d, lewy, j - 1)

        if j + 1 < prawy:
            sortuj_szybko(d, j + 1, prawy)

print(f"Nieposortowane liczby: {liczby}")

sortuj_szybko(liczby, 0, len(liczby) - 1)

print(f"Posortowane liczby: {liczby}")      
