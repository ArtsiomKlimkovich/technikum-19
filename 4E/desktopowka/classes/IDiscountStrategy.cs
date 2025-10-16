using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SpokojnySklep.classes
{
    internal interface IDiscountStrategy // Strategy - programming template
    {
        int CalculateDiscount(int price, int discount);
    }
}
