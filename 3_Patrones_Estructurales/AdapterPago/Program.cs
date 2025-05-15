using System;

namespace AdapterPago
{
    class Program
    {
        static void Main(string[] args)
        {
            IPago pago = new PagoAdapter();

            pago.RealizarPago(150.00);
        }
    }
}
