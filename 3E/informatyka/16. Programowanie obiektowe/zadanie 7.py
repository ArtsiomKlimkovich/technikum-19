import math

class Kolo:
    def __init__(self, promien):
        self.promien = promien

    def pole(self):
        return math.pi * (self.promien ** 2)

    def obwod(self):
        return 2 * math.pi * self.promien

promien = float(input("Podaj promień koła: "))

kolo = Kolo(promien)

print(f"Pole koła: {kolo.pole()}")
print(f"Obwód koła: {kolo.obwod()}")