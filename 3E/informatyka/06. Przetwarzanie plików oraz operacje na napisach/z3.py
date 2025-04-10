import random

# a
with open('losowe.txt', 'w') as plik:
    for _ in range(10):
        liczba = random.randint(1, 100)
        plik.write(f"{liczba}\n")

print("Zapisano 10 losowych liczb do pliku losowe.txt.")

# b
with open('losowe.txt', 'r') as plik:
    liczby = [int(linia.strip()) for linia in plik]

suma = sum(liczby)
minimum = min(liczby)
maksimum = max(liczby)
srednia = suma / len(liczby)

print(f"Suma: {suma}")
print(f"Minimum: {minimum}")
print(f"Maksimum: {maksimum}")
print(f"Średnia: {srednia:.2f}")