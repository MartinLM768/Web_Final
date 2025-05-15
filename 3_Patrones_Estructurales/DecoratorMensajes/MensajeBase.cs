using System;

namespace DecoratorMensajes
{
    public class MensajeBase : IMensaje
    {
        public void Enviar(string contenido)
        {
            Console.WriteLine($"Mensaje enviado: {contenido}");
        }
    }
}
