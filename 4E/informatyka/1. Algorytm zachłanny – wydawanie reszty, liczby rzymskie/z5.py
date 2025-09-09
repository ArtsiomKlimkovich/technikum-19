# Zadanie 5
def rzymski_na_dziesietny_program(rzymska):
    wartosci = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
    suma = 0
    poprzednia = 0
    for znak in reversed(rzymska):
        wartosc = wartosci.get(znak, 0)
        if wartosc < poprzednia:
            suma -= wartosc
        else:
            suma += wartosc
            poprzednia = wartosc
    return suma

rzymska = input("Podaj liczbę rzymską: ").upper()
print(rzymski_na_dziesietny_program(rzymska))