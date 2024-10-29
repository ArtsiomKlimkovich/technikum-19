def isInList(list, a, n):
    left = 0
    right = n-1
    while left < right:
        middle = (left + right) // 2
        if list[middle] == a:
            return True
        if list[middle] < a:
            left = middle + 1
        else:
            right = middle - 1
        return list[left] == a
        
ciag = list(map(int, input("input ciag: ").split(" ")))
a = int(input ("input a: "))
n = len(ciag)
if isInList(ciag, a, n):
    print("Tak")
else:
    print("Nie")
