with open("slowa.txt", 'r') as file:
    counter = 0
    for i in file:
        line = file.readline().strip()
        for i in line:
            if i == 'A':
                counter += 1
    print(counter)