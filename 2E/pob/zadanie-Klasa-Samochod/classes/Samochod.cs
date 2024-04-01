using Newtonsoft.Json;
using System;
using System.Collections.Generic;

namespace zadanie_Klasa_Samochod.classes {
    public enum TypPaliwa { Benzyna, Diesel, Elektryczny, Hybrydowy }

    public class Samochod {
        static int iloscKol = 4;
        private string marka { get; set; }
        private string model { get; set; }
        private int rokProdukcji { get; set; }
        private DateTime DataPierwszejRejstracji { get; set; }
        private float PojemnoscSilnika { get; set; }

        private TypPaliwa typPaliwa { get; set; }

        public Samochod() {
            marka = "Nieznany";
            model = "Nieznany";
            rokProdukcji = 0;
        }

        public Samochod(string marka, string model, int rokProdukcji, DateTime DataPierwszejRejstracji, float PojemnoscSilnika, TypPaliwa typPaliwa) {
            this.marka = marka;
            this.model = model;
            this.rokProdukcji = rokProdukcji;
            this.DataPierwszejRejstracji = DataPierwszejRejstracji;
            this.PojemnoscSilnika = PojemnoscSilnika;
            this.typPaliwa = typPaliwa;
        }

        public void WyswietlInformacje() {
            Console.WriteLine($"Samochod: {marka} o modelu: {model} o roku Produkcji: {rokProdukcji} o Dacie Pierwszej Rejstracji: {DataPierwszejRejstracji.ToShortDateString()} o Pojemnosci Silnika: {PojemnoscSilnika} o Typu paliwa {typPaliwa}");
        }

        public int ObliczWiek() {
            return (DateTime.Now.Year - rokProdukcji);
        }

        public bool CzyKlasyk() {
            return ObliczWiek() >= 25;
        }

        public void WyswietlInformacjeJSON() {
            Console.WriteLine($"{'{'}\nmarka: {marka}\nrokProdukcji: {rokProdukcji}\nDataPierwszejRejstracji: {DataPierwszejRejstracji}\nPojemnoscSilnika: {PojemnoscSilnika}\ntypPaliwa{typPaliwa}\n{'}'}");
        }

        public float ObliczSpalanie(int przejechaneKm, int zuzytePaliwo) {
            return ((float)zuzytePaliwo / przejechaneKm) * 100;
        }
    }
}