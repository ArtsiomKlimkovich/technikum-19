def czyDoskonala (n):
    counter = 0
    for i in range (1, n):
        if n % i == 0:
            counter += i
    return counter == n

for i in range (1, 1000):
    if czyDoskonala(i):
        print (i)
