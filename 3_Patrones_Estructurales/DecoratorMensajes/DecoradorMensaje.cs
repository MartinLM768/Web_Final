namespace DecoratorMensajes
{
    public abstract class DecoradorMensaje : IMensaje
    {
        protected IMensaje mensaje;

        public DecoradorMensaje(IMensaje mensaje)
        {
            this.mensaje = mensaje;
        }

        public virtual void Enviar(string contenido)
        {
            mensaje.Enviar(contenido);
        }
    }
}
