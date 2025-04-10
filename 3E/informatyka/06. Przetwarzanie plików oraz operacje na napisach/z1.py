imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")

# Zapisywanie danych do pliku
with open('dane_osobowe.txt', 'w') as plik:
    plik.write(f"{imie}\n{nazwisko}\n")

print("Dane zostały zapisane w pliku dane_osobowe.txt.")