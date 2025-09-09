# Zadanie 4
def dziesietny_na_rzymski_greedy(liczba):
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

liczba = int(input("Podaj liczbę (1–3999): "))
if 1 <= liczba < 4000:
    print(dziesietny_na_rzymski_greedy(liczba))
else:
    print("Liczba spoza zakresu")