with open("ciag.txt", "r") as file:
    numbers = list(map(int, file.readline().split()))
    # numbers = [2, 3, -4, 2, -5, 5, 2 -4]
print(numbers)
n = len(numbers)

maxSum = 0
currentSum = 0
maxStart = 0
currentStart = 0
maxEnd = 1
for i in range(n):
    if currentSum <= 0:
        currentStart = i
        currentSum = numbers[i]
    else:
        currentSum += numbers[i]

    if currentSum > maxSum or (currentSum == maxSum and (i - currentStart < maxEnd - maxStart)):
        maxSum = currentSum
        maxStart = currentStart
        maxEnd = i

print(maxSum)
print(numbers[maxStart:maxEnd + 1])