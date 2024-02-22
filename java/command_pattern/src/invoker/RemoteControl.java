package invoker;

import command.Command;
import command.NoCommand;

public class RemoteControl {
    
    private static final int SLOTS = 7;
    Command[] onCommands;
    Command[] offCommands;
    Command undoCommand;

    public RemoteControl() {
        onCommands = new Command[SLOTS];
        offCommands = new Command[SLOTS];

        Command defaultCommand = new NoCommand();
        for(int i = 0; i < SLOTS; i++) {
            onCommands[i] = defaultCommand;
            offCommands[i] = defaultCommand;
        }
        undoCommand = defaultCommand;
    }

    public void setCommand(int slot, Command onCommand, Command offCommand) {
        onCommands[slot] = onCommand;
        offCommands[slot] = offCommand;
    }

    public void onButtonWasPressed(int slot) {
        onCommands[slot].execute();
        undoCommand = onCommands[slot];
    }

    public void offButtonWasPressed(int slot) {
        offCommands[slot].execute();
        undoCommand = offCommands[slot];
    }

    public void undoButtonWasPressed() {
        undoCommand.undo();
    }

    public String toString() {
        StringBuffer stringBuff = new StringBuffer();
        stringBuff.append("\n------ Remote Control ------\n");
        for(int i = 0; i < SLOTS; i++) {
            stringBuff.append("[slot " + i + "] " + onCommands[i].getClass().getName() + "    " + offCommands[i].getClass().getName() + "\n");
        }
        stringBuff.append("[undo] " + undoCommand.getClass().getName() + "\n");
        return stringBuff.toString();
    }
}
