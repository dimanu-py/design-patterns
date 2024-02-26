package command;

import receiver.Account;


public class DepositCommand implements Transaction {

    private Account account;
    private float amount;

    public DepositCommand(Account account, float amount) {
        this.account = account;
        this.amount = amount;
    }

    public void execute() {
        account.deposit(amount);
    }

    public void undo() {
        account.withdraw(amount);
    }

    public void redo() {
        account.deposit(amount);
    }
    
}
