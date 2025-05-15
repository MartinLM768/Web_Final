namespace AdapterPago
{
    public class PagoAdapter : IPago
    {
        private PagoExterno pagoExterno;

        public PagoAdapter()
        {
            pagoExterno = new PagoExterno();
        }

        public void RealizarPago(double monto)
        {
            Console.WriteLine("[ADAPTADOR] Traduciendo llamada interna a API externa...");
            pagoExterno.ProcesarPago(monto);
        }
    }
}
