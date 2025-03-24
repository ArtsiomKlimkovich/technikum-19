def decimal_to_binary(n):
    if n < 0:
        return '-' + decimal_to_binary(-n)

    integer_part = int(n)
    fractional_part = n - integer_part

    binary_integer = ""
    if integer_part == 0:
        binary_integer = "0"
    else:
        while integer_part > 0:
            binary_integer = str(integer_part % 2) + binary_integer
            integer_part //= 2

    binary_fractional = ""
    count = 0
    while fractional_part > 0 and count < 15:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional += str(bit)
        fractional_part -= bit
        count += 1

    if binary_fractional:
        return f"{binary_integer},{binary_fractional}"
    else:
        return binary_integer


number = float(input("Podaj liczbę dziesiętną: "))
binary_output = decimal_to_binary(number)
print(f"Liczba binarna: {binary_output}")