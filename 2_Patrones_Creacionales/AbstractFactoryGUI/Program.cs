using AbstractFactoryGUI;

class Program {
    static void Main() {
        // Puedes cambiar el sistema operativo aquí:
        IGUIFactory factory = new WindowsFactory();
        App app = new App(factory);
        app.Run();

        // factory = new LinuxFactory(); // para probar Linux
        // factory = new MacFactory();   // para probar Mac
    }
}
