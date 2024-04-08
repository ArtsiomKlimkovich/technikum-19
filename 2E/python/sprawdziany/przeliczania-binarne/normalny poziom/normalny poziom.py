# Poziom maturalny z liczb binarnych

# 1. Napisz alg dodawania dwóch liczb binarnych o tej samej długości.")
def addBinary (a, b):
    res = ""
    carry = 0
    for i in range (len(a) - 1, -1, -1):
        bitSum = int(a[i]) + int(b[i]) + carry
        res = str(bitSum % 2) + res
        carry = bitSum // 2
    if carry:
        res = "1" + res
        
    return res
    
liczba1 = "1010111" # 87
liczba2 = "0110001" # 49
# liczba1 = int(input("wprowadz 1 liczbe binarna: "))
# liczba2 = int(input("wprowadz 2 liczbe binarna: "))

print (f"Wynik dodawania binarnego {liczba1} ({int(liczba1, 2)}) + {liczba2} ({int(liczba2, 2)}) = {addBinary(liczba1,liczba2)} ({int(addBinary(liczba1,liczba2), 2)})")
print()
# 2. Napisz algorytm dodawania dwóch liczb binarnych o różnej długości.
def addBinary_differentLength (a, b):
    if len (a) > len(b):
        for i in range (len(a)-len(b)):
            b = "0" + b
    else:
        for i in range (len(b)-len(a)):
            a = "0" + a
    res = ""
    carry = 0
    for i in range (len(a) - 1, -1, -1):
        bitSum = int(a[i]) + int(b[i]) + carry
        res = str(bitSum % 2) + res
        carry = bitSum // 2
    if carry:
        res = "1" + res
        
    return res

liczba3 = "1001001" # 87
liczba4 = "11001" # 49
# liczba3 = int(input("wprowadz 1 liczbe binarna: "))
# liczba4 = int(input("wprowadz 2 liczbe binarna: "))

print (f"Wynik dodawania binarnego liczb o roznej dlugosci {liczba3} ({int(liczba3, 2)}) + {liczba4} ({int(liczba4, 2)}) = {addBinary_differentLength(liczba4,liczba4)} ({int(addBinary_differentLength(liczba3,liczba4), 2)})")
print ()
# 3. Wypisz wszystkie liczby binarne sześciocyfrowe, w których liczba jedynek jest 2 razy większa od liczby zer.

