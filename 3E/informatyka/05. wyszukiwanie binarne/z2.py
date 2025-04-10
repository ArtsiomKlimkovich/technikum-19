def isInList(list, a, left, right):
    if left > right:
        return False
        
    middle = (left  + right) // 2
    
    if list[middle] == a:
        return True
    elif list[middle] < a:
        return isInList(list, a, middle+1, right)
    else:
        return isInList(list, a, left, middle-1)
        
ciag = list(map(int, input("input ciag: ").split(" ")))
a = int(input("input a: "))
n = len(ciag)
if isInList(ciag, a, 1, n):
    print("Tak")
else:
    print("Nie")
