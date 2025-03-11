import random

liczby = [random.randint(1, 1000) for _ in range(100)]

min = liczby[0]
maks = liczby[0]
porownania = 0

for liczba in liczby:
    porownania += 1
    if liczba < min:
        min = liczba
    if liczba > maks:
        maks = liczba

print(min, maks)
print(f"Liczba porównań: {porownania}")