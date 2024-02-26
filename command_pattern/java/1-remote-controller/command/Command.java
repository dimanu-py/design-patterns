package command;


/**
 * The command object is the one that encapsulates the receiver object and the action to be performed.
 */
public interface Command {
    public void execute();
    public void undo();
}
