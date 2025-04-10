def suma_binarnych(a, b):
    a_decimal = int(a, 2)
    b_decimal = int(b, 2)
    suma = a_decimal + b_decimal
    return bin(suma)[2:]

a = input("Podaj pierwszą liczbę binarną: ")
b = input("Podaj drugą liczbę binarną: ")

wynik = suma_binarnych(a, b)
print("Wynik dodawania:", wynik)
