from State import State
from IdleState import IdleState
from CashWithDrawyalState import CashWithdrawalState
from CheckBalanceState import CheckBalanceState


class SelectOperationState(State):

    def selectOperation(self, atm, transactionType):
        if transactionType == "CASH_WITHDRAWAL":
            atm.setATMState(CashWithdrawalState)
        elif transactionType == "DISPLAY_BALANCE":
            atm.setATMState(CheckBalanceState())

        else:
            print("Invalid Transaction Type")
            self.exit(atm)


    def returnCard(self):
        print("Returning card")

    def exit(self, atm):
        self.returnCard()
        atm.setATMState(IdleState())