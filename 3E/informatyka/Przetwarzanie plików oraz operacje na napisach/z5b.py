with open ("slowa.txt", "r") as file:
    counter = 0
    for i in file:
        counter += 1
    print (counter)