# Zadanie 1
# Napisz program, który wczyta liczbę naturalną n&gt;1 z klawiatury i wyświetli czynniki pierwsze liczby n
# w osobnych liniach.
n = int(input ("input n: "))

def rozloz(n):
    k = 2
    while n != 1:
        while n % k == 0:
            print(k)
            n //= k
        k += 1


rozloz(n)