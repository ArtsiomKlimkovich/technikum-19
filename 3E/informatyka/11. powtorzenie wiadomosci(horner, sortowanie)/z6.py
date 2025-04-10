with open("ciag.txt", "r") as file:
    ciag = list(map(int, file.readline().split()))

n = len(ciag)

maxSum = ciag[0]
currentSum = ciag[0]

for i in range(1, n):
    currentSum = max(currentSum, currentSum + ciag[i])

    maxSum = max(currentSum, maxSum)

print(maxSum)