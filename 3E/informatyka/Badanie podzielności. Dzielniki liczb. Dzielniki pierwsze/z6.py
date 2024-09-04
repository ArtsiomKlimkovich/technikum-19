# Zadanie 6
# Napisz program, który sprawdzi, czy liczby całkowite dodatnie a i b podane przez użytkownika
# są liczbami bliźniaczymi. Liczby całkowite dodatnie są liczbami bliźniaczymi,
# jeżeli są liczbami pierwszymi i ich różnica wynosi 2, np. liczby 5 i 7 oraz 11 i 13
# są liczbami bliźniaczymi, a 7 i 9 nie są bliźniacze, bo 9 nie jest liczbą pierwszą.
def isPrime(n):
    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
    return True
a = int(input ("input a: "))
b = int(input ("input b: "))
def czyBiezoce(a, b):
    return isPrime(a) and isPrime(b) and abs(a - b) == 2
print (czyBiezoce(a, b))