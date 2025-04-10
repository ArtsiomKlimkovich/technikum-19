# Zadanie 9
# Napisz program, który wyświetli w osobnych wierszach wszystkie pary liczb bliźniaczych mniejszych
# od 1000.
def isPrime (n):
    if n == 2: return True
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

j = 5
for i in range (7, 1000+1):
    if isPrime(i) and isPrime(j):
        print (i, j)
    i += 2
    j += 2
