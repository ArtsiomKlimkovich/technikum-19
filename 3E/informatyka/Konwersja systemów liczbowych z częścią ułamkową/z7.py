def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary_str = ""
    while n > 0:
        binary_str = str(n % 2) + binary_str
        n //= 2
    return binary_str

number = int(input("Podaj liczbę całkowitą dziesiętną: "))
binary_output = decimal_to_binary(number)
print(f"Liczba binarna: {binary_output}")