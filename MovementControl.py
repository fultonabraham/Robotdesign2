import time
import random

MOVE_FORWARD = 0
MOVE_BACKWARD = 1
MOVE_LEFTH = 2
MOVE_RIGHT = 3

NUMEVENTS = 4
EVENTNAMES = ["MOVE_FORWARD","MOVE_BACKWARD","MOVE_LEFTH","MOVE_RIGHT"]

"""
This is the MovementControl class
"""

class MovementControl:
    def __init__(self, numstates, handler, DrivingSystem, debug=False):
        self._numstates = numstates
        self._running = False
        self._transitions = []
        for i in range(0, numstates):
            self._transitions.append([None]*NUMEVENTS)
        self._curState = -1
        self._handler = handler
        self._debug = debug
        self._DrivingSystem = DrivingSystem

    def MoveForward(self):
        self._curState = 2
        self._running = True
        self._handler.stateEntered(0)  # MOVE_FORWARD the state model

    def MoveBackward(self):
        self._curState = 3
        self._running = True
        self._handler.stateEntered(0)  # MOVE_BACKWARD the state model

    def TurnLeft(self):
        self._curState = 4
        self._running = True
        self._handler.stateEntered(2)  # MOVE_LEFTH the state model

    def TurnRight(self):
        self._curState = 5
        self._running = True
        self._handler.stateEntered(2)  # MOVE_RIGHT the state model