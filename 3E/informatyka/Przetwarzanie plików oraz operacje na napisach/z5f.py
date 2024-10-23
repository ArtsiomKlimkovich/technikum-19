with open("slowa.txt", "r") as file:
    maxes = []
    for i in file: maxes.append(i)
    print (max(maxes, key=len), min(maxes, key=len))