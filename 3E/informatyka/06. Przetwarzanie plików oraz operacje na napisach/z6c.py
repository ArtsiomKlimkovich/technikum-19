with open("liczby.txt", "r") as file:
    for i in file:
        line = file.readline().strip()
        if line[-3:] == "000":
            print (line)