# Monte Carlo
import random

def MonteCarlo (n):
    c = 0
    for i in range (n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            c += 1
    return 4 * c / n

# n = int (input ("imput number of dots: "))
# print (MonteCarlo(n))

print (MonteCarlo(10))
print (MonteCarlo(100))
print (MonteCarlo(100000))