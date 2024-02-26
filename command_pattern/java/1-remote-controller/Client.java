import command.CeilingFanHighCommand;
import command.CeilingFanLowCommand;
import command.CeilingFanMediumCommand;
import command.GarageDoorCloseCommand;
import command.GarageDoorOpenCommand;
import command.LightOffCommand;
import command.LightOnCommand;
import command.StereoOffWithDVDCommand;
import command.StereoOnWithCDCommand;
import command.MacroCommand;
import invoker.RemoteControl;
import receiver.CeilingFan;
import receiver.GarageDoor;
import receiver.Light;
import receiver.Stereo;


public class Client {
    
    public static void main(String[] args){
        RemoteControl remoteControl = new RemoteControl();
        
        Light livingRoomLight = new Light("Living Room");
        Light kitchenLight = new Light("Kitchen");
        CeilingFan ceilingFan = new CeilingFan("Living Room");
        GarageDoor garageDoor = new GarageDoor("");
        Stereo stereo = new Stereo("Living Room");
        
        LightOnCommand livingRoomLightOn = new LightOnCommand(livingRoomLight);
        LightOffCommand livingRoomLightOff = new LightOffCommand(livingRoomLight);
        LightOnCommand kitchenLightOn = new LightOnCommand(kitchenLight);
        LightOffCommand kitchenLightOff = new LightOffCommand(kitchenLight);
        
        CeilingFanHighCommand ceilingFanHigh = new CeilingFanHighCommand(ceilingFan);
        CeilingFanMediumCommand ceilingFanMedium = new CeilingFanMediumCommand(ceilingFan);
        CeilingFanLowCommand ceilingFanLow = new CeilingFanLowCommand(ceilingFan);
        
        GarageDoorOpenCommand garageDoorUp = new GarageDoorOpenCommand(garageDoor);
        GarageDoorCloseCommand garageDoorDown = new GarageDoorCloseCommand(garageDoor);
        
        StereoOnWithCDCommand stereoOnWithCD = new StereoOnWithCDCommand(stereo);
        StereoOffWithDVDCommand stereoOffWithDVD = new StereoOffWithDVDCommand(stereo);

        Command[] partyOn = {livingRoomLightOn, ceilingFanHigh, stereoOnWithCD};
        Command[] partyOff = {livingRoomLightOff, ceilingFanLow, stereoOffWithDVD};
        MacroCommand partyOnMacro = new MacroCommand(partyOn);
        MacroCommand partyOffMacro = new MacroCommand(partyOff);
        
        remoteControl.setCommand(0, livingRoomLightOn, livingRoomLightOff);
        remoteControl.setCommand(1, kitchenLightOn, kitchenLightOff);
        remoteControl.setCommand(2, garageDoorUp, garageDoorDown);
        remoteControl.setCommand(3, stereoOnWithCD, stereoOffWithDVD);
        remoteControl.setCommand(4, partyOnMacro, partyOffMacro);
        
        System.out.println(remoteControl);
        
        remoteControl.onButtonWasPressed(0);
        remoteControl.undoButtonWasPressed();

        System.out.println(remoteControl);

        remoteControl.offButtonWasPressed(0);
        remoteControl.onButtonWasPressed(1);
        remoteControl.offButtonWasPressed(1);
        remoteControl.onButtonWasPressed(2);
        remoteControl.offButtonWasPressed(2);
        remoteControl.undoButtonWasPressed();

        System.out.println(remoteControl);
        
        remoteControl.onButtonWasPressed(3);

        System.out.println("\n--- Pushing Macro On ---\n");
        remoteControl.onButtonWasPressed(4);
        System.out.println("\n--- Pushing Macro Off ---\n");
        remoteControl.offButtonWasPressed(4);
    }
}
