"""
File containing System class
"""
class PowerSystem:
    def __init__(self, Software) -> None:
        self._Software = Software

    def TurnOn(self):
        print("Turm on System")

    def TurnOff(self):
        print("Turn off the System")