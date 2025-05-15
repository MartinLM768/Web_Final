namespace AbstractFactoryGUI {
    public class MacButton : IButton {
        public void Render() {
            System.Console.WriteLine("Renderizando botón en Mac");
        }
    }

    public class MacWindow : IWindow {
        public void Show() {
            System.Console.WriteLine("Mostrando ventana en Mac");
        }
    }

    public class MacFactory : IGUIFactory {
        public IButton CreateButton() => new MacButton();
        public IWindow CreateWindow() => new MacWindow();
    }
}
