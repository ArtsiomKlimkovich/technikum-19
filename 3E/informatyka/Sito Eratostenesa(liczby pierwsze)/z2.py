# Napisz program w języku Python, który wyświetli liczbę oraz sumę liczb pierwszych mniejszych lub równych n, gdzie
# n jest liczbą naturalną większą od 1, wykorzystując algorytm sita Eratostenesa.
def sito (n):
    sum = 0
    count = 0
    primes = [True] * (n+1)
    p = 2
    while p*p <= n:
        if primes[p]:
            for i in range (p*p, n+1, p):
                primes[i] = False
        p += 1
    for i in range(2, n+1):
        if primes[i]:
            count += 1
            sum += i
    print ("ilosc - ", count, "; suma - ", sum)

n = int(input ("input n: "))
sito(n)
