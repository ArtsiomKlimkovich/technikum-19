with open('ciagi.txt', 'r') as plik:
    liczba_ciagow = int(plik.readline().strip())
    liczba_parzystych = 0

    for _ in range(liczba_ciagow):
        dane = list(map(int, plik.readline().strip().split()))
        suma = sum(dane[1:])

        if suma % 2 == 0:
            liczba_parzystych += 1

print(f"Liczba ciągów o parzystej sumie wyrazów: {liczba_parzystych}")