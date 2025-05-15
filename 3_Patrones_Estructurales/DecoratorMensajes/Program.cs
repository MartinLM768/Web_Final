using System;

namespace DecoratorMensajes
{
    class Program
    {
        static void Main(string[] args)
        {
            // Mensaje simple
            IMensaje mensaje = new MensajeBase();

            // Decorar con cifrado
            IMensaje mensajeCifrado = new CifradoDecorator(mensaje);

            // Decorar con compresión también
            IMensaje mensajeFinal = new CompresionDecorator(mensajeCifrado);

            mensajeFinal.Enviar("ay mi gatito miau miau");
        }
    }
}
