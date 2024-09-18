# Napisz program, który wyświetli w osobnych wierszach te liczby z pliku liczby2.txt, które mają
# co najmniej 2 różne czynniki pierwsze w rozkładzie na czynniki pierwsze.

f = open ("liczby2.txt", "r")
liczby = list(map(int, f.read().split()))

def isMoreThan2Czynniki(n):
    count = set()
    k = 2
    while n > 1:
        while n % k == 0:
            count.add(k)
            n /= k
        k += 1
    return len (count) >=2

for i in liczby:
    if isMoreThan2Czynniki(i):
        print (i)