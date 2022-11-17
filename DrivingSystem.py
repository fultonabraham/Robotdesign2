import time
import random

STOP = 0
GO = 1
ROTATE = 2

NUMEVENTS = 3
EVENTNAMES = ["STOP","GO","ROTATE"]

"""
This is the DrivingSystem class
"""

class DrivingSystem:
    def __init__(self, handler, CollisionDetection, PowerSystem, debug=False):
        self._curState = -1
        self._handler = handler
        self._running = True
        self._debug = debug
        self._CollisionDetection = CollisionDetection
        self._PowerSystem = PowerSystem

    def Stop(self):
        self._curState = 0
        self._running = False
        self._handler.stateEntered(3)  # off the state model

    def GO(self):
        self._curState = 1
        self._running = True
        self._handler.stateEntered(0)  # MOVE_FORWARD the state model

    def Rotate(self):
        self._curState = 2
        self._running = True
        self._handler.stateEntered(2)  # MOVE_BACKWARD the state model