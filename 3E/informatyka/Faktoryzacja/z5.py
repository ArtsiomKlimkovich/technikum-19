# Napisz program, który sprawdzi, czy liczba naturalna n&gt;1 podana przez użytkownika jest liczbą
# Smitha.
# https://pl.wikipedia.org/wiki/Liczba_Smitha

n = int (input ("input n: "))
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

if (suma(n) == sumOfDigits(n)):
    print ("tak")
else:
    print ("nie")