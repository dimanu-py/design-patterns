package command;

import receiver.GarageDoor;

public class GarageDoorCloseCommand implements Command {
        
        GarageDoor garageDoor;
        
        public GarageDoorCloseCommand(GarageDoor garageDoor) {
            this.garageDoor = garageDoor;
        }
        
        public void execute() {
            garageDoor.close();
            garageDoor.lightOff();
        }

        public void undo(){
            garageDoor.open();
            garageDoor.lightOn();
        }
}
