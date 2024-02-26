package command;

import receiver.Stereo;

public class StereoOffWithDVDCommand implements Command {
    
    Stereo stereo;
    
    public StereoOffWithDVDCommand(Stereo stereo) {
        this.stereo = stereo;
    }
    
    public void execute() {
        stereo.off();
    }

    public void undo(){
        stereo.on();
        stereo.setDVD();
        stereo.setVolume(11);
    }
}
