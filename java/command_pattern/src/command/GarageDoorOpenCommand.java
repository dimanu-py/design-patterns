package command;

import receiver.GarageDoor;

public class GarageDoorOpenCommand implements Command {
        
        GarageDoor garageDoor;
        
        public GarageDoorOpenCommand(GarageDoor garageDoor) {
            this.garageDoor = garageDoor;
        }
        
        public void execute() {
            garageDoor.open();
            garageDoor.lightOn();
        }
}
