from dataclasses import dataclass, field
from account import Account
import random
import string


@dataclass
class Bank:
    """
    The bank object will be our client in the command pattern.
    """
    
    accounts: dict[str, Account] = field(default_factory=dict)
    
    def create_account(self, name: str) -> Account:
        number = "".join(random.choices(string.digits, k=10))
        account = Account(name, number)
        self.accounts[number] = account
        return account
    
    def get_account(self, number: str) -> Account:
        return self.accounts.get(number, None)


if __name__ == '__main__':

    bank = Bank()

    account_one = bank.create_account('Apple')
    account_two = bank.create_account('Tesla')
    account_three = bank.create_account('Microsoft')

    account_one.deposit(1000)
    account_two.deposit(2000)
    account_three.deposit(3000)

    account_one.withdraw(500)
    account_two.withdraw(1000)

    print(bank)