# Napisz program, który wyświetli liczbę różnych czynników pierwszych liczby n podanej przez
# użytkownika.
n = int (input ("input n: "))

def rozloz (n):
    count = set()
    k = 2
    while n > 1:
        while n % k == 0:
            count.add(k)
            n /= k
        k += 1
    print (len(count))
    return len (count)

rozloz(n)