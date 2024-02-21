"""
The receiver object in the command pattern is the object that is able to perform the operations.

With the command pattern, the receiver object is decoupled from the objects that would want to use its instance to execute an action.
"""

class Light:
    """
    Represent any light in the house.
    
    It can be turned on and off.
    """
    
    def __init__(self, location: str = "") -> None:
        self.location = location
        self.bulb = "off"

    def turn_on(self) -> None:
        self.bulb = "on"
        print(f"Light is {self.bulb}")

    def turn_off(self) -> None:
        self.bulb = "off"
        print(f"Light is {self.bulb}")


class GarageDoor:
    """
    Represents the garage door. 
    
    It can be opened, closed, stopped, and the light can be turned on and off.
    """
    def __init__(self, location: str = "") -> None:
        self.location = location
        self.door = "closed"

    def open(self) -> None:
        self.door = "open"
        print(f"Garage door is {self.door}")
        
    def close(self) -> None:
        self.door = "closed"
        print(f"Garage door is {self.door}")
        
    def stop(self) -> None:
        print("Garage door is stopped")
        
    def light_on(self) -> None:
        print("Garage light is on")
        
    def light_off(self) -> None:
        print("Garage light is off")


class Stereo:
    """
    Represents the stereo in the house.
    
    It can be turned on and off, the CD, DVD, and radio can be set, and the volume can be adjusted.
    """
    def __init__(self, location: str = "") -> None:
        self.location = location
        self.state = "off"
        self.volume = 0

    def on(self) -> None:
        self.state = "on"
        print(f"Stereo is {self.state}")

    def off(self) -> None:
        self.state = "off"
        print(f"Stereo is {self.state}")

    def set_cd(self) -> None:
        print("CD is set")

    def set_dvd(self) -> None:
        print("DVD is set")

    def set_radio(self) -> None:
        print("Radio is set")

    def set_volume(self, volume: int) -> None:
        self.volume = volume
        print(f"Volume is {self.volume}")
        

class CeilingFan:
    """
    Represents the ceiling fan in the house.
    
    It can be turned on and off, and the speed can be adjusted.
    """
    
    HIGH_SPEED = 3
    MEDIUM_SPEED = 2
    LOW_SPEED = 1
    OFF_SPEED = 0
    
    def __init__(self, location: str = "") -> None:
        self.location = location
        self.speed = self.OFF_SPEED
        
    def high(self) -> None:
        self.speed = self.HIGH_SPEED
        print("Ceiling fan is on high speed")
        
    def medium(self) -> None:
        self.speed = self.MEDIUM_SPEED
        print("Ceiling fan is on medium speed")
        
    def low(self) -> None:
        self.speed = self.LOW_SPEED
        print("Ceiling fan is on low speed")
        
    def off(self) -> None:
        self.speed = self.OFF_SPEED
        print("Ceiling fan is off")
    
    
    