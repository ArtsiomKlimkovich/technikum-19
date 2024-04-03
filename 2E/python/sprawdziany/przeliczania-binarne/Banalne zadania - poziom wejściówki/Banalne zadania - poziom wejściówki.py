# zad 1

n = input("wprowadz liczbe binarna: ")
if n[-1] == "0":
    print ("wpisana liczba jest parzysta")
else:
    print ("wpisana liczba nie jest parzysta")
print ()
# zad 2
a = input ("wprowadz pierwsza liczbe binarna: ")
print ()
b = input ("wprowadz druga liczbe binarna: ")
print ()
def parzystaSuma (a, b):
    if (int(a[-1]) % 2 == 0 and int (b[-1]) == 0) or (int(a[-1]) % 2 != 0 and int(b[-1]) % 2 != 0):
        print ("suma jest parzysta")
    else:
        print ("suma nie jest parzysta")
    print ()

def parzystaRoznica(a, b):
    if (int(a[-1]) % 2 == 0 and int(b[-1])) or (int(a[-1]) % 2 != 0 and int(b[-1]) % 2 != 0):
        print ("roznica jest parzysta")
    else:
        print ("roznicy nie jest parzysta")
    print ()
def parzystyIloczn(a, b):
    if (int(a[-1]) % 2 == 0 and int(b[-1]) == 0) or (int(a[-1]) % 2 != 0 and int(b[-1]) % 2 != 0):
        print ("iloczyn jest parzysty")
    else:
        print ("iloczyn nie jest parzysty")
    print ()
    
parzystaSuma (a, b)
parzystaRoznica (a, b)
parzystyIloczn(a, b)
# zad 3

