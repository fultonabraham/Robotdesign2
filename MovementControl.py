import time
import random

TURN_ON = 0
TURN_OFF = 1
MOVE_FORWARD = 2
MOVE_BACKWARD = 3
MOVE_LEFTH = 4
MOVE_RIGHT = 5
COLLISION_DETECTED = 6

NUMEVENTS = 7
EVENTNAMES = ["TURN_ON","TURN_OFF","MOVE_FORWARD","MOVE_BACKWARD","MOVE_LEFTH","MOVE_RIGHT","COLLISION_DETECTED"]

"""
This is the MovementControl class
"""

class MovementControl:
    def __init__(self, numstates, handler, debug=False):
        self._numstates = numstates
        self._running = False
        self._transitions = []
        for i in range(0, numstates):
            self._transitions.append([None]*NUMEVENTS)
        self._curState = -1
        self._handler = handler
        self._debug = debug

    def off(self):
        self._curState = 1
        self._running = False
        self._handler.stateEntered(3)  # off the state model

    def forward(self):
        self._curState = 2
        self._running = True
        self._handler.stateEntered(0)  # MOVE_FORWARD the state model

    def backward(self):
        self._curState = 3
        self._running = True
        self._handler.stateEntered(0)  # MOVE_BACKWARD the state model

    def left(self):
        self._curState = 4
        self._running = True
        self._handler.stateEntered(2)  # MOVE_LEFTH the state model

    def right(self):
        self._curState = 5
        self._running = True
        self._handler.stateEntered(2)  # MOVE_RIGHT the state model

    def collision(self):
        rnd = random.randint(0, 1)
        if rnd == 0:
            self._curState = 6
            self._running = True
            return rnd
        else:
            return rnd