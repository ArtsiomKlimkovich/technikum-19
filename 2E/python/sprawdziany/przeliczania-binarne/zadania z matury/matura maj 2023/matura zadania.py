# zad 2.1
def iloscBlokow(n):
    count = 1
    for i in range (len(n) - 1):
        if n[i+1] != n[i]:
            count += 1
    return count
    
def decToBIn(n):
    res = ""
    while n > 0:
        e = n % 2
        n //= 2
        res = str(e) + res
    return res
    
# n = int(input("input num"))
print (f"ilosc blokow: {iloscBlokow(decToBIn(67))}") # albo n
print (f"ilosc blokow: {iloscBlokow(decToBIn(245))}") # n
print ()
# 2.2
binNums = ["1011", "100010", "1000", "110011", "111111", "101010"] # przykladowe
def atLeast2Blocks(binNums):
    count = 0
    for i in binNums:
        if iloscBlokow(i) <= 2:
            count += 1
    return count
print (f"ilosc liczb skladajacych sie z co najmniej 2 blokow: {atLeast2Blocks(binNums)}")
print ()

# zad 2.3
def maxBinary(numbers):
    max_num = numbers[0]

    for num in numbers[1:]:
        # Porównujemy liczby binarne jako ciągi znaków
        for i in range(len(num)):
            if num[i] > max_num[i]:
                max_num = num
                break
            elif num[i] < max_num[i]:
                break

    return max_num
    
print("Największa liczba binarna:", maxBinary(binNums))
