from State import State
from Direction import Direction
from InternalButton import InternalButton
from Display import Display
from Door import Door

class ElevatorCar:

    def __init__(self, no) -> None:
        self.no = no
        self.display = Display()
        self.internalButton = InternalButton()
        self.door = Door()
        self.state = State.IDLE
        self.floor = 0
        self.direction= Direction.UP

    def pressButton(self):
        destFloor = int(input())
        self.internalButton.pressButton(destFloor, self)

    def move(self, destFloor):
        if self.direction == Direction.UP:
            start = self.floor
            for curFloor in range(start, destFloor+1):
                self.floor = curFloor
                self.display.setDisplay(self.floor, self.direction)
                self.display.showDisplay()
                if self.floor == destFloor:
                    self.state = State.IDLE
        
        if self.direction == Direction.DOWN:
            start = self.floor
            for curFloor in range(start, destFloor-1, -1):
                self.floor = curFloor
                self.display.setDisplay(self.floor, self.direction)
                self.display.showDisplay()
                if self.floor == destFloor:
                    self.state = State.IDLE


