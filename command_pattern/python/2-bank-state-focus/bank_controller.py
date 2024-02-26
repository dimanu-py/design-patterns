from transaction import Transaction


class BankController:
    """This class will be our invoker. It will be responsible for executing the transactions."""

    def __init__(self) -> None:
        self.undo_stack = []
        self.redo_stack = []

    def execute(self, transaction: Transaction) -> None:
        transaction.execute()
        self.redo_stack.clear()
        self.undo_stack.append(transaction)

    def undo(self) -> None:
        if not self.undo_stack:
            return

        transaction = self.undo_stack.pop()
        transaction.undo()
        self.redo_stack.append(transaction)

    def redo(self) -> None:
        if not self.redo_stack:
            return

        transaction = self.redo_stack.pop()
        transaction.redo()
        self.undo_stack.append(transaction)