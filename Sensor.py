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

class Sensor:
    def __init__(self, fov, range_min, range_max):
        self._fov = fov
        self._range_min = range_min
        self._range_max = range_max

    def get_fov(self):
        return self._fov

    def get_range_min(self):
        return self._range_min

    def get_range_max(self):
        return self._range_max