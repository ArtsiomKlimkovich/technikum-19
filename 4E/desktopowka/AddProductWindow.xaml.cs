using System;
using System.Windows;

namespace SpokojnySklep
{
    public partial class AddProductWindow : Window
    {
        public string ProductName { get; private set; }
        public int ProductPrice { get; private set; }
        public bool IsDigitalProduct { get; private set; }

        public AddProductWindow()
        {
            InitializeComponent();
        }

        private void AddButton_Click(object sender, RoutedEventArgs e)
        {
            if (string.IsNullOrWhiteSpace(ProductNameTextBox.Text) || !int.TryParse(ProductPriceTextBox.Text, out int price))
            {
                MessageBox.Show("Wprowadź poprawną nazwę i liczbę jako cenę.");
                return;
            }

            ProductName = ProductNameTextBox.Text;
            ProductPrice = price;
            IsDigitalProduct = DigitalRadio.IsChecked == true;

            this.DialogResult = true;
            this.Close();
        }

        private void PhysicalRadio_Checked(object sender, RoutedEventArgs e)
        {

        }
    }
}