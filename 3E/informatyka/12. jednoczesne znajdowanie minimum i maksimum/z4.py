import random

liczby = [random.randint(1, 1000) for _ in range(101)]

min = liczby[0]
maks = liczby[0]
porownania = 0

for i in range(1, len(liczby), 2):
    porownania += 1
    if i + 1 < len(liczby):
        if liczby[i] < liczby[i + 1]:
            if liczby[i] < min:
                min = liczby[i]
            if liczby[i + 1] > maks:
                maks = liczby[i + 1]
        else:
            if liczby[i + 1] < min:
                min = liczby[i + 1]
            if liczby[i] > maks:
                maks = liczby[i]
    else:
        if liczby[i] < min:
            min = liczby[i]
        elif liczby[i] > maks:
            maks = liczby[i]

print(min, maks)
print(f"Liczba porównań: {porownania}")