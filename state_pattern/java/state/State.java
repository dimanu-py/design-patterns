package state_pattern.java.state;

public interface State {
    
    public void insertQuarter();

    public void ejectQuarter();

    public void turnCrank();

    public void dispense();
}

