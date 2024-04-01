# Algorytm Newtona - Raphsona

def pierwiastek(x, eps):
    a = x
    b = 1
    while abs(a - b) > eps:
        a = (a + b) / 2
        b = x / a
    return a

def pierwiastek2(x, n):
    a = x
    b = 1
    for i in range(n):
        a = (a + b) / 2
        b = x / a
    return a