package duck;


public class RedheadDuck extends Duck {

    public ReadheadDuck() {
        quackBehavior = new Quack();
        flyBehavior = new FlyWithWings();
    }

    public void display() {
        System.out.println("I'm a Redhead Duck");
    }

}