# Zadanie 1: Sprawdź czy wpisana przez użytkownika liczba binarna jest parzysta

n = input("Wprowadź liczbę binarną: ")

# Sprawdź ostatni bit liczby binarnej
if n[-1] == "0":
    print("Wpisana liczba jest parzysta.")
else:
    print("Wpisana liczba nie jest parzysta.")
print()

# Zadanie 2: Określ parzystość sumy/różnicy/iloczynu dwóch liczb binarnych

a = input("Wprowadź pierwszą liczbę binarną: ")
b = input("Wprowadź drugą liczbę binarną: ")

# Funkcja sprawdzająca parzystość sumy
def parzystaSuma(a, b):
    suma = int(a, 2) + int(b, 2)  # Konwersja z binarnej na dziesiętną i dodanie
    if suma % 2 == 0:
        print("Suma jest parzysta.")
    else:
        print("Suma nie jest parzysta.")
    print()

# Funkcja sprawdzająca parzystość różnicy
def parzystaRoznica(a, b):
    roznica = abs(int(a, 2) - int(b, 2))  # Konwersja i obliczenie różnicy
    if roznica % 2 == 0:
        print("Różnica jest parzysta.")
    else:
        print("Różnica nie jest parzysta.")
    print()

# Funkcja sprawdzająca parzystość iloczynu
def parzystyIloczn(a, b):
    iloczyn = int(a, 2) * int(b, 2)  # Konwersja i obliczenie iloczynu
    if iloczyn % 2 == 0:
        print("Iloczyn jest parzysty.")
    else:
        print("Iloczyn nie jest parzysty.")
    print()

# Wywołanie funkcji dla podanych liczb binarnych
parzystaSuma(a, b)
parzystaRoznica(a, b)
parzystyIloczn(a, b)
