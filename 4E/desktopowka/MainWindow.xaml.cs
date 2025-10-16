using SpokojnySklep.classes;
using System;
using System.Windows;

namespace SpokojnySklep
{
    public partial class MainWindow : Window
    {
        private Cart cart;
        private int currentIndex = 0;

        public MainWindow()
        {
            InitializeComponent();
            cart = new Cart();
            ShowCurrentProduct();
            UpdateButtonStates();
            this.KeyDown += MainWindow_KeyDown;
        }

        private void MainWindow_KeyDown(object sender, System.Windows.Input.KeyEventArgs e)
        {
            if (e.Key == System.Windows.Input.Key.A && (System.Windows.Input.Keyboard.Modifiers & System.Windows.Input.ModifierKeys.Control) == System.Windows.Input.ModifierKeys.Control)
            {
                var addProductWindow = new AddProductWindow();
                addProductWindow.Owner = this;

                if (addProductWindow.ShowDialog() == true)
                {
                    if (addProductWindow.IsDigitalProduct)
                    {
                        cart.Products.Add(new DigitalProduct(addProductWindow.ProductName, addProductWindow.ProductPrice));
                    }
                    else
                    {
                        cart.Products.Add(new PhysicalProduct(addProductWindow.ProductName, addProductWindow.ProductPrice));
                    }

                    currentIndex = cart.Products.Count - 1;
                    ShowCurrentProduct();
                }

            }
        }

        private void ShowCurrentProduct()
        {
            if (cart.Products.Count == 0) return;

            var current = cart.Products[currentIndex];
            Dane.Text = current.Nazwa;
            Cena.Text = current.Cena.ToString("0.00");

            UpdateButtonStates();
        }

        private void bNext_Click(object sender, RoutedEventArgs e)
        {
            if (currentIndex < cart.Products.Count - 1)
            {
                currentIndex++;
                ShowCurrentProduct();
            }
        }

        private void bPrev_Click(object sender, RoutedEventArgs e)
        {
            if (currentIndex > 0)
            {
                currentIndex--;
                ShowCurrentProduct();
            }
        }

        private void UpdateButtonStates()
        {
            bPrev.IsEnabled = currentIndex > 0;
            bNext.IsEnabled = currentIndex < cart.Products.Count - 1;
        }

        private void CalculateDiscount_Click(object sender, RoutedEventArgs e)
        {
            if (cart.Products.Count == 0) return;

            int discountValue;
            if (!int.TryParse(DiscountInput.Text, out discountValue))
            {
                MessageBox.Show("Nieprawidłowa wartość rabatu.");
                return;
            }

            IDiscountStrategy discountStrategy;

            if (PercentRadio.IsChecked == true)
            {
                discountStrategy = new PercentageDiscount();
            }
            else if (FixedRadio.IsChecked == true)
            {
                discountStrategy = new FixedAmountDiscount();
            }
            else
            {
                MessageBox.Show("Wybierz typ rabatu.");
                return;
            }

            int originalPrice = cart.CalculateCartValue();
            int finalPrice = cart.CalculateCartValueWithDiscount(discountStrategy, discountValue);

            BeforePrice.Content = $"Przed: {originalPrice:0.00} zł";
            AfterPrice.Content = $"Po: {finalPrice:0.00} zł";
        }
    }
}