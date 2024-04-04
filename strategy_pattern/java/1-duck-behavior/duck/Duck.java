package duck;


public abstract class Duck {

    FlyBehavior flyBehavior;
    QuackBehavior quackBehavior;

    public Duck() {}

    public void quack() {
        quackBehavior.quack();
    }

    public void swim() {
        System.out.println("Swim");
    }

    public abstract void display();

    public void fly() {
        flyBehavior.fly();
    }

    public void setFlyBehavior(FlyBehavior behavior) {
        flyBehavior = behavior;
    }

    public void setQuackBehavior(QuackBehavior behavior) {
        quackBehavior = behavior;
    }

}