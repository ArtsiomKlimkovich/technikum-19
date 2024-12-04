with open("liczby.txt", "r") as plik:
    liczby = plik.readline().strip().split()

n = len(liczby)

def isStaly():
    for i in range(n):
        if i == i+1:
            continue
        else:
            return False
    return True

if isStaly():
    print("tak")
else:
    print("nie")