package command;

import receiver.Account;

public class TransferCommand implements Transaction {

    private Account fromAccount;
    private Account toAccount;
    private float amount;

    public TransferCommand(Account fromAccount, Account toAccount, float amount) {
        this.fromAccount = fromAccount;
        this.toAccount = toAccount;
        this.amount = amount;
    }
    
    public void execute() {
        fromAccount.withdraw(amount);
        toAccount.deposit(amount);
    }

    public void undo() {
        toAccount.withdraw(amount);
        fromAccount.deposit(amount);
    }

    public void redo() {
        fromAccount.withdraw(amount);
        toAccount.deposit(amount);
    }
}
