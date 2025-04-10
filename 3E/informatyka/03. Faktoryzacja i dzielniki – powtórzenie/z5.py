# Napisz program, który wyświetli liczby z pliku liczby2.txt, które mają najmniejszą sumę
# czynników pierwszych.

f = open ("liczby2.txt", "r")
liczby = list(map(int, f.read().split()))

def isPrime (n):
    if n == 2: return True
    for i in range (2, n):
        if n % i == 0:
            return False
    return True


def sumaCzynnikowPierwszych (n):
    k = 2
    sum = 0
    while n > 1:
        while n % k == 0:
            sum += k
            n //= k
        k += 1
    return sum

sumyCzynnikow = []
for i in liczby:
    sumyCzynnikow.append (sumaCzynnikowPierwszych(i))

minimum = min(sumyCzynnikow)
for i in range (len (liczby)):
    if sumyCzynnikow[i] == minimum:
        print (liczby[i])