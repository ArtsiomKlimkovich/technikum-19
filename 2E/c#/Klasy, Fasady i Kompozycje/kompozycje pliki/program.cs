Katalog d1 = new Katalog("Dysk");
Katalog k1 = new Katalog("Zdjecia");
Katalog k2 = new Katalog("Praca");
Katalog k3 = new Katalog("Rozne");

d1.dodaj(k1);
d1.dodaj(k2);
d1.dodaj(k3);

Plik z1 = new Plik("foto1");
Plik z2 = new Plik("foto2");
k1.dodaj(z1);
k1.dodaj(z2);

d1.wyswietl();
abstract class Wierzcholek {
    public string name;
    public abstract void wyswietl();
}

class Plik : Wierzcholek {
    public Plik(string n) {
        name = n;
    }

    public override void wyswietl() {
        Console.Write("--");
        Console.WriteLine(name);
    }
}

class Katalog : Wierzcholek {
    List<Wierzcholek> wierzcholki = new List<Wierzcholek>();
    public Katalog(string n) {
        name = n;
    }
    public void dodaj (Wierzcholek wierzcholek) {
        wierzcholki.Add(wierzcholek);
    }
    public override void wyswietl() {
        Console.WriteLine(name);
        foreach (var item in wierzcholki) {
            Console.Write("--");
            item.wyswietl();
        }
    }
}
