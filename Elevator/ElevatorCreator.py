from ElevatorCar import ElevatorCar
from ElevatorController import ElevatorController
class ElevatorCreator:

    def __init__(self) -> None:
        self.elevatorControllerList = []
        self.no = 0

    def listElevatorController(self):
        return self.elevatorControllerList

    def addElevatorController(self):
        self.no += 1
        newCar = ElevatorCar(self.no)
        elevatorController = ElevatorController(newCar)
        self.elevatorControllerList.append(elevatorController)

    def removeElevatorController(self, no):

        for controller in self.elevatorControllerList:
            if controller.eleVatorCar.no == no:
                self.elevatorControllerList.remove(controller)
                break


