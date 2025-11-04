def wczytaj_dane_z_pliku(nazwa_pliku):
    with open(nazwa_pliku, 'r') as f:
        nominaly = list(map(int, f.readline().split()))
        kwoty = [int(line.strip()) for line in f.readlines()]
    return nominaly, kwoty


def najmniejsza_liczba_nominalow(kwota, nominaly):
    dp = [kwota + 1] * (kwota + 1)
    dp[0] = 0

    for nominal in nominaly:
        for i in range(nominal, kwota + 1):
            dp[i] = min(dp[i], dp[i - nominal] + 1)

    return dp[kwota] if dp[kwota] <= kwota else -1


nominaly, kwoty = wczytaj_dane_z_pliku("dane.txt")

najmniejsza_liczba = max(kwoty) + 1
wyniki = []

for kwota in kwoty:
    liczba_nominalow = najmniejsza_liczba_nominalow(kwota, nominaly)

    if liczba_nominalow != -1:
        if liczba_nominalow < najmniejsza_liczba:
            najmniejsza_liczba = liczba_nominalow
            wyniki = [kwota]
        elif liczba_nominalow == najmniejsza_liczba:
            wyniki.append(kwota)

for wynik in wyniki:
    print(wynik)