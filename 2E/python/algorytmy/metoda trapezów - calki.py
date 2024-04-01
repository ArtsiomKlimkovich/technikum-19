# metoda trapezów - 2 techniki

def trapezy(a,b,n):
    dx = (b-a)/n
    suma = 0
    for i in range(n):
        suma += (f(a+i*dx)+f(a+(i+1)*dx))/2*dx
    return suma

def trapezy2(a,b,n):
    dx = (b-a)/n
    suma = f(a) + f(b)
    for i in range(1,n):
        suma += 2*f(a+i*dx)
    suma *= dx/2
    return suma
