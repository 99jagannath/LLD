
from State import State
from IdleState import IdleState
from DispenseState import DispenseState

class SelectionState(State):

    def __init__(self) -> None:
        print("Current State is selection state")

    def refundMoney(machine):
        print("Refunding all the money")
        machine.setVendingMachineState()
        machine.getCoinList()

    def selectItem(machine, code):
        shelf = None
        for i in range(len(machine.getInventory())):
            if machine.getInventory()[i].code == code:
                shelf = machine.getInventory()[i]
                break
        if shelf.isSoldOut():
            print("Item is sold out")
            machine.setVendingMachineState(IdleState())
            return
        
        amount = 0

        for coin in machine.getCoinList():
            amount += coin.value

        price = shelf.item.price

        if price > amount:
            print("Not enough money")
            machine.setVendingMachineState(IdleState())
            return
        
        change = amount - price
        if change > 0:
            self.getChange(change)

        machine.setVendingMachineState(DispenseState())

    def getChange(amount):
        print("returning change amount %s" % amount)


