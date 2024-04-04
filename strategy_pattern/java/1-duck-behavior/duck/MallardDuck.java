package duck;


public class MallardDuck extends Duck implements Flyable, Quackable {

    public void display() {
        System.out.println("I'm a Mallard Duck");
    }

    public void fly() {
        System.out.println("I'm flying");
    }

    public void quack() {
        System.out.println("Quack");
    }

}
