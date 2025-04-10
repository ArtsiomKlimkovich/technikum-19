with open("slowa.txt", "r") as file:
    counter = 1
    for i in file:
        line = file.readline().strip()
        print (counter, "-", line)
        counter += 1