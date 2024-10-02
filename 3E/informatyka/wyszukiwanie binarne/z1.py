def isInTable (T, a, n):
    left = 0
    right = n-1
    while left < right:
        middle = (left+right) // 2
        if T[middle] == a:
            return True
        if T[middle] < a:
            left = middle + 1
        else:
            right = middle - 1
    return T[left] == a

nums = list(map(int, input("input sequence: ").split(" ")))
a = int (input ("input a: "))
n = 10
if isInTable(nums, a, n):
    print ("tak")
else:
    print ("nie")
