with open ("slowa.txt", "r") as file:
    for i in file:
        line = file.readline().strip()
        if len(line) == 6:
            print (line)