class ProstokatEkstra:
    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def pole(self):
        return self.dlugosc * self.szerokosc

    def obwod(self):
        return 2 * (self.dlugosc + self.szerokosc)

    def wyswietl_pole(self):
        print(f"Pole prostokąta: {self.pole()}")

    def wyswietl_obwod(self):
        print(f"Obwód prostokąta: {self.obwod()}")

dlugosc = float(input("Podaj długość prostokąta: "))
szerokosc = float(input("Podaj szerokość prostokąta: "))

prostokat_ekstra = ProstokatEkstra(dlugosc, szerokosc)

prostokat_ekstra.wyswietl_pole()
prostokat_ekstra.wyswietl_obwod()