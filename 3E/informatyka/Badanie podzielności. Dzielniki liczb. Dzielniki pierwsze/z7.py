n = int(input ("input num: "))

count = 0
for i in range (1, n):
    if n % i == 0:
        count += i

if n == count:
    print ("Tak")
else:
    print ("Nie")
