#encoding: utf-8

# A State model implementation

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
This is the Robot class
"""

class Robot:
    def __init__(self, numstates, handler, debug=False):
        self._numstates = numstates
        self._running = False
        self._transitions = []
        for i in range(0, numstates):
            self._transitions.append([None]*NUMEVENTS)
        self._curState = -1
        self._handler = handler
        self._debug = debug

    def start(self):
        self._curState = 0
        self._running = True
        self._handler.stateEntered(0)  # start the state model

    def stop(self):
        if self._running:
            self._handler.stateLeft(2)
        self._running = False
        self._curState = -1

    def gotoState(self, newState):
        if (newState < self._numstates):
            if self._debug:
                print(f"Going from State {self._curState} to State {newState}")
            self._handler.stateLeft(self._curState)
            self._curState = newState
            self._handler.stateEntered(self._curState)

    def addTransition(self, fromState, event, toState):
        self._transitions[fromState][event] = toState

    def processEvent(self, event):
        if (event < NUMEVENTS):
            newstate = self._transitions[self._curState][event]
            if newstate is None:
                if self._debug:
                    print(f"Ignoring event {EVENTNAMES[event]}")
            else:
                if self._debug:
                    print(f"Processing event {EVENTNAMES[event]}")
                self.gotoState(self._transitions[self._curState][event])