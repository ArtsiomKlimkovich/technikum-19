def binary_search(arr, n):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < n:
            left = mid + 1
        elif arr[mid] > n:
            right = mid - 1
        else:
            return True
    return False

with open('ciagi.txt', 'r') as file:
    for line in file:
        numbers = list(map(int, line.split()))
        numbers.sort()
        if binary_search(numbers, 10):
            print(' '.join(map(str, numbers)))