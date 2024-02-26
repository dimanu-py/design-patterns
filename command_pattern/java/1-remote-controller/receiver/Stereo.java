package receiver;


/**
 * Represents the stereo.
 * The stereo can be turned on, off, set for CD input, set for DVD input, set for Radio input and set volume.
 */
public class Stereo {

    private String state;
    String location;
    int volume;

    public Stereo(String location){
        this.location = location;
        this.state = "off";
        this.volume = 0;
    }

    public void on() {
        this.state = "on";
        System.out.println("Stereo is " + this.state);
    }

    public void off() {
        this.state = "off";
        System.out.println("Stereo is " + this.state);
    }

    public void setCD() {
        System.out.println("Stereo is set for CD input");
    }

    public void setDVD() {
        System.out.println("Stereo is set for DVD input");
    }

    public void setRadio() {
        System.out.println("Stereo is set for Radio input");
    }

    public void setVolume(int volume) {
        this.volume = volume;
        System.out.println("Stereo volume set to " + this.volume);
    }
}
