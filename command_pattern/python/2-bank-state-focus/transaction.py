"""This transaction will model our command object. It would be the equivalent of the Command interface in the remote controller example"""
from typing import Protocol

from account import Account


class Transaction(Protocol):
    """A transaction that can be executed, undone, and redone."""

    def execute(self) -> None:
        """Execute the transaction."""

    def undo(self) -> None:
        """Undo the transaction."""

    def redo(self) -> None:
        """Redo the transaction."""


class DepositCommand:
    """Command to do deposits into an account."""

    def __init__(self, account: Account, amount: int) -> None:
        self.account = account
        self.amount = amount

    def execute(self) -> None:
        self.account.deposit(self.amount)

    def undo(self) -> None:
        self.account.withdraw(self.amount)

    def redo(self) -> None:
        self.account.deposit(self.amount)


class WithDrawCommand:
    """Command to withdraw money from an account."""

    def __init__(self, account: Account, amount: int) -> None:
        self.account = account
        self.amount = amount

    def execute(self) -> None:
        self.account.withdraw(self.amount)

    def undo(self) -> None:
        self.account.deposit(self.amount)

    def redo(self) -> None:
        self.account.withdraw(self.amount)


class TransferCommand:
    """Command to do a transfer from one account to another."""

    def __init__(self, from_account: Account, to_account: Account, amount: int) -> None:
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount

    def execute(self) -> None:
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)

    def undo(self) -> None:
        self.to_account.withdraw(self.amount)
        self.from_account.deposit(self.amount)

    def redo(self) -> None:
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)