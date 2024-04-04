

public class MiniDuckSimulator {

    public static void main(String[] args) {
        Duck mallard = new MallardDuck();
        mallard.display();
        mallard.fly();
        mallard.quack();

        Duck decoy = new DecoyDuck();
        decoy.display();
        decoy.fly();
        decoy.quack();
    }
}