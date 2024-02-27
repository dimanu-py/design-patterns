

class GumballMachine:
    
    SOLD_OUT: int = 0
    NO_QUARTER: int = 1
    HAS_QUARTER: int = 2
    SOLD: int = 3
    
    def __init__(self, number_gumballs: int) -> None:
        self.number_gumballs = number_gumballs
        
        if number_gumballs > 0:
            self.state = self.NO_QUARTER
            
    def insert_quarter(self) -> None:
        
        if self.state == self.HAS_QUARTER:
            print("You can't insert another quarter")
        elif self.state == self.NO_QUARTER:
            self.state = self.HAS_QUARTER
            print("You inserted a quarter")
        elif self.state == self.SOLD_OUT:
            print("You can't insert a quarter, the machine is sold out")
        elif self.state == self.SOLD:
            print("Please wait, we're already giving you a gumball")
            
    def eject_quarter(self) -> None:
        
        if self.state == self.HAS_QUARTER:
            print("Quarter returned")
            self.state = self.NO_QUARTER
        elif self.state == self.NO_QUARTER:
            print("You haven't inserted a quarter")
        elif self.state == self.SOLD:
            print("Sorry, you already turned the crank")
        elif self.state == self.SOLD_OUT:
            print("You can't eject, you haven't inserted a quarter yet")
            
    def turn_crank(self) -> None:
        
        if self.state == self.SOLD:
            print("Turning twice doesn't get you another gumball")
        elif self.state == self.NO_QUARTER:
            print("You turned but there's no quarter")
        elif self.state == self.SOLD_OUT:
            print("You turned, but there are no gumballs")
        elif self.state == self.HAS_QUARTER:
            print("You turned...")
            self.state = self.SOLD
            self.dispense()
            
    def dispense(self) -> None:
        
        if self.state == self.SOLD:
            print("A gumball comes rolling out the slot")
            self.number_gumballs -= 1
            if self.number_gumballs == 0:
                print("Oops, out of gumballs!")
                self.state = self.SOLD_OUT
            else:
                self.state = self.NO_QUARTER
        elif self.state == self.NO_QUARTER:
            print("You need to pay first")
        elif self.state == self.SOLD_OUT:
            print("No gumball dispensed")
        elif self.state == self.HAS_QUARTER:
            print("No gumball dispensed")
        