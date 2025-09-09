# Zadanie 1
def wydaj_reszte():
    with open("nominaly.txt", "r") as plik:
        nominaly = list(map(int, plik.readline().split()))

    nominaly.sort(reverse=True)
    kwota = int(input("Podaj kwotę do wydania: "))

    for nom in nominaly:
        ilosc = kwota // nom
        if ilosc > 0:
            print(f"{ilosc}x{nom}")
            kwota -= ilosc * nom


wydaj_reszte()