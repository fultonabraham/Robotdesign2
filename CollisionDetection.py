import time
import random

"""
This is the CollisionDetection class
"""

class CollisionDetection:
    def __init__(self, position, obstacle, debug=False):
        self._curState = -1
        self._position = position
        self._obstacle = obstacle
        self._running = True
        self._debug = debug

    def Reroute(self):
        rnd = random.randint(0, 1)
        if rnd == 0:
            self._curState = 6
            self._running = True
            return rnd
        else:
            return rnd