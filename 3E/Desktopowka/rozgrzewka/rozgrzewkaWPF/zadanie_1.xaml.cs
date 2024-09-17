using System;
using System.Collections.Generic;
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

namespace rozgrzewkaWPF{
    /// <summary>
    /// Логика взаимодействия для zadanie_1.xaml
    /// </summary>
    public partial class zadanie_1 : Window{
        public zadanie_1(){
            InitializeComponent();
        }

        private void imie_TextChanged (object sender, TextChangedEventArgs e) {
            
        }

        private void nazwisko_TextChanged (object sender, TextChangedEventArgs e) {
            
        }

        private void showDataBtn_Click (object sender, RoutedEventArgs e) {
            String imie = imieText.Text;
            String nazwisko = nazwiskoText.Text;
            MessageBox.Show ("Witaj " + imie + " " + nazwisko);
        }

        private void exitBtn_Click (object sender, RoutedEventArgs e) {
            MessageBox.Show ("Bye bye");
            Close();
        }

        private void imie_Копировать_TextChanged (object sender, TextChangedEventArgs e) {

        }
    }
}
