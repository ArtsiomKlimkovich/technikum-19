def horner(A, x):
    n = len(A)-1
    y = A[n]
    for i in range(n-1, -1, -1):
        y = x*y + A[i]
    return y

wsp = list(map(int, input("input wsp: ").split()))
x= int(input("input x: "))

print(horner(wsp,x))