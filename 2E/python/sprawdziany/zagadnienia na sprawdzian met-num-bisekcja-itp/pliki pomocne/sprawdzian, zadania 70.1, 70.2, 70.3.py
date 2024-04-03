import math
def f(x):
    return x**4/500 - x**2/200 - 3/250

def g(x):
    return -x**3/30 + x/20 + 1/6
    
def poleF(a, b, n):
    dx = (b-a)/n
    s = 0
    for i in range (n):
        s += f(a + i*dx + dx/2) * dx
    return s

def poleG(a, b, n):
    dx = (b-a)/n
    s = 0
    for i in range (n):
        s += g(a + i*dx + dx/2) * dx
    return s
# zad 1    
x1 = 2
x2 = 10
poleABCD = (10-2) * (f(10) + abs(g(10)))
poleZaslony = poleF(x1, x2, 1000) + abs(poleG(x1, x2, 1000))
polePozostale = poleABCD - poleZaslony
polePozostale = round(polePozostale, 3)
print (f"pole pozostale: {polePozostale}")

# zad 2
def krzywaF (a, b, n):
    dx = (b-a)/n
    s = 0
    for i in range (n):
        s += math.sqrt(dx**2 + (f(a + dx) - f(a)) * (f(a + dx) -f(a)))
    return s

def krzywaG (a, b, n):
    dx = (b-a)/n
    s = 0
    for i in range (n):
        s += math.sqrt(dx**2 + (g(a + dx) - g(a)) * (g(a + dx) -g(a)))
    return s
obwodZaslony = krzywaF(x1, x2, 1000) + krzywaG(x1, x2, 1000) + (f(10) - g(10)) + (10-2) * 2
print (f"obwod zaslony jest rowny: {obwodZaslony}")
# zad 3
def poleKoniec (a, b, n):
    dx = 0.25
    s = 0
    for i in range (n):
        s += math.floor (f(a + i*dx))
    return s
print (poleKoniec(x1, x2, int(8/0.25)))
