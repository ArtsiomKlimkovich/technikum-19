# Napisz program, który wyświetli liczbę z pliku liczby2.txt, która ma najmniejszą sumę cyfr
# wszystkich czynników pierwszych. Jest tylko jedna taka liczba.

f = open ("liczby2.txt", "r")
liczby = list(map(int, f.read().split()))

def suma (n):
    k = 2
    suma = 0
    while n > 1:
        while n % k == 0:
            n /= k
            suma += sumOfDigits(k)
        k += 1
    return suma

def sumOfDigits(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum

sumyCzynnikow = []
for i in liczby:
    sumyCzynnikow.append (suma(i))

minimum = min(sumyCzynnikow)
for i in range (len (liczby)):
    if sumyCzynnikow[i] == minimum:
        print (liczby[i])