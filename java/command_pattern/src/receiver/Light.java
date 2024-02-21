package receiver;


/**
 * Represents a light.
 * The light can be turned on or off.
 */
public class Light {
    private String bulb;
    String location;

    public Light(String location){
        this.location = location;
        this.bulb = "off";
    }

    public void on() {
        this.bulb = "on";
        System.out.println("Light is " + this.bulb);
    }

    public void off() {
        this.bulb = "off";
        System.out.println("Light is " + this.bulb);
    }
}
