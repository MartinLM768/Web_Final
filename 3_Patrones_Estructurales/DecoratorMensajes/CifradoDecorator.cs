using System;

namespace DecoratorMensajes
{
    public class CifradoDecorator : DecoradorMensaje
    {
        public CifradoDecorator(IMensaje mensaje) : base(mensaje) {}

        public override void Enviar(string contenido)
        {
            string contenidoCifrado = $"***{contenido}*** (cifrado)";
            base.Enviar(contenidoCifrado);
        }
    }
}
