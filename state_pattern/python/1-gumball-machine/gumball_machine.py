from state import State, SoldOutState, HasQuarterState, SoldState, NoQuarterState, WinnerState


class GumballMachine:
    
    sold_out_state: State
    no_quarter_state: State
    has_quarter_state: State
    sold_state: State
    winner_state: State
    
    def __init__(self, number_gumballs: int) -> None:
        
        self.sold_out_state = SoldOutState(self)
        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)
        self.winner_state = WinnerState(self)
        
        self.state = self.sold_out_state
        self.number_gumballs = number_gumballs
        
        if number_gumballs > 0:
            self.state = self.no_quarter_state
            
    def insert_quarter(self) -> None:
        self.state.insert_quarter()
            
    def eject_quarter(self) -> None:
        self.state.eject_quarter()
            
    def turn_crank(self) -> None:
        self.state.turn_crank()
            
    def dispense(self) -> None:
        self.state.dispense()
        
    def set_state(self, state: State) -> None:
        self.state = state
        
    def release_ball(self) -> None:
        print("A gumball comes rolling out the slot...")
        if self.number_gumballs != 0: 
            self.number_gumballs = self.number_gumballs - 1;
        