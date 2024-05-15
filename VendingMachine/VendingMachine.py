from Inventory import Inventory
from IdleState import IdleState
class VendingMachine:

    def __init__(self) -> None:
        self.inventory = Inventory(10)
        self.coinList = []
        self.vendingMachineState = IdleState()

    def setVendingMachineState(self, state):
        self.vendingMachineState = state

    def getVendingMachineState(self):
        return self.vendingMachineState
    
    def setInventory(self, inventory):
        self.inventory = inventory

    def getInventory(self):
        return self.inventory
    
    def getCoinList(self):
        return self.coinList
    
    def setCoinList(self, coinList):
        self.coinList = coinList
