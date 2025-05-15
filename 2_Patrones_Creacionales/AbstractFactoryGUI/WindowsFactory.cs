namespace AbstractFactoryGUI {
    public class WindowsButton : IButton {
        public void Render() {
            System.Console.WriteLine("Renderizando botón en Windows");
        }
    }

    public class WindowsWindow : IWindow {
        public void Show() {
            System.Console.WriteLine("Mostrando ventana en Windows");
        }
    }

    public class WindowsFactory : IGUIFactory {
        public IButton CreateButton() => new WindowsButton();
        public IWindow CreateWindow() => new WindowsWindow();
    }
}
