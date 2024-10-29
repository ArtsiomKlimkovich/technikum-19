def sito (a, b):
    sum = 0
    count = 0
    primes = [True] * (b+1)
    p = 2
    while p*p <= b:
        if primes[p]:
            for i in range (p*p, b+1, p):
                primes[i] = False
        p += 1
    for i in range (a, b+1):
        if primes[i]:
            print (i, end=" ")
            sum += i
            count += 1
    print ()
    print ("ilosc -", count, "; suma -", sum)

a = int(input("input a: "))
b = int(input("input b: "))
sito(a, b)
