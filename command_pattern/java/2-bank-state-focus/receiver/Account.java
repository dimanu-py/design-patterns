package receiver;


public class Account {

    String name;
    String number;
    private float balance;

    public Account(String name, String number) {
        this.name = name;
        this.number = number;
        this.balance = 0;
    }

    public void deposit(float amount) {
        this.balance += amount;
    }

    public void withdraw(float amount) {

        if (amount > this.balance) {
            throw new IllegalArgumentException("Insufficient funds");
        }
        this.balance -= amount;
    }
}