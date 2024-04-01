# metoda prostokątów - potrzeba jest funkcja oraz trzy warianty tej metody


def f(x): 
    return -x**2 + 6*x + 2

def prostokaty1(a, b, n):
    dx = (b - a) / n
    s = 0
    for i in range(n):
        s += f(a + i * dx) * dx
    return s

def prostokaty2(a, b, n):
    dx = (b - a) / n
    s = 0
    for i in range(n):
        s += f(a + dx / 2 + i * dx) * dx
    return s

def prostokaty3(a, b, n):
    dx = (b - a) / n
    s = 0
    for i in range(n):
            s += f(a + dx + i * dx) * dx
    return s