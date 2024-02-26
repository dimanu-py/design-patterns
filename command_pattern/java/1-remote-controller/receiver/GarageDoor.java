package receiver;


/**
 * Represents the garage door.
 * The door can be opened, closed or stopped. Its light is turned on or off depending on the state of the door.
*/
public class GarageDoor {

    private String door;
    String location;

    public GarageDoor(String location){
        this.location = location;
        this.door = "closed";
    }

    public void open() {
        this.door = "open";
        System.out.println("Garage door is " + this.door);
    }

    public void close() {
        this.door = "closed";
        System.out.println("Garage door is " + this.door);
    }

    public void stop() {
        this.door = "stopped";
        System.out.println("Garage door is " + this.door);
    }

    public void lightOn() {
        System.out.println("Garage light is on");
    }

    public void lightOff() {
        System.out.println("Garage light is off");
    }
}
