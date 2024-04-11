binNums = ["101011010011001100111", "10001001", "1000000", "101010011100 ","100010"] # przykladowe

# zad 4.1
count = 0
for i in binNums:
    if i.count("0") > i.count("1"):
        count += 1

print ("zad 4.1")
print(f"W {count} liczbach ilosc zer wiecej niz jedynek")
print ()

# zad 4.2
binNums2 = ["101011010011001100000", "10001001", "100100", "101010010101011011000", "100011"] # przykladowe
def isDivededBy2(n):
    if n[-1] == "0":
        return n
    else:
        return

def isDivededBy8(n):
    if n[-3:] == "000":
        return n
    else:
        return

counterDevBy2 = 0
counterDevBy8 = 0
for i in binNums2:
    if isDivededBy2(i):
        counterDevBy2 += 1
    if isDivededBy8(i):
        counterDevBy8 += 1

print("zad 4.2")
print(f"{counterDevBy2} liczb jest podzielne prez 2\n{counterDevBy8} liczb jest podzielne przez 8")
print()

# 4.3
binNums3 = ["101011010011001100111", "10001001011101010", "1001000", "101010011100", "1000110"] # przykladowe
def maxAndMinBin(binNums):
    max_length = len(max(binNums, key=len))
    min_length = len(min(binNums, key=len))

    max_index = 0
    min_index = 0

    binNums_aligned = [num.zfill(max_length) for num in binNums] # zfill jest wbudowana, ale mozemy zrobic sami

    # Porównujemy liczby binarne jako ciągi znaków
    for i in range(1, len(binNums_aligned)):
        if binNums_aligned[i] > binNums_aligned[max_index]:
            max_index = i
        if binNums_aligned[i] < binNums_aligned[min_index]:
            min_index = i

    return [min_index+1, max_index+1]

print("zad 4.3")
print (f"Najwieksza i najmniejsza liczby sa liczby o indeksie {maxAndMinBin(binNums3)[0]} i {maxAndMinBin(binNums3)[1]}")
