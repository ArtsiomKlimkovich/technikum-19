with open("ciag.txt", "r") as file:
    numbers = list(map(int, file.readline().split()))
    # numbers = [2, 3, -4, 2, -5, 5, 2 -4]
print(numbers)
n = len(numbers)

maxSum = 0
currentSum = 0
for i in range(n):
    currentSum += numbers[i]
    if currentSum < 0:
        currentSum = 0
    else:
        if currentSum > maxSum:
            maxSum = currentSum

print(maxSum)