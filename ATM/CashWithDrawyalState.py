from State import State
from IdleState import IdleState
from TwoHunCashWithDrawalProcessor import TwoHunCashWithDrawalProcessor
from FiveHunCashWithDrawalProcessor import FiveHunCashWithDrawProcessor
from OneHunCashWithDrawalProcessor import OneHunCashWithDrawalProcessor

class CashWithdrawalState(State):

    def cashWithdrawal(self, atm, card, amount):
        atmBalance = atm.getBalance()
        if atmBalance < amount:
            print("Insufficient balance")
            self.returnCard()
            self.exit(atm)
            
        elif card.getBankAccount().getBalance() < amount:
            print("Your bank account does not have enough money to cover this transaction.")
            self.returnCard()
            self.exit(atm)
        
        else:
            cashWithdrawalProcessor = TwoHunCashWithDrawalProcessor(FiveHunCashWithDrawProcessor(OneHunCashWithDrawalProcessor(None)))
            cashWithdrawalProcessor.withDraw(atm, amount)
            atm.setATMState(IdleState())


    def returnCard(self):
        return print("Returning card")
    
    def exit(self, atm):
        return atm.setATMState(IdleState())
        