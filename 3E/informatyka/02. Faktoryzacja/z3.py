# Napisz program, który wczyta liczbę naturalną > 1 z klawiatury i wyświetli komunikat, czy suma
# czynników pierwszych liczby n jest liczbą pierwszą.
n = int (input ("input n: "))

def IfPrime(x):
    if x == 1:
        return False
    for i in range(2, n):
        if x % i == 0:
            return False
    return True

def rozloz (n):
    k = 2
    sum = 0
    while n > 1:
        while n % k == 0:
            sum += k
            n /= k
        k += 1
    if IfPrime(sum):
        print("tak")
    else:
        print("nie")

rozloz(n)