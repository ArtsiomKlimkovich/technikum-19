using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace SpokojnySklep.classes
{
    internal abstract class Product
    {
        public string Nazwa;
        public int Cena;

        protected Product(string nazwa, int cena)
        {
            Nazwa = nazwa;
            Cena = cena;
        }
    }
}
