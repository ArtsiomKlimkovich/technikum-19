import math
import matplotlib.pyplot as plt
def fib(n):
    fibNums = [1, 1]
    for i in range(2, n):
        fibNums.append(fibNums[-1] + fibNums[-2])
    return fibNums

def F(n):
    fibNums = fib(n)
    return fibNums[-1]

def isPrime(n):
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True
    
def decToBin(n):
    res = ""
    while n > 0:
        e = n % 2
        n //= 2
        res = str(e) + res
    return res
    
def draw_fractal(fibonacci_binary):
    plt.imshow([[int(bit) for bit in row] for row in fibonacci_binary], cmap='binary')
    plt.axis('off')
    plt.savefig('fractal.png')
    plt.show()

print("zad 67.1")
print (f"F{10} = {F(10)}")
print (f"F{20} = {F(20)}")
print (f"F{30} = {F(30)}")
print (f"F{40} = {F(40)}")
print ()
print("zad 67.2")
primeFib = fib(40)
for i in primeFib[1:]:
    if isPrime(i):
        print (i)
print ()
print("zad 67.3")
print()
primeFibBin = []
for i in primeFib:
    primeFibBin.append(decToBin(i))
    print (decToBin(i))

maxLength = len(primeFibBin[-1])
primeFibBinSameLength = []
for i in primeFibBin:
    primeFibBinSameLength.append(i.zfill(maxLength))
    
draw_fractal(primeFibBinSameLength)
print ()
print("zad 67.4")
print()
for i in primeFibBin:
    if i.count("1") == 6:
        print (i)
