using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using zadanie_Klasa_Samochod.classes;

namespace zadanie_Klasa_Samochod {
    internal class Program {
        static List<Samochod> samochody = new List<Samochod>();

        static void Main(string[] args) {
            // Testowanie metody WyswietlInformacje na obiekcie utworzonym za pomocą domyślnego konstruktora
            Samochod defaultCar = new Samochod();
            Console.WriteLine("Informacje o samochodzie utworzonym za pomocą domyślnego konstruktora:");
            defaultCar.WyswietlInformacje();
            Console.WriteLine();

            // Testowanie metody WyswietlInformacje na obiekcie utworzonym za pomocą konstruktora parametrycznego
            Samochod customCar = new Samochod("Fiat", "500", 2018, new DateTime(2018, 5, 20), 1.2f, TypPaliwa.Benzyna);
            Console.WriteLine("Informacje o samochodzie utworzonym za pomocą konstruktora parametrycznego:");
            customCar.WyswietlInformacje();
            Console.WriteLine();

            // Testowanie metody ObliczWiek
            Console.WriteLine($"Wiek samochodu: {customCar.ObliczWiek()} lat.");
            Console.WriteLine();

            // Testowanie metody CzyKlasyk
            Console.WriteLine($"Czy samochód jest klasykiem? {customCar.CzyKlasyk()}");
            Console.WriteLine();

            // Testowanie metody WyswietlInformacjeJSON
            Console.WriteLine("Informacje o samochodzie w formacie JSON:");
            customCar.WyswietlInformacjeJSON();
            Console.WriteLine();

            // Testowanie metody ObliczSpalanie
            int przejechaneKilometry = 500;
            int zuzytePaliwo = 50;
            int spalanie = (int)customCar.ObliczSpalanie(zuzytePaliwo, przejechaneKilometry);
            Console.WriteLine($"Spalanie: {spalanie} l/100km.");

            // Testowanie Menu operacji
            Console.WriteLine("Witam w menu operacji");
            bool exit = false;
            do {
                ShowMenu();
                int choice;
                if (!int.TryParse(Console.ReadLine(), out choice)) {
                    Console.WriteLine("Niepoprawny numer operacji.");
                    continue;
                }

                switch (choice) {
                    case 1:
                        DodajSamochod();
                        break;
                    case 2:
                        WyswietlInformacje();
                        break;
                    case 3:
                        ObliczWiekSamochodu();
                        break;
                    case 4:
                        SprawdzCzyKlasyk();
                        break;
                    case 5:
                        WyswietlInformacjeJSON();
                        break;
                    case 6:
                        ObliczSpalanie();
                        break;
                    case 7:
                        exit = true;
                        break;
                    default:
                        Console.WriteLine("Niepoprawny numer operacji.");
                        break;
                }
                Console.WriteLine("Naciśnij dowolny klawisz, aby kontynuować...");
                Console.ReadKey();
                Console.Clear();
            } while (!exit);
        }

        public static void ShowMenu() {
            Console.WriteLine("1: Dodaj Samochód");
            Console.WriteLine("2: Wyświetl Informacje");
            Console.WriteLine("3: Oblicz Wiek Samochodu");
            Console.WriteLine("4: Sprawdź, Czy Klasyk");
            Console.WriteLine("5: Wyświetl Informacje JSON");
            Console.WriteLine("6: Oblicz Spalanie");
            Console.WriteLine("7: Wyjście");
            Console.Write("Wprowadz numer operacji: ");
        }

        public static void DodajSamochod() {
            try {
                Console.Write("Wprowadz marke samochodu: ");
                string marka = Console.ReadLine();

                Console.Write("Wprowadz model samochodu: ");
                string model = Console.ReadLine();

                Console.Write("Wprowadz rok produkcji samochodu: ");
                int rokProdukcji;
                while (!int.TryParse(Console.ReadLine(), out rokProdukcji) || rokProdukcji < 1900 || rokProdukcji > DateTime.Now.Year) {
                    Console.WriteLine("Niepoprawny rok produkcji. Wprowadz ponownie.");
                    Console.Write("Wprowadz rok produkcji samochodu: ");
                }

                Console.Write("Wprowadz date pierwszej rejestracji (RRRR-MM-DD): ");
                DateTime dataRejestracji;
                while (!DateTime.TryParse(Console.ReadLine(), out dataRejestracji) || dataRejestracji > DateTime.Now) {
                    Console.WriteLine("Niepoprawna data rejestracji. Wprowadz ponownie.");
                    Console.Write("Wprowadz date pierwszej rejestracji (RRRR-MM-DD): ");
                }

                Console.Write("Wprowadz pojemnosc silnika: ");
                float pojemnoscSilnika;
                while (!float.TryParse(Console.ReadLine(), out pojemnoscSilnika) || pojemnoscSilnika <= 0) {
                    Console.WriteLine("Niepoprawna pojemność silnika. Wprowadz ponownie.");
                    Console.Write("Wprowadz pojemnosc silnika: ");
                }

                TypPaliwa typPaliwa;
                bool isValidTypPaliwa = false;
                do {
                    Console.WriteLine("Wybierz typ paliwa:");
                    foreach (var typ in Enum.GetValues(typeof(TypPaliwa))) {
                        Console.WriteLine($"{(int)typ}: {typ}");
                    }

                    if (Enum.TryParse(Console.ReadLine(), out typPaliwa)) {
                        isValidTypPaliwa = true;
                    } else {
                        Console.WriteLine("Niepoprawny typ paliwa. Wybierz ponownie.");
                    }
                } while (!isValidTypPaliwa);
                Samochod samochod = new Samochod(marka, model, rokProdukcji, dataRejestracji, pojemnoscSilnika, typPaliwa);
                samochody.Add(samochod);
                Console.WriteLine("Dodano nowy samochód.");
            } catch (Exception ex) {
                Console.WriteLine($"Wystąpił błąd: {ex.Message}");
            }
        }
        public static void WyswietlInformacje() {
            try {
                Console.WriteLine("Lista samochodów:");
                for (int i = 0; i < samochody.Count; i++) {
                    Console.WriteLine($"Samochód {i + 1}:");
                    samochody[i].WyswietlInformacje();
                    Console.WriteLine();
                }
            } catch (Exception ex) {
                Console.WriteLine($"Wystąpił błąd: {ex.Message}");
            }
        }

