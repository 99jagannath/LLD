from State import State
from IdleState import IdleState

class CheckBalanceState(State):

    def displayBalance(self, atm, card):
        balance = card.getBankAccount().getBalance()
        print("Current balance is %s" % balance)
        atm.setATMState(IdleState())