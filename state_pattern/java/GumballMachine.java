package state_pattern.java;

import state_pattern.java.state.HasQuarterState;
import state_pattern.java.state.NoQuarterState;
import state_pattern.java.state.SoldOutState;
import state_pattern.java.state.SoldState;
import state_pattern.java.state.State;

public class GumballMachine {
    
    State soldOutState;
    State noQuarterState;
    State hasQuarterState;
    State soldState;

    State state = soldOutState;
    int numberGumballs = 0;

    public GumballMachine(int numberGumballs) {
        
        soldOutState = new SoldOutState(this);
        noQuarterState = new NoQuarterState(this);
        hasQuarterState = new HasQuarterState(this);
        soldState = new SoldState(this);
        
        this.numberGumballs = numberGumballs;

        if (numberGumballs > 0) {
            state = noQuarterState;
        }
    }

    public void insertQuarter() {
        state.insertQuarter();
    }

    public void ejectQuarter() {
        state.ejectQuarter();
    }

    public void turnCrank() {
        state.turnCrank();
    }

    public void dispense() {
        state.dispense();
    }

    public void setState(State state) {
        this.state = state;
    }

    public void releaseBall() {
        System.out.println("A gumball comes rolling out the slot...");
        if (numberGumballs != 0) {
            numberGumballs = numberGumballs - 1;
        }
    }

    public State getSoldOutState() {
        return soldOutState;
    }

    public State getNoQuarterState() {
        return noQuarterState;
    }

    public State getHasQuarterState() {
        return hasQuarterState;
    }

    public State getSoldState() {
        return soldState;
    }

    public int getNumberGumballs() {
        return numberGumballs;
    }

}
