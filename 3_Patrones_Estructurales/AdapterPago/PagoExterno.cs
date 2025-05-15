namespace AdapterPago
{
    public class PagoExterno
    {
        public void ProcesarPago(double cantidad)
        {
            Console.WriteLine($"[API EXTERNA] Pago procesado por ${cantidad}");
        }
    }
}
