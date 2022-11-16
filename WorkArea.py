"""
File containing WorkArea class
"""
class WorkArea:
    def __init__(self, Area, Restriction) -> None:
        self._Area = Area
        self._Restriction = Restriction

    def DefineWorkArea(self):
        print("Defne Robot work area")