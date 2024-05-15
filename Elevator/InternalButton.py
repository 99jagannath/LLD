
from InternalButtonDispacher import InternalButtonDispacher


class InternalButton:

    def __init__(self) -> None:
        self.internalButtonDispacher = InternalButtonDispacher()
        self.buttons = [1, 2, 3, 4, 5, 6]

    def pressButton(self, floor, elevatorCar):
        self.internalButtonDispacher.submitRequest(floor, elevatorCar)
        
