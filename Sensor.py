"""
This is the Sensor class
"""

class Sensor:
    
    def __init__(self, Scan) -> None:
        self._Scan = Scan

    def ScanProximity(self):
        print("Scan Proximity")

    def ScanPath(self):
        print("Scan Path")

    def ScanObject(self):
        print("Scan Object")