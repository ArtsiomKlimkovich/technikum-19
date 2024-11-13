def oblicz_wielomian(wspolczynniki, x):
    wynik = 0
    for i, wsp in enumerate(wspolczynniki):
        wynik += wsp * (x ** i)
    return wynik

wspolczynniki = list(map(int, input("Podaj współczynniki wielomianu, oddzielone spacjami: ").split()))

x = float(input("Podaj wartość x: "))

wynik = oblicz_wielomian(wspolczynniki, x)

print(f"Wartość wielomianu dla x = {x} wynosi: {wynik}")