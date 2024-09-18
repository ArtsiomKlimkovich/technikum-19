# Napisz program, który wyświetli liczbę z pliku liczby2.txt, która ma największą sumę
# dzielników pierwszych. Jest tylko jedna taka liczba.

f = open ("liczby2.txt", "r")
liczby = list(map(int, f.read().split()))

def isPrime (n):
    if n == 2: return True
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

def sumaPrimeDzielnikow (n):
    sum = 0
    for i in range (1, n):
        if isPrime(i) and n % i == 0:
            sum += i
    return sum

maxNumSum = liczby[0]
maxNum = 0
for i in liczby:
    if sumaPrimeDzielnikow(i) > maxNumSum:
        maxNumSum = sumaPrimeDzielnikow(i)
        maxNum = i

print (maxNum)