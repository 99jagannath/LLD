
from ElevatorCreator import ElevatorCreator

class ExternalButtonDispacher:

    def __init__(self) -> None:
        self.elevatorControllerList = ElevatorCreator().listElevatorController()

    def submitRequest(self, floor, direction):
        selectedElevatorController = None

        for controller in self.elevatorControllerList:
            if controller.eleVatorCar.no %2 == 0 and floor % 2== 0:
                selectedElevatorController = controller
                break

            if controller.eleVatorCar.no %2 != 0 and floor % 2!= 0:
                selectedElevatorController = controller
                break
        
        selectedElevatorController.submitExternalRequest(floor, direction)
