# Wyszukiwanie lidera

def lider(T):
    ilość = 1
    lider = T[0]
    for i in range(1,len(T)):
        if ilość == 0:
            lider = T[i]
            ilość = 1
        else:
            if T[i] == lider:
                ilość += 1
            else:
                ilość -= 1
    ilość_liderów = 0
    if ilość == 0:
        print("brak lidera")
    else:
        for i in range(len(T)):
            if T[i] == lider:
                ilość_liderów += 1
    if ilość_liderów > len(T)//2:
        print("Jest lider", lider)