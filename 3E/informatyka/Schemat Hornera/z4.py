# FUNKCJA oblicz_wartosc_wielomianu_naiwnie(n, A, x)
#     y ← 0
#     DLA i OD 0 DO n
#         potega ← 1
#         DLA j OD 0 DO n - i - 1
#             potega ← potega * x
#         KONIEC DLA
#         y ← y + A[i] * potega
#     KONIEC DLA
#     ZWRÓĆ y
# KONIEC FUNKCJI
#
# START
#     WPROWADŹ n
#     WPROWADŹ A[0..n]
#     WPROWADŹ x
#     wynik ← oblicz_wartosc_wielomianu_naiwnie(n, A, x)
#     WYŚWIETL "Wartość wielomianu dla x=", x, " wynosi: ", wynik
# KONIEC