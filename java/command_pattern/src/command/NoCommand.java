package command;

/*
 * This is a null object pattern. It is used to avoid null pointer exceptions.
 */
public class NoCommand implements Command {
    public void execute() {
        System.out.println("No command");
    }
}
