def suma_w_systemie_p(a, b, p):
    a_decimal = int(a, p)
    b_decimal = int(b, p)
    suma = a_decimal + b_decimal
    wynik_p = ""   
    while suma > 0:
        wynik_p = str(suma % p) + wynik_p
        suma //= p
    return wynik_p
   
a = input("Podaj pierwszą liczbę w systemie o podstawie p: ")
b = input("Podaj drugą liczbę w systemie o podstawie p: ")
p = int(input("Podaj podstawę systemu (od 2 do 9): "))

if p < 2 or p > 9:
    print("Podstawa systemu musi być w zakresie od 2 do 9.")
else:   
    wynik = suma_w_systemie_p(a, b, p)
    print(f"Wynik dodawania w systemie o podstawie {p}: {wynik}")
