from command import (CeilingFanHighCommand, CeilingFanLowCommand,
                     CeilingFanMediumCommand, GarageDoorCloseCommand,
                     GarageDoorOpenCommand, LightOffCommand, LightOnCommand,
                     StereoOnWithCDCommand, StereoOnWithDVDCommand, MacroCommand)
from invoker import RemoteControl
from receiver import CeilingFan, GarageDoor, Light, Stereo


def main() -> None:
    # Invoker
    remote = RemoteControl()

    # Receivers
    living_room_light = Light("Living Room")
    garage_door = GarageDoor()
    stereo = Stereo("Bedroom")
    outdoor_light = Light("Outdoor")
    ceiling_fan = CeilingFan("Ceiling Fan")

    # Commands
    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)

    garage_door_open = GarageDoorOpenCommand(garage_door)
    garage_door_close = GarageDoorCloseCommand(garage_door)

    stereo_on_with_cd = StereoOnWithCDCommand(stereo)
    stereo_on_with_dvd = StereoOnWithDVDCommand(stereo)

    outdoor_light_on = LightOnCommand(outdoor_light)
    outdoor_light_off = LightOffCommand(outdoor_light)
    
    ceiling_fan_high = CeilingFanHighCommand(ceiling_fan)
    ceiling_fan_medium = CeilingFanMediumCommand(ceiling_fan)
    ceiling_fan_low = CeilingFanLowCommand(ceiling_fan)

    party_on_commands = [living_room_light_on, stereo_on_with_cd, ceiling_fan_high]
    party_off_commands = [living_room_light_off, stereo_on_with_dvd, ceiling_fan_low]
    party_on_macro = MacroCommand(party_on_commands)
    party_off_macro = MacroCommand(party_off_commands)

    # Add command to invoker
    remote.set_command(0, living_room_light_on, living_room_light_off)
    remote.set_command(1, garage_door_open, garage_door_close)
    remote.set_command(2, stereo_on_with_cd, stereo_on_with_dvd)
    remote.set_command(3, outdoor_light_on, outdoor_light_off)
    remote.set_command(4, ceiling_fan_high, ceiling_fan_low)
    remote.set_command(5, party_on_macro, party_off_macro)

    print(remote)

    # Execute command
    remote.on_button_was_pressed(0)
    remote.off_button_was_pressed(0)
    print(remote)
    remote.undo_button_was_pressed()

    remote.on_button_was_pressed(1)
    print(remote)
    remote.undo_button_was_pressed()
    remote.off_button_was_pressed(1)

    remote.on_button_was_pressed(2)
    remote.off_button_was_pressed(2)

    remote.on_button_was_pressed(3)
    remote.off_button_was_pressed(3)
    
    remote.on_button_was_pressed(4)
    print(remote)
    remote.undo_button_was_pressed()

    remote.on_button_was_pressed(5)
    print(remote)
    remote.off_button_was_pressed(5)
    
    
if __name__ == "__main__":
    main()
    