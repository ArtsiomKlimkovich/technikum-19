# Zadanie 7
# Napisz program, który sprawdzi, czy liczba całkowita dodatnia n podana przez użytkownika jest liczbą
# doskonałą. Liczba doskonała, to taka, która jest równa sumie swoich dzielników właściwych (czyli
# mniejszych od tej liczby). Program wyświetli jeden z komunikatów „tak” lub „nie”. Przykładowe liczby
# doskonałe:
# 6 = 1+2+3
# 28 = 1+2+4+7+14
n = int(input ("input num: "))

count = 0
for i in range (1, n):
    if n % i == 0:
        count += i

if n == count:
    print ("Tak")
else:
    print ("Nie")
