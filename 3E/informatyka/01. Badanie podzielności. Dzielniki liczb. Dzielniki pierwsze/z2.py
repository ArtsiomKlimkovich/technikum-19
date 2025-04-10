# Zadanie 2
# Napisz program, który wyświetli dzielniki liczby całkowitej dodatniej n
# podanej przez użytkownika.
n = int(input("input num: "))
for i in range (1, n+1):
    if n % i == 0: print (i, end=" ")
print ()
print ()
# version 2
i = 1
while i*i<n:
    if n % i == 0:
        print (i, end = " ")
        print (n // i, end = " ")
    i += 1
if i * i == n:
    print (i)