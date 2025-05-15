namespace AbstractFactoryGUI {
    public class LinuxButton : IButton {
        public void Render() {
            System.Console.WriteLine("Renderizando botón en Linux");
        }
    }

    public class LinuxWindow : IWindow {
        public void Show() {
            System.Console.WriteLine("Mostrando ventana en Linux");
        }
    }

    public class LinuxFactory : IGUIFactory {
        public IButton CreateButton() => new LinuxButton();
        public IWindow CreateWindow() => new LinuxWindow();
    }
}
