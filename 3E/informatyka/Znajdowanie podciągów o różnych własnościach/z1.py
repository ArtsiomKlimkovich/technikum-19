with open("liczby.txt", "r") as file:
    liczby = file.readline().strip().split()

n = len(liczby)

for i in range(n):
    for j in range(i + 1, n + 1):
        print(' '.join(liczby[i:j]))