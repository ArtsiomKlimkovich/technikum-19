# Zadanie 5
# Napisz program, który wyświetli dzielniki pierwsze liczby całkowitej dodatniej n
# podanej przez użytkownika.
n = int(input("input num: "))
def isPrime(n):
    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
    return True

for i in range (1, n + 1):
    if (n % i == 0 and isPrime(i)):
        print (i, end=" ")