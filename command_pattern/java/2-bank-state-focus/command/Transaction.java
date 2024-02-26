package command;


public interface Transaction {
    
    public void execute();

    public void undo();

    public void redo();

}
