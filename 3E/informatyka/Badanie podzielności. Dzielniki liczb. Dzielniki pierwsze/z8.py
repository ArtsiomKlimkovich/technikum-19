a = int(input ("input a: "))
b = int(input ("input b: "))

def sumaDzielnikow(n):
    count = 0
    for i in range (1, n):
        if n % i == 0:
            count += i
    return count


if sumaDzielnikow(a) == b and sumaDzielnikow(b) == a:
    print ("tak")
else:
    print ("nie")
