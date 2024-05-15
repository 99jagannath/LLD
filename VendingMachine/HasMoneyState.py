
from State import State
from SelectionState import SelectionState
from  IdleState import IdleState

class HasMoneyState(State):

    def __init__(self) -> None:
        print("Current State is has money state")

    def insertCoin(machine, coin):
        return machine.coinList.append(coin)
    
    def clickOnProductSelectButton(machine):
        machine.setVendingMachineState(SelectionState())

    def refundMoney(machine):
        print("Refunding all the money")
        machine.setVendingMachineState(IdleState())
        return machine.getCoinList()