using System;

namespace DecoratorMensajes
{
    public class CompresionDecorator : DecoradorMensaje
    {
        public CompresionDecorator(IMensaje mensaje) : base(mensaje) {}

        public override void Enviar(string contenido)
        {
            string contenidoComprimido = $"<{contenido}> (comprimido)";
            base.Enviar(contenidoComprimido);
        }
    }
}
