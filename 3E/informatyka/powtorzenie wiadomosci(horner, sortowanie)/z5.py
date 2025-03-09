with open("ciag.txt", "r") as file:
    ciag = list(map(int, file.readline().split()))

n = len(ciag)

maxSum = sum(ciag[:3])

for i in range(3, n-3):
    currentSum = sum(ciag[i:i+3])
    maxSum = max(maxSum, currentSum)

print(maxSum)