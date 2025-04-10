# Zadanie 4
# Napisz program, który wyświetli ile dzielników ma liczba całkowita dodatnia n
# podana przez użytkownika.
n = int(input("input num: "))
count = 0
for i in range (1, n + 1):
    if n % i == 0:
        count += 1
print (count)