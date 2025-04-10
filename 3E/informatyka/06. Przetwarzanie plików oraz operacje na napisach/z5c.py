with open ("slowa.txt", "r") as file:
    for i in file:
        line = file.readline().strip()
        if line[0] == 'A':
            print (line)