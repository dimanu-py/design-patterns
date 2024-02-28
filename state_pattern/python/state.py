from abc import ABC, abstractmethod


class State(ABC):
    
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
    