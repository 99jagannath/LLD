from abc import ABC


class State(ABC):

    def insertCard(self, atm):
        pass

    def authenticatePin(self, atm, card, pin):
        pass

    def selectOperation(self, atm, transactionType):
        pass

    def cashWithdrawal(self, atm, card, amount):
        pass

    def displayBalance(self, atm, card):
        pass

    def returnCard(self):
        pass

    def exit(self, atm):
        pass
