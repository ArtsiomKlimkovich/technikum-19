import random

liczba_liczb = 1000000
liczby = []

pierwsza = random.randint(1, 10)
liczby.append(pierwsza)

for _ in range(1, liczba_liczb):
    nowa_liczba = liczby[-1] + random.randint(1, 3)
    liczby.append(nowa_liczba)

liczba_do_sprawdzenia = 1500000
istnieje = False
liczba_porownan = 0

for liczba in liczby:
    liczba_porownan += 1
    if liczba == liczba_do_sprawdzenia:
        istnieje = True
        break

with open('zadanie6.txt', 'w') as f:
    if istnieje:
        f.write("tak\n")
    else:
        f.write("nie\n")

    f.write(f"Liczba porównań: {liczba_porownan}\n")