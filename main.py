import os
from CollisionDetection import CollisionDetection
from DrivingSystem import DrivingSystem
from MovementControl import MovementControl
from Robot import *
from PowerSystem import *
from System import *
import time
import random

class Main:
    def buildModel(self):
        self._model = Robot(1, self)
        self._timer.reset()
        self._model.addTransition(0, TIMEOUT, 2)

    def stateLeft(self, stateno):
        self._display.reset()
        if stateno == 1:
            self._timer.cancel()
        elif stateno == 2:
            self._timer.cancel()
        elif stateno == 3:
            self._timer.cancel()
        else:
            pass

    def run(self):
        self._model.start()
        '''
        while self._model._running:
            if self._model._curState == 0:
                self._model.gotoState(1)
                time.sleep(0.5)
            if self._model._curState == 1:
                self._model.gotoState(6)
                self._model.gotoState(1)
                time.sleep(0.5)
            if self._model._curState == 2:
                self._model.gotoState(6)
                self._model.gotoState(1)
                time.sleep(0.5)
            if self._model._curState == 3:
                self._model._running = False
                time.sleep(0.5)
            else:
                pass
        '''
    def __init__(self):
        self._timer = SoftwareTimer(self)
        self._collision = CollisionDetection(2, 1)
        self._power = PowerSystem('XXX')
        self._driving = DrivingSystem(self, self._collision, self._power)
        self._movement = MovementControl(2, self, self._driving)
        self.buildModel()


    def stateEntered(self, state):
        if state == 0:        # what should happen when we enter state 0?
            self._timer.cancel()
            coll = self._collision.Reroute()
            if(coll == 0):
                print("Forward")
                self._movement.MoveForward()
                pick = random.randrange(0,9)
                if pick == 5:
                    self._model.stop()
            else:
                print("================= Review Collision =================")
                inputData = input()
                if inputData == "left":
                    print("Turn left")
                    self._movement.TurnLeft()
                elif inputData == "right":
                    print("Turn right")
                    self._movement.TurnRight()
                else:
                    print("Valor no identificado, vuelva a intentarlo")
            print("0: Go")
        elif state == 1:      # what should happen when we enter state 1?
            print("1: Wait")
        elif state == 2:      # what should happen when we enter state 2?
            coll = self._collision.Reroute()
            if(coll == 0):
                print("Forward")
                self._movement.MoveForward()
            else:
                print("================= Review Collision =================")
                inputData = input()
                if inputData == "left":
                    print("Turn left")
                    self._movement.TurnLeft()
                elif inputData == "right":
                    print("Turn right")
                    self._movement.TurnRight()
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