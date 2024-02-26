package command;

import receiver.Account;


public class WithDrawCommand implements Transaction {

    private Account account;
    private float amount;
    
    public WithDrawCommand(Account account, float amount) {
        this.account = account;
        this.amount = amount;
    }

    public void execute() {
        account.withdraw(amount);
    }

    public void undo() {
        account.deposit(amount);
    }

    public void redo() {
        account.withdraw(amount);
    }
}
