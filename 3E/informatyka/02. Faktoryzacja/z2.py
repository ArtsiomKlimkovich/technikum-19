# Napisz program, który wczyta liczbę naturalną > 1 z klawiatury i wyświetli sumę czynników
# pierwszych tej liczby.

n = int(input ("input n: "))
def suma (n):
    k = 2
    suma = 0
    while n > 1:
        while n % k == 0:
            suma += k
            n /= k
        k += 1
    print(suma)

suma (n)