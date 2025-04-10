with open("slowa.txt", "r") as file:
    for i in file:
        line = file.readline().strip()
        if line.__contains__('O'):
            print(line, line.count('O'))