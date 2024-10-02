def isInTable(T, a, left, right):
    if left > right:
        return False

    middle = (left + right) // 2

    if T[middle] == a:
        return True
    elif T[middle] < a:
        return isInTable(T, a, middle + 1, right)
    else:
        return isInTable(T, a, left, middle - 1)

nums = list(map(int, input("input sequence: ").split(" ")))
a = int (input ("input a: "))
n = 10
if isInTable(nums, a, 1, len(nums)):
    print ("tak")
else:
    print ("nie")