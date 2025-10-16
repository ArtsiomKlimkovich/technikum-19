using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SpokojnySklep.classes
{
    internal class FixedAmountDiscount : IDiscountStrategy
    {
        public int CalculateDiscount(int price, int discount)
        {
            return price - discount;
        }
    }
}
