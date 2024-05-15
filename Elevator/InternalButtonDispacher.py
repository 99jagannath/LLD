
from ElevatorCreator import ElevatorCreator

class InternalButtonDispacher:

    def __init__(self) -> None:
        self.curController = None
        self.elevatorControllerList = ElevatorCreator().listElevatorController()

    def submitRequest(self, floor, eleVatorCar):
        for controller in self.elevatorControllerList:
            if controller.eleVatorCar.no == eleVatorCar.no:
                self.curController = controller
                break
        
        self.curController.submitInternalRequest(floor)

        