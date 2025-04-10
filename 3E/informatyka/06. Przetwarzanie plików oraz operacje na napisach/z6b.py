with open("liczby.txt", "r") as file:
    for i in file:
        line = file.readline().strip()
        if line[-1] == '0':
            print(line)