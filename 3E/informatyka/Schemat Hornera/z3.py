def horner_rekurencyjnie(wspolczynniki, x, n):
    if n == 0:
        return wspolczynniki[0]
    return wspolczynniki[n] + x * horner_rekurencyjnie(wspolczynniki, x, n - 1)

wejscie = input("Podaj współczynniki wielomianu (od a0 do an) rozdzielone spacjami: ")
wspolczynniki = list(map(float, wejscie.split()))
x = float(input("Podaj wartość x: "))
wynik = horner_rekurencyjnie(wspolczynniki, x, len(wspolczynniki) - 1)
print(f"Wartość wielomianu dla x={x} wynosi: {wynik}")