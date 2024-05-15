from State import State
from HasMoneyState import HasMoneyState

class IdleState(State):

    def __init__(self) -> None:
        print("Currently in Idle state")

    def clickOnInsertCoinButton(machine):
        return machine.setVendingMachineState(HasMoneyState())