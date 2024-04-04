package duck;

public class DecoyDuck extends Duck {

    public void quack() {
        System.out.println("Silence");
    }

    public void display() {
        System.out.println("I'm a Decoy duck");
    }

    public void fly() {
        System.out.println("I can't fly");
    }

}