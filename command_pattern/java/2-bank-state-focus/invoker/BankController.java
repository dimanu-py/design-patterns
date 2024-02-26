package invoker;

import java.util.ArrayList;
import java.util.List;

import command.Transaction;

public class BankController {
    
    private List<Transaction> undoStack;
    private List<Transaction> redoStack;

    public BankController() {
        this.undoStack = new ArrayList<>();
        this.redoStack = new ArrayList<>();
    }

    public void execute(Transaction transaction) {
        transaction.execute();
        undoStack.add(transaction);
        redoStack.clear();
    }

    public void undo() {
        if (undoStack.isEmpty()) {
            return;
        }
        Transaction transaction = undoStack.remove(undoStack.size() - 1);
        transaction.undo();
        redoStack.add(transaction);
    }

    public void redo() {
        if (redoStack.isEmpty()) {
            return;
        }
        Transaction transaction = redoStack.remove(redoStack.size() - 1);
        transaction.redo();
        undoStack.add(transaction);
    }
}
