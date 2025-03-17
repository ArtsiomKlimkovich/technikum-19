with open("liczby.txt", "r") as file:
    liczby = [int(line.strip()) for line in file]

def sortowanie_szybkie(ciag):
    n = len(ciag)
    if n < 2:
        return ciag
    pivot = ciag[n // 2]
    lewy = [x for x in ciag if x < pivot]
    srodek = [x for x in ciag if x == pivot]
    prawy = [x for x in ciag if x > pivot]

    print(f"Lewe: {lewy}, Środek: {srodek}, Prawe: {prawy}")

    return sortowanie_szybkie(lewy) + srodek + sortowanie_szybkie(prawy)

posortowane_liczby = sortowanie_szybkie(liczby)
print(f"Posortowane liczby: {posortowane_liczby}")