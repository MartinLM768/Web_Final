namespace AbstractFactoryGUI {
    public class App {
        private IButton button;
        private IWindow window;

        public App(IGUIFactory factory) {
            button = factory.CreateButton();
            window = factory.CreateWindow();
        }

        public void Run() {
            button.Render();
            window.Show();
        }
    }
}
