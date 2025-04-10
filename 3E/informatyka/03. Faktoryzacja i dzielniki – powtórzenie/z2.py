# Napisz program, który wyświetli w osobnych wierszach te liczby z pliku liczby2.txt, które są
# podzielne przez 2.

f = open ("liczby2.txt", "r")
liczby = list(map(int, f.read().split()))
for x in liczby:
    if int (x) % 2 == 0:
        print (x)