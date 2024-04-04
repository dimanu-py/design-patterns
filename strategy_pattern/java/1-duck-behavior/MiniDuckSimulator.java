

public class MiniDuckSimulator {

    public static void main(String[] args) {
        Duck mallard = new MallardDuck();
        mallard.display();
        mallard.fly();
        mallard.quack();
        mallard.setFlyBehavior(new FlyRocketPowered());
        mallard.fly()

        Duck decoy = new DecoyDuck();
        decoy.display();
        decoy.fly();
        decoy.quack();
        decoy.setQuackBehavior(new Quack());
        decoy.quack();
    }
}