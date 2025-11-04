def wczytaj_nominaly_z_pliku(nazwa_pliku):
    with open(nazwa_pliku, 'r') as f:
        return list(map(int, f.readline().split()))


def najmniejsza_liczba_nominalow(k, nominaly):
    dp = [k + 1] * (k + 1)
    dp[0] = 0

    for nominal in nominaly:
        for i in range(nominal, k + 1):
            dp[i] = min(dp[i], dp[i - nominal] + 1)

    return dp[k] if dp[k] <= k else -1


nominaly = wczytaj_nominaly_z_pliku("nominaly.txt")
k = int(input("Podaj kwotę reszty k do wydania: "))
wynik = najmniejsza_liczba_nominalow(k, nominaly)

if wynik != -1:
    print(wynik)
else:
    print("Nie można wydać tej kwoty.")