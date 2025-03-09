with open("ciagi.txt", "r") as file:
    liczby = list()
    for line in file:
        liczby.append(list(map(int, line.split())))

def printCiagiWhereSumEquals10(ciag):
    n = len(ciag)
    for i in range(n-2):
        tempCiag = ciag[i:i+3]
        if sum(tempCiag) == 10:
            tempCiag = ' '.join(map(str, tempCiag))
            print(tempCiag)

for ciag in liczby:
    printCiagiWhereSumEquals10(ciag)