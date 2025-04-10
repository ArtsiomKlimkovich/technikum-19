with open("liczby.txt", "r") as file:
    liczby = list(map(int, file.readline().split()))

n = len(liczby)

maxLength = 1
currentLength = 1

for i in range(1, n):
    if liczby[i] >= liczby[i-1]:
        currentLength += 1
    else:
        maxLength = max(maxLength, currentLength)
        currentLength = 1

maxLength = max(maxLength, currentLength)
print(maxLength)