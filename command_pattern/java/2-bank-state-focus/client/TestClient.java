package client;

import command.DepositCommand;
import command.WithDrawCommand;
import command.TransferCommand;
import invoker.BankController;
import receiver.Account;

public class TestClient {
    
    public static void main(String[] args){

        Bank bank = new Bank();
        BankController controller = new BankController();

        Account accountOne = bank.createAccount("Apple");
        Account accountTwo = bank.createAccount("Tesla");
        Account accountThree = bank.createAccount("Microsoft");

        controller.execute(new DepositCommand(accountOne, 1000));
        controller.execute(new DepositCommand(accountTwo, 2000));
        controller.execute(new DepositCommand(accountThree, 3000));

        controller.undo();

        controller.execute(new WithDrawCommand(accountOne, 500));
        controller.redo();

        controller.execute(new TransferCommand(accountOne, accountTwo, 500));

    }
}
