def oblicz_wielomian_horner(wspolczynniki, x):
    wynik = wspolczynniki[0]
    for wsp in wspolczynniki[1:]:
        wynik = wynik * x + wsp
    return wynik


wspolczynniki = list(map(int, input("Podaj współczynniki wielomianu, oddzielone spacjami: ").split()))

x = float(input("Podaj wartość x: "))

wynik = oblicz_wielomian_horner(wspolczynniki, x)

print(f"Wartość wielomianu dla x = {x} wynosi: {wynik}")