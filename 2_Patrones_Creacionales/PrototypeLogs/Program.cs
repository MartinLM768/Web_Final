using System;

namespace PrototypeLogs
{
    // Interface Prototype
    public interface ILogMessage : ICloneable
    {
        void PrintMessage();
    }

    // Clase concreta de LogMessage de tipo Info
    public class InfoLog : ILogMessage
    {
        public string Message { get; set; }
        public DateTime Timestamp { get; set; }

        public InfoLog(string message)
        {
            Message = message;
            Timestamp = DateTime.Now;
        }

        public void PrintMessage()
        {
            Console.WriteLine($"[INFO] {Timestamp}: {Message}");
        }

        public object Clone()
        {
            // Copia superficial está bien aquí
            return this.MemberwiseClone();
        }
    }

    // Clase concreta de LogMessage de tipo Error
    public class ErrorLog : ILogMessage
    {
        public string Message { get; set; }
        public int ErrorCode { get; set; }
        public DateTime Timestamp { get; set; }

        public ErrorLog(string message, int errorCode)
        {
            Message = message;
            ErrorCode = errorCode;
            Timestamp = DateTime.Now;
        }

        public void PrintMessage()
        {
            Console.WriteLine($"[ERROR] {Timestamp}: Código {ErrorCode} - {Message}");
        }

        public object Clone()
        {
            return this.MemberwiseClone();
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Creamos un mensaje base de info
            InfoLog baseInfo = new InfoLog("Sistema iniciado");
            baseInfo.PrintMessage();

            // Clonamos y modificamos el mensaje
            InfoLog newInfo = (InfoLog)baseInfo.Clone();
            newInfo.Message = "Usuario autenticado";
            newInfo.Timestamp = DateTime.Now;
            newInfo.PrintMessage();

            // Creamos un mensaje base de error
            ErrorLog baseError = new ErrorLog("Fallo de conexión", 500);
            baseError.PrintMessage();

            // Clonamos y modificamos el mensaje de error
            ErrorLog newError = (ErrorLog)baseError.Clone();
            newError.Message = "Error al guardar datos";
            newError.ErrorCode = 501;
            newError.Timestamp = DateTime.Now;
            newError.PrintMessage();
        }
    }
}
