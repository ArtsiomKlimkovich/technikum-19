def oblicz_wielomian_horner(wspolczynniki, x):
    wynik = wspolczynniki[0]
    for wsp in wspolczynniki[1:]:
        wynik = wynik * x + wsp
    return wynik

def horner_rekurencyjnie(wspolczynniki, x, n):
    if n == 0:
        return wspolczynniki[0]
    return wspolczynniki[n] + x * horner_rekurencyjnie(wspolczynniki, x, n - 1)

wspolczynniki = list(map(int, input("Podaj współczynniki wielomianu od a_n do a_0, oddzielone spacjami: ").split()))
x = float(input("Podaj wartość x: "))

wynik_horner = oblicz_wielomian_horner(wspolczynniki, x)
print(f"Wartość wielomianu dla x={x} wynosi (metoda Hornera): {wynik_horner}")

wynik_rekurencyjnie = horner_rekurencyjnie(wspolczynniki, x, len(wspolczynniki) - 1)
print(f"Wartość wielomianu dla x={x} wynosi (metoda rekurencyjna): {wynik_rekurencyjnie}")