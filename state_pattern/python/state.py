from abc import ABC, abstractmethod

from gumball_machine import GumballMachine


class State(ABC):
    
    def __init__(self, gumball_machine: GumballMachine) -> None:
        self.gumball_machine = gumball_machine
            
    @abstractmethod
    def insert_quarter(self) -> None:
        pass
    
    @abstractmethod
    def eject_quarter(self) -> None:
        pass
    
    @abstractmethod
    def turn_crank(self) -> None:
        pass
    
    @abstractmethod
    def dispense(self) -> None:
        pass
    

class SoldOutState(State):
    
    def insert_quarter(self):
        print("You can't insert a quarter, the machine is sold out")
        
    def eject_quarter(self) -> None:
        print("You can't eject, you haven't inserted a quarter yet")
        
    def turn_crank(self) -> None:
        print("You turned, but there are no gumballs")
        
    def dispense(self) -> None:
        print("No gumball dispensed")
        

class SoldState(State):
    
    def insert_quarter(self) -> None:
        print("Please wait, we're already giving you a gumball")
        
    def eject_quarter(self) -> None:
        print("Sorry, you already turned the crank")
        
    def turn_crank(self) -> None:
        print("Turning twice doesn't get you another gumball!")
        
    def dispense(self) -> None:
        self.gumball_machine.release_ball()
        
        if self.gumball_machine.number_gumballs == 0:
            print("Oops, out of gumballs!")
            self.gumball_machine.set_state(self.gumball_machine.sold_out_state)


class NoQuarterState(State):
    
    def insert_quarter(self) -> None:
        print("You inserted a quarter")
        self.gumball_machine.set_state(self.gumball_machine.has_quarter_state)
        
    def eject_quarter(self) -> None:
        print("You haven't inserted a quarter")
        
    def turn_crank(self) -> None:
        print("You turned, but there's no quarter")
    
    def dispense(self) -> None:
        print("You need to pay first")
        
        
class HasQuarterState(State):
    
    def insert_quarter(self) -> None:
        print("You can't insert another quarter")
        
    def eject_quarter(self) -> None:
        print("Quarter returned")
        self.gumball_machine.set_state(self.gumball_machine.no_quarter_state)
        
    def turn_crank(self) -> None:
        print("You turned...")
        self.gumball_machine.set_state(self.gumball_machine.sold_state)
        
    def dispense(self) -> None:
        print("No gumball dispensed")