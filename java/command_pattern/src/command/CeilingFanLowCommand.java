package command;

import receiver.CeilingFan;

public class CeilingFanLowCommand implements Command {
    
    CeilingFan ceilingFan;

    public CeilingFanLowCommand(CeilingFan ceilingFan) {
        this.ceilingFan = ceilingFan;
    }

    public void execute() {
        ceilingFan.low();
    }
}
