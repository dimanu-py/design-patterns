package client;
import java.util.HashMap;
import java.util.Random;

import receiver.Account;


public class Bank {

    private HashMap<String, Account> accounts;
    
    public Bank() {
        this.accounts = new HashMap<>();
    }

    public void createAccount(String name) {
        String number = generateRandomNumber();
        Account account = new Account(name, number);
        accounts.put(number, account);
    }

    public Account getAccount(String number) {
        return accounts.get(number);
    }

    private String generateRandomNumber() {
        Random random = new Random();
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < 10; i++) {
            builder.append(random.nextInt(10));
        }
        return builder.toString();
    }
}
