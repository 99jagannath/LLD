from abc import ABC, abstractclassmethod

class State(ABC):

    def clickOnInsertCoinButton(machine):
        pass

    def insertCoin(machine, coin):
        pass

    def clickOnProductSelectButton(machine):
        pass

    def selectItem(machine, code):
        pass

    def getChange(amount):
        pass

    def refundMoney(machine):
        pass

    def dispatchItem(machine, code):
        pass

    def updateInventory(machine, item, code):
        pass

