using System;

namespace FacadeFacturacion
{
    class Program
    {
        static void Main(string[] args)
        {
            FacturacionFacade facturacion = new FacturacionFacade();
            facturacion.RealizarFacturacion();
        }
    }
}
