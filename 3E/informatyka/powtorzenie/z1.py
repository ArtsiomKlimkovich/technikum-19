# Napisz program, który wyświetli ile jest liczb pierwszych w pliku liczby1.txt
f = open ("liczby1.txt", "r")

def isPrime (n):
    if n == 2:
        return True
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

primeCount = 0
for x in f:
    if isPrime(int(x)):
        primeCount += 1
print (primeCount)