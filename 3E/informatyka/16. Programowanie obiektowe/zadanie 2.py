class Prostokat:
    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def pole(self):
        return self.dlugosc * self.szerokosc

    def obwod(self):
        return 2 * (self.dlugosc + self.szerokosc)

prostokat = Prostokat(5, 3)

print(f"Pole prostokąta: {prostokat.pole()}")
print(f"Obwód prostokąta: {prostokat.obwod()}")