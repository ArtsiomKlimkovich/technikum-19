# Zadanie 8
# Napisz program, który sprawdzi, czy liczby całkowite dodatnie a i b podane przez użytkownika są
# liczbami zaprzyjaźnionymi. Liczby całkowite dodatnie a i b są liczbami zaprzyjaźnionymi, jeżeli są
# różne oraz suma dzielników właściwych liczby a jest równa liczbie b oraz suma dzielników właściwych
# liczby b jest równa liczbie a. Program wyświetli jeden z komunikatów „tak” lub „nie”. Przykłady liczb
# zaprzyjaźnionych:
# Dzielniki liczby 284: 1, 2, 4, 71, 142
# Dzielniki liczby 220: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110
# 220 = 1 + 2 + 4 + 71 + 142
# 284 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110
# Kolejna para liczb zaprzyjaźnionych: 1184 i 1210
a = int(input ("input a: "))
b = int(input ("input b: "))

def sumaDzielnikow(n):
    count = 0
    for i in range (1, n):
        if n % i == 0:
            count += i
    return count


if sumaDzielnikow(a) == b and sumaDzielnikow(b) == a:
    print ("tak")
else:
    print ("nie")
