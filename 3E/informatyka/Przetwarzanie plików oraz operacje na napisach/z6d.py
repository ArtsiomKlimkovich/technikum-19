with open("liczby.txt", "r") as file:
    for i in file:
        line = file.readline().strip()
        if line.count('1') > line.count('0'):
            print(line)