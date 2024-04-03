# Zagadnienia na spr 1:

# 1. Metody numeryczne - prostokąty i trapezy
def f(x):
    return -x**2 + 6*x + 2
def prostokąty_poczatek(a,b,n):
    dx = (b-a)/n
    s = 0
    for i in range(n):
        s += f(a + i*dx) * dx
    return s
    
def prostokąty_srodek(a,b,n):
    dx = (b-a)/n
    s = 0
    for i in range(n):
        s += f(a + i*dx + dx/2) * dx
    return s
    
def prostokąty_koniec(a,b,n):
    dx = (b-a)/n
    s = 0
    for i in range(n):
        s += f(a + i*dx + dx) * dx
    return s
print ("poczatek", prostokąty_poczatek(3, 6, 100))
print ("srodek", prostokąty_srodek(3, 6, 100))
print ("koniec", prostokąty_koniec(3, 6, 100))
print()
def trapezy1(a, b, n):
    dx = (b-a)/n
    s = 0
    for i in range (n):
        s +=(f(a + i*dx) + f(a+(i+1)*dx)) / 2 * dx
    return s

def trapezy2(a, b, n):
    dx = (b-a)/n
    s = f(a) + f(b)
    for i in range (1, n):
        s += 2 * f(a + i*dx)
    s *= dx/2
    return s

print (trapezy1(3, 6, 100))
print (trapezy2(3, 6, 100))
print ()
# 2. Metoda bisekcji (stopowana ilością kroków lub przedziałem)

def bisekcja1(a, b, eps):
    while abs(a-b) > eps:
        middle = (a+b)/2
        if f(middle) == 0:
            return middle
        if f(a) * f(middle) < 0:
            b = middle
        else:
            a = middle
    return (a+b)/2

def bisekcja2(a, b, n):
    for i in range (n):
        middle = (a+b)/2
        if f(middle) == 0:
            return middle
        if f(a) * f(middle) < 0:
            b = middle
        else:
            a = middle
    return (a+b)/2

print (bisekcja1 (3, 6, 0.01))
print (bisekcja2 (3, 6, 100))
print ()
# 3. Alg Newtona - Raphsona (stopowany ilością kroków lub przedziałem)
def NR1(x, eps):
    a = x
    b = 1
    while abs(a-b) > eps:
        a = (a+b)/2
        b = x/a
    return a

def NR2(x, n):
    a = x
    b = 1
    for i in range (n):
        a = (a+b)/2
        b = x/a
    return a
    
print (NR1 (49, 0.01))
print (NR2 (49, 100))
print ()
# 4. Wyszukiwanie lidera w liście

def lider (T):
    ilosc = 1
    lider = T[0]
    for i in range (1, len (T)):
        if ilosc == 0:
            lider = T[i]
            ilosc = 1
        else:
            if lider == T[i]:
                ilosc += 1
            else:
                ilosc -= 1
    iloscLiderow = 0
    if ilosc == 0:
        print ("nie ma lidera")
    else:
        for i in range (len(T)):
            if T[i] == lider:
                iloscLiderow += 1
        if iloscLiderow > len(T)//2:
            print (f"jest lider i to jest {lider}")
    
T = [1, 2, 1, 1, 1, 3]
lider (T)
print ()
# 5. Metoda Monte Carlo
import random as r
def MonteCarlo (n):
    dotsInCircle = 0
    for i in range (n):
        x = r.uniform (-1, 1)
        y = r.uniform (-1, 1)
        if x**2 + y**2 <= 1:
            dotsInCircle += 1
    return 4 * dotsInCircle/ n
    
print (MonteCarlo(10))
print (MonteCarlo(100))
print (MonteCarlo(1000))
print (MonteCarlo(10000))
