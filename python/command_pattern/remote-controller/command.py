"""
The command object is the one that encapsulates the receiver object and the action that should be performed on it.
"""

from abc import ABC, abstractmethod

from receiver import CeilingFan, GarageDoor, Light, Stereo


class Command(ABC):
    """Interface for all command objects."""

    @abstractmethod
    def execute(self):
        """Method to execute the command. This is what the invoker will call."""    


class NoCommand(Command):
    """This is a null object that will help us to avoid checking for null references."""
    
    def execute(self) -> None:
        return


class LightOnCommand(Command):
    """Command to switch on a light receiver."""
    
    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.turn_on()
    

class LightOffCommand(Command):
    """Command to switch off a light receiver."""
    
    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.turn_off()


class StereoOnWithCDCommand(Command):
    """Command to switch on a stereo receiver and set it to CD mode."""

    def __init__(self, stereo: Stereo) -> None:
        self.stereo = stereo

    def execute(self) -> None:
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)


class StereoOnWithDVDCommand(Command):
    """Command to switch on a stereo receiver and set it to DVD mode."""

    def __init__(self, stereo: Stereo) -> None:
        self.stereo = stereo

    def execute(self) -> None:
        self.stereo.on()
        self.stereo.set_dvd()
        self.stereo.set_volume(11)


class StereoOffWithCDCommand(Command):
    """Command to switch off a stereo receiver and set it to CD mode."""

    def __init__(self, stereo: Stereo) -> None:
        self.stereo = stereo

    def execute(self) -> None:
        self.stereo.off()
        self.stereo.set_cd()
        self.stereo.set_volume(0)


class StereoOffWithDVDCommand(Command):
    """Command to switch off a stereo receiver and set it to DVD mode."""

    def __init__(self, stereo: Stereo) -> None:
        self.stereo = stereo

    def execute(self) -> None:
        self.stereo.off()
        self.stereo.set_dvd()
        self.stereo.set_volume(0)


class GarageDoorOpenCommand(Command):
    """Command to open a garage door."""

    def __init__(self, garage_door: GarageDoor) -> None:
        self.garage_door = garage_door

    def execute(self) -> None:
        self.garage_door.open()
        self.garage_door.light_on()


class GarageDoorCloseCommand(Command):
    """Command to close a garage door."""

    def __init__(self, garage_door: GarageDoor) -> None:
        self.garage_door = garage_door

    def execute(self) -> None:
        self.garage_door.close()
        self.garage_door.light_off()


class CeilingFanHighCommand(Command):
    """Command to set a ceiling fan to high speed."""

    def __init__(self, ceiling_fan: CeilingFan) -> None:
        self.ceiling_fan = ceiling_fan

    def execute(self) -> None:
        self.ceiling_fan.high()
        

class CeilingFanMediumCommand(Command):
    """Command to set a ceiling fan to medium speed."""

    def __init__(self, ceiling_fan: CeilingFan) -> None:
        self.ceiling_fan = ceiling_fan

    def execute(self) -> None:
        self.ceiling_fan.medium()
        

class CeilingFanLowCommand(Command):
    """Command to set a ceiling fan to low speed."""

    def __init__(self, ceiling_fan: CeilingFan) -> None:
        self.ceiling_fan = ceiling_fan

    def execute(self) -> None:
        self.ceiling_fan.low()
