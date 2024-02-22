package command;

import receiver.CeilingFan;

public class CeilingFanHighCommand implements Command {
        
        CeilingFan ceilingFan;
        int previousSpeed;
        
        public CeilingFanHighCommand(CeilingFan ceilingFan) {
            this.ceilingFan = ceilingFan;
            this.previousSpeed = 0;
        }
        
        public void execute() {
            previousSpeed = ceilingFan.getSpeed();
            ceilingFan.high();
        }

        public void undo(){
            if(previousSpeed == CeilingFan.HIGH) {
                ceilingFan.high();
            } else if(previousSpeed == CeilingFan.MEDIUM) {
                ceilingFan.medium();
            } else if(previousSpeed == CeilingFan.LOW) {
                ceilingFan.low();
            } else if(previousSpeed == CeilingFan.OFF) {
                ceilingFan.off();
            }
        }
        
}
