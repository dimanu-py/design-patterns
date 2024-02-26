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
    from bank_controller import BankController
    from transaction import DepositCommand, WithDrawCommand, TransferCommand

    bank = Bank()
    controller = BankController()

    account_one = bank.create_account('Apple')
    account_two = bank.create_account('Tesla')
    account_three = bank.create_account('Microsoft')

    controller.execute(DepositCommand(account_one, 1000))
    controller.execute(DepositCommand(account_two, 2000))
    controller.execute(DepositCommand(account_three, 3000))

    print(bank)

    controller.undo()

    print(bank)

    controller.execute(WithDrawCommand(account_one, 500))
    controller.redo()

    print(bank)

    controller.execute(TransferCommand(account_one, account_two, 500))

    print(bank)

    controller.undo()
