class Trojkat:
    def __init__(self, a, b, c, wysokosc):
        self.a = a
        self.b = b
        self.c = c
        self.wysokosc = wysokosc

    def pole(self):
        return 0.5 * self.a * self.wysokosc

    def obwod(self):
        return self.a + self.b + self.c

a = float(input("Podaj bok a trójkąta: "))
b = float(input("Podaj bok b trójkąta: "))
c = float(input("Podaj bok c trójkąta: "))
wysokosc = float(input("Podaj wysokość trójkąta: "))

trojkat = Trojkat(a, b, c, wysokosc)

print(f"Pole trójkąta: {trojkat.pole()}")
print(f"Obwód trójkąta: {trojkat.obwod()}")