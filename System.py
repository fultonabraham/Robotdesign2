import time
'''
File containing System class
'''
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

'''
Communication is a subclass of System
'''
class Communication(System):
    def __init__(self, Software):
        super().__init__(Software)
        self._StartContact = 0
        self._EndContact = 0

    def Command(self):
        print("Make the System accept the Command")

    def Execution(self):
        print("Make the system execute the Commmand")

class Counter:
    def __init__(self):
        print("Counter: constructor")
        self._count = 0

    def reset(self):
        print("Counter - reset")
        self._count = 0

class SoftwareTimer(Counter):
    def __init__(self, handler):
        super().__init__()
        self._handler = handler
        self._starttime = 0
        self._started = False

    def start(self, seconds):
        print(f"Starting timer with {seconds} seconds")
        self._count = seconds
        self._starttime = time.ticks_ms()
        self._started = True

    def cancel(self):
        if self._started:
            self._starttime = 0
            print(f"{self._count} sec timer cancelled")
        self._started = False
        self._count = 0

    def check(self):
        if self._started and time.ticks_diff(time.ticks_ms(), self._starttime) > self._count * 1000:
            print(f"{self._count} sec timer is up")
            self._started = False
            self._count = 0
            self._handler.timeout()