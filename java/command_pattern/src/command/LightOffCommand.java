package command;

import receiver.Light;


/**
 * This is the concrete command to switch a light off. It is used to encapsulate the receiver object and the action to be performed.
 */
public class LightOffCommand implements Command {

    Light light;

    public LightOffCommand(Light light) {
        this.light = light;
    }

    public void execute() {
        light.off();
    }

    public void undo(){
        light.on();
    }
    
}
