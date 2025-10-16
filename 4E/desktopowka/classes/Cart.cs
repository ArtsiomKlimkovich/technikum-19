using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SpokojnySklep.classes
{
    internal class Cart
    {
        public IDiscountStrategy DiscountStrategy;
        public List<Product> Products;

        public Cart()
        {
            Products = new List<Product>();
            GenerateSampleProducts();
        }

        private void GenerateSampleProducts(){
            Products.Add(new PhysicalProduct("Chleb", 4));
            //Products.Add(new PhysicalProduct("Mleko", 3));
            //Products.Add(new PhysicalProduct("Masło", 7));
            //Products.Add(new PhysicalProduct("Ser", 12));

            Products.Add(new DigitalProduct("E-book", 15));
            //Products.Add(new DigitalProduct("Licencja Windows", 399));
            //Products.Add(new DigitalProduct("Subskrypcja Spotify", 20));
            //Products.Add(new DigitalProduct("Gra na Steam", 120));
        }

        public int CalculateCartValue()
        {
            int value = 0;
            foreach (var item in Products)
            {
                value += item.Cena;
            }
            return value;
        }

        public int CalculateCartValueWithDiscount(IDiscountStrategy discountStrategy, int discountValue)
        {
            this.DiscountStrategy = discountStrategy;
            int cartValue = CalculateCartValue();
            return DiscountStrategy.CalculateDiscount(cartValue, discountValue);
        }
    }
}
