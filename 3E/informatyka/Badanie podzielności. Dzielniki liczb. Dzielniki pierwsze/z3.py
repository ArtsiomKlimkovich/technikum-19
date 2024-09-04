# Zadanie 3
# Napisz program, który wyświetli sumę dzielników liczby całkowitej dodatniej n
# podanej przez użytkownika.
n = int(input("input num: "))
sum = 0
for i in range (1, n + 1):
    if n % i == 0:
        sum += i
print (sum)