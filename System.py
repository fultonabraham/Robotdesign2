"""
File containing System class
"""
class System:
    def __init__(self, Software) -> None:
        self._Software = Software
        
    def SystemCheck(self):
        print("Make the System run a check")

    def SystemOpearation(self):
        print("Make the System run an operation")

    def SetSpeed (slef):
        print("Make the System set the movement speed")
    
    def Update (slef):
        print("Make the System run an upate")

"""
Communication is a subclass of System
"""
class Communication(System):
    def __init__(self, Software):
        super().__init__(Software)
        self._StartContact = 0
        self._EndContact = 0

    def Command(self):
        print("Make the System accept the Command")

    def Execution(self):
        print("Make the system execute the Commmand")
