string[] Adressat1 = new string[] { "Kasia", "Marianna", "Zuzanna", "Izabella" };

void wyswietlMenuGlowne() {
    Console.WriteLine("Napisz - wybierz 1");
    Console.WriteLine("Czy zdolny - wybierz 2");
    Console.WriteLine("Zapraszam wyjsc - wybierz Esc");
}
bool czyZdolnyDoWyslania() {
    Random random = new Random();

    int a = random.Next(1, 10);
    int b = random.Next(1, 10);
    int c = random.Next(1, 10);

    string dzialanie = string.Format("{0} + {1} * {2}", a, b, c);
    int wynik = a + b * c;
    Console.WriteLine(dzialanie);
    int odPijaka = int.Parse(Console.ReadLine());

    return wynik == odPijaka;
}

void wyswietlFormularzWiadomosci() {
    Console.WriteLine("Wybierz adresatke: ");
    int j = 1;
    foreach (var item in Adressat1 ) {
        Console.WriteLine(j + " - " + item);
        j++;
    }
}

void writeMessage() {
    Console.WriteLine("Wybierz adressata");
    int a = int.Parse(Console.ReadLine());

    Console.Clear();

    string adressat = Adressat1[a - 1]; 
    Console.WriteLine("Napisz swoje imie: ");
    string yourName = Console.ReadLine();

    Console.WriteLine("Napisz wiadomosc: ");
    string message = Console.ReadLine();

    
}

wyswietlMenuGlowne();
ConsoleKey k;
bool zdolny = false;

do {
    k = Console.ReadKey().Key;
    switch (k) {
        case (ConsoleKey.D1):
            Console.WriteLine("1");
            Console.Clear();
            if (zdolny) {
                wyswietlFormularzWiadomosci();
                writeMessage();
            } else {
                wyswietlMenuGlowne();
            }
            break;
        case (ConsoleKey.D2):
            Console.WriteLine("2");
            Console.Clear();
            if (zdolny) {
                continue;
            }
            if (czyZdolnyDoWyslania()) {
                zdolny = true;
                Console.Clear();
                wyswietlMenuGlowne();
            }
            break;
        case (ConsoleKey.Escape):
            break;
        default:
            Console.WriteLine("wybierz menu pijaku");
            break;
    }
}while(k != ConsoleKey.Escape);
