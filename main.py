import os
from MovementControl import MovementControl
from Robot import *
import time
import random

class Main:
    def buildModel(self):
        self._model = Robot(1, self)

    def run(self):
        self._model.start()
        while self._model._running:
            if self._model._curState == 0:
                self._model.gotoState(1)
            if self._model._curState == 1:
                self._model.gotoState(6)
                self._model.gotoState(1)
            if self._model._curState == 2:
                self._model.gotoState(6)
                self._model.gotoState(1)
            if self._model._curState == 3:
                self._model._running = False
            else:
                pass

    def __init__(self):
        self._movement = MovementControl(2, self)
        self.buildModel()


    def stateEntered(self, state):
        if state == 0:        # what should happen when we enter state 0?
            coll = self._movement.collision()
            if(coll == 0):
                print("Forward")
                self._movement.forward()
                pick = random.randrange(0,9)
                if pick == 5:
                    self._model.stop()
            else:
                print("================= Review Collision =================")
                inputData = input()
                if inputData == "left":
                    print("Turn left")
                    self._movement.left()
                elif inputData == "rigth":
                    print("Turn right")
                    self._movement.right()
                else:
                    print("Valor no identificado, vuelva a intentarlo")
            print("0: Go")
        elif state == 1:      # what should happen when we enter state 1?
            print("1: Wait")
        elif state == 2:      # what should happen when we enter state 2?
            coll = self._movement.collision()
            if(coll == 0):
                print("Forward")
                self._movement.forward()
            else:
                print("================= Review Collision =================")
                inputData = input()
                if inputData == "left":
                    print("Turn left")
                    self._movement.left()
                elif inputData == "rigth":
                    print("Turn right")
                    self._movement.right()
                else:
                    print("Valor no identificado, vuelva a intentarlo")
            print("2: Caution")
        elif state == 3:      # what should happen when we enter state 3?
            print("3: Stop")
            self._movement.stop()
        else:
            print("Invalid state")
            self._movement.stop()

if __name__ == "__main__":
    m = Main()
    m.run()