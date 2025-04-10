with open("liczby.txt", "r") as file:
    for i in file:
        line = file.readline().strip()
        print (int(line, 2))