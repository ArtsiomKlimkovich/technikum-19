def binary_to_decimal(binary_str):
    if ',' in binary_str:
        integer_part, fractional_part = binary_str.split(',')
    else:
        integer_part, fractional_part = binary_str, ''

    decimal_integer = 0
    for i, digit in enumerate(reversed(integer_part)):
        if digit == '1':
            decimal_integer += 2 ** i

    decimal_fractional = 0
    for i, digit in enumerate(fractional_part):
        if digit == '1':
            decimal_fractional += 2 ** -(i + 1)

    return decimal_integer + decimal_fractional

binary_input = input("Podaj liczbę binarną (np. 101,0101): ")
decimal_output = binary_to_decimal(binary_input)
print(f"Liczba dziesiętna: {decimal_output}")