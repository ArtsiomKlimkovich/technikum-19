with open("slowa.txt", "r") as file:
    for i in file:
        line = file.readline().strip()
        print (line, len(line))