# 3.1
def zrownoWazona(n):
    iloscZer = 0
    iloscJedynek = 0
    for i in n:
        if i == "0":
            iloscZer += 1
        else:
            iloscJedynek += 1
    return iloscZer == iloscJedynek
    
def prawieZrownoWazona(n):
    iloscZer = 0
    iloscJedynek = 0
    for i in n:
        if i == "0":
            iloscZer += 1
        else:
            iloscJedynek += 1
    return iloscZer + 1 == iloscJedynek
    
n = input("wprowadz liczbe binarna: ")
if zrownoWazona(n):
    print ("jest zrownowazona")
if prawieZrownoWazona(n):
    print ("jest prawie zrownowazona")
print ()
# 3.2
binNums = ["10001011","10111000","10100111","11111000","10011100","11100011","10111010","10100011","10011010","10110001","11011010","10001101","1110001010","10000001", "1011", "1011101", "101", "10111111"]

def iloscJedynek(n):
    count = 0
    for i in n:
        if i == "1":
            count += 1
    return count
    
for i in binNums:
    if len(i) == 8 and iloscJedynek(i) >= 3 and iloscJedynek(i) <= 5:
        print (i)
print()
# 3.3
def binToDec (n):
    res = 0
    for i in n:
        res = res * 2 + int(i)
    return res
    
def decToBin(n):
    res = ""
    while n > 0:
        e = n % 2
        n //= 2
        res = str(e) + res
    return res
def maxAbs(binNums):
    max = 0
    for i in range (len(binNums) - 1):
        if abs(binToDec(binNums[i]) - binToDec(binNums[i+1])) > max:
            max = abs(binToDec(binNums[i]) - binToDec(binNums[i+1]))
    return max
print (f"max wartosc bezwzgledna: {decToBin(maxAbs(binNums))}")
print()

# 3.4
# a
binNumsInDec = []
for i in binNums:
    binNumsInDec.append(binToDec(i))

def noZero(n):
    while n > 0:
        if n % 10 == 0:
            return False
        n //= 10
    return True
    
countNoZero = 0
for i in binNumsInDec:
    if noZero(i):
        countNoZero += 1
        
print (f"liczb dziesietnych bez zera: {countNoZero}")
print ()
# b
def countDigits(n):
    count = 0
    while n > 0:
        count += n % 10
        n //= 10
    return count
    
def maxDigitSum (binNumsInDec):
    maxDigitSum = 0
    for i in binNumsInDec:
        if countDigits(i) > maxDigitSum:
            maxDigitSum = i
    return maxDigitSum

print (f"liczba z największą sumę różnych cyfr {maxDigitSum(binNumsInDec)}")
