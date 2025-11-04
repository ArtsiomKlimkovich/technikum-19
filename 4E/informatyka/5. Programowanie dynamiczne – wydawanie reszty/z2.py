def wczytaj_nominaly_z_pliku(nazwa_pliku):
    with open(nazwa_pliku, 'r') as f:
        return list(map(int, f.readline().split()))


def najmniejsza_liczba_nominalow(k, nominaly):
    dp = [k + 1] * (k + 1)
    last_used = [-1] * (k + 1)
    dp[0] = 0

    for nominal in nominaly:
        for i in range(nominal, k + 1):
            if dp[i - nominal] + 1 < dp[i]:
                dp[i] = dp[i - nominal] + 1
                last_used[i] = nominal

    if dp[k] > k:
        return -1, []

    result = []
    while k > 0:
        nominal = last_used[k]
        result.append(nominal)
        k -= nominal

    return dp[-1], result


def policz_nominaly(result):
    liczba_nominalow = {}
    for nominal in result:
        if nominal in liczba_nominalow:
            liczba_nominalow[nominal] += 1
        else:
            liczba_nominalow[nominal] = 1
    return liczba_nominalow


nominaly = wczytaj_nominaly_z_pliku("nominaly.txt")
k = int(input("Podaj kwotę reszty k do wydania: "))
wynik, result = najmniejsza_liczba_nominalow(k, nominaly)

if wynik != -1:
    print(f"Minimalna liczba nominalów: {wynik}")
    liczba_nominalow = policz_nominaly(result)
    for nominal, liczba in liczba_nominalow.items():
        print(f"{liczba}x{nominal}")
else:
    print("Nie można wydać tej kwoty.")