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
    if a[-1] == b[-1]:
        print("Suma jest parzysta.")
    else:
        print("Suma nie jest parzysta.")
    print()

# Funkcja sprawdzająca parzystość różnicy
def parzystaRoznica(a, b):
    if a[-1] == b[-1]:
        print("Różnica jest parzysta.")
    else:
        print("Różnica nie jest parzysta.")
    print()

# Funkcja sprawdzająca parzystość iloczynu
def parzystyIloczn(a, b):
    if (a[-1] == "1" and b[-1] == "1") or (a[-1] == "0" and b[-1] == "0"):
        print("Iloczyn jest parzysty.")
    else:
        print("Iloczyn nie jest parzysty.")
    print()

# Wywołanie funkcji dla podanych liczb binarnych
parzystaSuma(a, b)
parzystaRoznica(a, b)
parzystyIloczn(a, b)
