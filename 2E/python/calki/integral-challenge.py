# sqrt(x) + 1    od 1 do 4

import numpy as np
from matplotlib import pyplot as plt


# def f(x):
#     return np.sqrt(x) + 1

def f(x):
    return x ** 2 - 8 * x + 12


def pole(a, b, n):
    dx = (b - a) / n
    s = 0
    for i in range(n):
        s += f(a + dx / 2 + i * dx) * dx
    return s


print(pole(1, 4, 10))

x = np.linspace(-5, 50, 100)

plt.plot(x, f(x), color='crimson')

plt.show()

def bisekcja(a, b, epsilon):
    while abs(b - a) > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2
        middle = (a + b) / 2
        if a >= b:
            print ("Nie ma miejsc zerowych")
            return -1
    return middle

def bisekcja_2(a, b, n):
    for i in range(n):
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

print ("miejsce zerowe to")
print(bisekcja(1, 10, 0))