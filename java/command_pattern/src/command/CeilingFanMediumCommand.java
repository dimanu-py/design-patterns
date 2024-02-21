package command;

import receiver.CeilingFan;

public class CeilingFanMediumCommand implements Command {
    
    CeilingFan ceilingFan;

    public CeilingFanMediumCommand(CeilingFan ceilingFan) {
        this.ceilingFan = ceilingFan;
    }

    public void execute() {
        ceilingFan.medium();
    }
}
