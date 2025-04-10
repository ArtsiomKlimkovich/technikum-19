with open('liczby.txt', 'r') as plik:
    liczby = plik.readline().strip().split()

liczby = list(map(int, liczby))

n = len(liczby)

for i in range(n - 4):
    podciag = liczby[i:i + 5]
    suma = sum(podciag)
    print(f"Podciąg: {' '.join(map(str, podciag))}, Suma: {suma}")