from State import State
from IdleState import IdleState
class DispenseState(State):

    def __init__(self) -> None:
        print("Currently in Dispense state")

    def dispatchItem(machine, code):
        shelf = None

        for i in range(len(machine.getInventory())):
            if machine.getInventory()[i].code == code:
                shelf = machine.getInventory()[i]
                break

        shelf.setSoldOut()
        machine.setVendingMachineState(IdleState())
        return shelf.item

