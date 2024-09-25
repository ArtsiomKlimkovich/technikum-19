# Napisz program w języku Python, który wyświetli liczbę oraz sumę liczb pierwszych mniejszych lub równych n, gdzie
# n jest liczbą naturalną większą od 1, wykorzystując algorytm sita Eratostenesa.
def sito (n):
    czy_pierwsza = []
    for i in range (n+1):
        czy_pierwsza.append(0)
    czy_pierwsza[0] = czy_pierwsza[1] = 1
    i = 2
    while i * i <= n:
        if czy_pierwsza[i] == 0:
            for j in range (i*i, n+1, i):
                czy_pierwsza[j] = 1
        i += 1
    return czy_pierwsza

n = int (input ("input n: "))

pierwsze = sito (n)

sum = 0
for i in range (n + 1):
    if pierwsze[i] == 0:
        sum += i

print (sum)