namespace FacadeFacturacion
{
    public class FacturacionFacade
    {
        private Cliente cliente;
        private Producto producto;
        private Pago pago;

        public FacturacionFacade()
        {
            cliente = new Cliente();
            producto = new Producto();
            pago = new Pago();
        }

        public void RealizarFacturacion()
        {
            Console.WriteLine("---- Iniciando Facturación ----");
            cliente.ObtenerDatosCliente();
            producto.CalcularTotal();
            pago.ProcesarPago();
            Console.WriteLine("---- Facturación Completada ----");
        }
    }
}
