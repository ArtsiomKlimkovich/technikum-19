using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SpokojnySklep.classes
{
    internal class PercentageDiscount : IDiscountStrategy
    {
        public int CalculateDiscount(int price, int percentageDiscount)
        {
            return (price * (100 - percentageDiscount)) / 100;
        }
    }
}
