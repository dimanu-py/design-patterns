package command;

import receiver.Light;


/**
 * This is the concrete command to switch a light on. It is used to encapsulate the receiver object and the action to be performed.
 */
public  class LightOnCommand implements Command {

    Light light;

    public LightOnCommand(Light light) {
        this.light = light;
    }

    public void execute() {
        light.on();
    }
    
}
