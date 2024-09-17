using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace rozgrzewkaWPF {
    /// <summary>
    /// Interaction logic for zadanie_2.xaml
    /// </summary>
    public partial class zadanie_2 : Window {
        public zadanie_2 () {
            InitializeComponent ();
        }

        private void ImieTextBox_TextChanged (object sender, System.Windows.Controls.TextChangedEventArgs e) {
            
        }

        private void Zapisz_Click (object sender, RoutedEventArgs e) {
            try {
                // Pobranie wartości z kontrolek
                string imie = imieText.Text;
                string plec = maleRadio.IsChecked == true ? "Mężczyzna" :
                              femaleRadio.IsChecked == true ? "Kobieta" :
                              "Nie wybrano";
                string hobby = (SportCheckbox.IsChecked == true ? "Sport, " : "") +
                               (MuzykaCheckbox.IsChecked == true ? "Muzyka, " : "") +
                               (PodrozeCheckbox.IsChecked == true ? "Podróże" : "").TrimEnd (',', ' ');
                string opis = opisTextArea.Text;

                // Tworzenie ścieżki do pliku
                string filePath = "dane_osoby.txt";
                using(StreamWriter writer = new StreamWriter (filePath)) {
                    writer.WriteLine ($"Imię: {imie}");
                    writer.WriteLine ($"Płeć: {plec}");
                    writer.WriteLine ($"Hobby: {hobby}");
                    writer.WriteLine ($"Opis: {opis}");
                }

                // Aktualizacja statusu
                StatusLabel.Content = "Dane zostały zapisane do pliku.";
            } catch(Exception ex) {
                StatusLabel.Content = $"Błąd: {ex.Message}";
            }
        }

        private void Zamknij_Click (object sender, RoutedEventArgs e) {
            // Wyświetlenie komunikatu o zamknięciu
            MessageBoxResult result = MessageBox.Show ("Czy na pewno chcesz zamknąć aplikację?", "Potwierdzenie", MessageBoxButton.YesNo);
            if(result == MessageBoxResult.Yes) {
                Application.Current.Shutdown ();
            }
        }
    }
}
