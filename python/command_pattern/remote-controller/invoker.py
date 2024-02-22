"""
The invoker object is the one that will have the command object and will be able to call the execute method on it.
"""
from command import Command, NoCommand


class RemoteControl:
    """
    The remote control will have different slots for different commands.
    
    Per slot, it will have an on command and an off command. For example, slot 0 will have an on command to turn on the light and an off command to turn off the light,
    the slot 1 can have an on command to open the garage door and an off command to close the garage door, and so on. If a slot has no command assigned to it, it will
    have a NoCommand object.
    """
    
    NUMBER_BUTTONS = 7
    
    def __init__(self) -> None:
        self.on_commands: list[Command] = []
        self.off_commands: list[Command] = []

        default_command = NoCommand()
        for _ in range(self.NUMBER_BUTTONS):
            self.on_commands.append(default_command)
            self.off_commands.append(default_command)

    def set_command(self, slot: int, on_command: Command, off_command: Command) -> None:
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pressed(self, slot: int) -> None:
        self.on_commands[slot].execute()

    def off_button_was_pressed(self, slot: int) -> None:
        self.off_commands[slot].execute()

    def __str__(self) -> str:
        representation = ""

        representation += "\n------ Remote Control ------\n"
        for i in range(len(self.on_commands)):
            representation += f"[slot {i}] {self.on_commands[i].__class__.__name__}    {self.off_commands[i].__class__.__name__}\n"
        return representation