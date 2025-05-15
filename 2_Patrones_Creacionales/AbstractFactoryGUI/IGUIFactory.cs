namespace AbstractFactoryGUI {
    public interface IGUIFactory {
        IButton CreateButton();
        IWindow CreateWindow();
    }
}
