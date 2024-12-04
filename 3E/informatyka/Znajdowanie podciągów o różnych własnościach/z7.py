with open("liczby.txt", "r") as plik:
    liczby = plik.readline().strip().split()

n = len(liczby)

def isMalejacy():
    for i in range(n):
        if i > i+1:
            continue
        else:
            return False
    return True

if isMalejacy():
    print("tak")
else:
    print("nie")