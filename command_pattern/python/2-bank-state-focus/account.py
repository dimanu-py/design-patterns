from dataclasses import dataclass


@dataclass
class Account:
    """
    The account object will be our receiver object.

    It will be the object that knows how to execute the action that the command object will encapsulate.
    """

    name: str
    number: str
    balance: float = 0.0
    
    def deposit(self, amount: float) -> None:
        self.balance += amount
        
    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        
        self.balance -= amount