# Zadanie 3
def dziesietny_na_rzymski(liczba):
    wartosci = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    wynik = ""
    for wartosc, symbol in wartosci:
        while liczba >= wartosc:
            wynik += symbol
            liczba -= wartosc
    return wynik

print(dziesietny_na_rzymski(1293))  # a) MCCXCIII
print(dziesietny_na_rzymski(2189))  # b) MMCLXXXIX
print(dziesietny_na_rzymski(3743))  # c) MMMDCCXLIII
print(dziesietny_na_rzymski(999))   # d) CMXCIX