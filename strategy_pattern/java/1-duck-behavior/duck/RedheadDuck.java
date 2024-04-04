package duck;


public class RedheadDuck extends Duck implements Flyable, Quackable {

    public void display() {
        System.out.println("I'm a Redhead Duck");
    }

    public void fly() {
        System.out.println("I'm flying");
    }

    public void quack() {
        System.out.println("Quack");
    }

}