        public static void ObliczWiekSamochodu() {
            WyswietlListeSamochodow();
            try {
                Console.Write("Podaj indeks samochodu do obliczenia wieku: ");
                int index;
                while (!int.TryParse(Console.ReadLine(), out index) || index < 1 || index > samochody.Count) {
                    Console.WriteLine("Niepoprawny indeks samochodu. Wprowadz ponownie.");
                    Console.Write("Podaj indeks samochodu do obliczenia wieku: ");
                }

                int wiek = samochody[index - 1].ObliczWiek();
                Console.WriteLine($"Wiek samochodu: {wiek} lat.");
            } catch (Exception ex) {
                Console.WriteLine($"Wystąpił błąd: {ex.Message}");
            }
        }

        public static void SprawdzCzyKlasyk() {
            WyswietlListeSamochodow();
            try {
                Console.Write("Podaj indeks samochodu do sprawdzenia: ");
                int index;
                while (!int.TryParse(Console.ReadLine(), out index) || index < 1 || index > samochody.Count) {
                    Console.WriteLine("Niepoprawny indeks samochodu. Wprowadz ponownie.");
                    Console.Write("Podaj indeks samochodu do sprawdzenia: ");
                }

                bool isKlasyk = samochody[index - 1].CzyKlasyk();
                Console.WriteLine($"Czy samochód jest klasykiem: {isKlasyk}");
            } catch (Exception ex) {
                Console.WriteLine($"Wystąpił błąd: {ex.Message}");
            }
        }

        public static void WyswietlInformacjeJSON() {
            WyswietlListeSamochodow();
            try {
                Console.Write("Podaj indeks samochodu do wyświetlenia informacji JSON: ");
                int index;
                while (!int.TryParse(Console.ReadLine(), out index) || index < 1 || index > samochody.Count) {
                    Console.WriteLine("Niepoprawny indeks samochodu. Wprowadz ponownie.");
                    Console.Write("Podaj indeks samochodu do wyświetlenia informacji JSON: ");
                }

                samochody[index - 1].WyswietlInformacjeJSON();
            } catch (Exception ex) {
                Console.WriteLine($"Wystąpił błąd: {ex.Message}");
            }
        }

        public static void ObliczSpalanie() {
            WyswietlListeSamochodow();
            try {
                Console.Write("Podaj indeks samochodu do obliczenia spalania: ");
                int index;
                while (!int.TryParse(Console.ReadLine(), out index) || index < 1 || index > samochody.Count) {
                    Console.WriteLine("Niepoprawny indeks samochodu. Wprowadz ponownie.");
                    Console.Write("Podaj indeks samochodu do obliczenia spalania: ");
                }

                Console.Write("Podaj przejechane kilometry: ");
                int przejechaneKm;
                while (!int.TryParse(Console.ReadLine(), out przejechaneKm) || przejechaneKm <= 0) {
                    Console.WriteLine("Niepoprawna wartość. Wprowadz ponownie.");
                    Console.Write("Podaj przejechane kilometry: ");
                }

                Console.Write("Podaj zużytą ilość paliwa (w litrach): ");
                int zuzytePaliwo;
                while (!int.TryParse(Console.ReadLine(), out zuzytePaliwo) || zuzytePaliwo <= 0) {
                    Console.WriteLine("Niepoprawna wartość. Wprowadz ponownie.");
                    Console.Write("Podaj zużytą ilość paliwa (w litrach): ");
                }

                float spalanie = samochody[index - 1].ObliczSpalanie(przejechaneKm, zuzytePaliwo);
                Console.WriteLine($"Spalanie wynosi: {spalanie} l/100km.");
            } catch (Exception ex) {
                Console.WriteLine($"Wystąpił błąd: {ex.Message}");
            }
        }
        public static void WyswietlListeSamochodow() {
            Console.WriteLine("Lista samochodów:");
            for (int i = 0; i < samochody.Count; i++) {
                Console.WriteLine($"Samochód {i + 1}:");
                samochody[i].WyswietlInformacje();
                Console.WriteLine();
            }
        }
    }
}