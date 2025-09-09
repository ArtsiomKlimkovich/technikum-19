# Zadanie 2
def rzymski_na_dziesietny(rzymska):
    wartosci = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
    suma = 0
    poprzednia = 0
    for znak in reversed(rzymska):
        wartosc = wartosci[znak]
        if wartosc < poprzednia:
            suma -= wartosc
        else:
            suma += wartosc
            poprzednia = wartosc
    return suma

print(rzymski_na_dziesietny("MDCCLXXXV"))   # a) 1785
print(rzymski_na_dziesietny("MMCDXCIV"))    # b) 2494
print(rzymski_na_dziesietny("MCXCIII"))     # c) 1193
print(rzymski_na_dziesietny("MMMCXXIII"))   # d) 3123