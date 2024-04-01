def binToDec(n): # zwykly sposob przez dzielenie liczby przez 2 i tak do 1, dalej zapisywanie modulo(2) tego w zmienna e, potem  modulo + res, zeby odrazu bylo odwrocone
    res = ""
    while n > 0:
        e = n % 2
        n //= 2
        res = str(e) + res
    return res

def binToDecReku(n): # rekurencyjnie bez return przez print(), najpierw robi stos liczby podzielonej przez 2 i tak do 1, potem print modulo (2)
    if n == 0: return 0;
    binToDecReku(n // 2)
    print (n % 2, end="")

def binToDecReku2(n): # rekurencyjnie z returnem, robi stos liczby prez 2 i tak do 1, czyli od 1 do 39 dodaje str modulo od 1 do 39 modulo(2)
    if n == 0: return "";
    return binToDecReku2(n // 2) + str(n % 2)

def decToBin(s): # idzie od konca liczby i dodaje do res od konca 2 do potegi i
    res = 0
    for i in range (len(s)):
        res = res + 2 ** i * int(s[-1-i])
    return res
def decToBin2 (n): # (schemat Hornera) dla kazdego 1 lub 0 w str(n) dodaje do calej sumy pomnozona sume + 1 lub 0
    res = 0
    for digit in str(n):
        res = res * 2 + int(digit)
    return res

n = int (input("input a number: "))
print (f"liczba {n} w systemie dwojkowym to {binToDec(n)}")
print (f"liczba {n} w systemie dwojkowym to ", end="")
binToDecReku(n)
print ()
print (f"liczba {n} w systemie dwojkowym to {binToDecReku2(n)}")

print (f"liczba {n} w systemie dziesiatkowym to {decToBin(str(n))}")
print (f"liczba {n} w systemie dziesiatkowym to {decToBin2(n)}")
