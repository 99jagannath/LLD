
from CashWithDrawalProcessor import CashWithDrawalProcessor

class TwoHunCashWithDrawalProcessor(CashWithDrawalProcessor):

    def __init__(self, processor) -> None:
        super().__init__(processor)

    def withDraw(self, atm, amount):
        requiredNotes = amount // 200
        remainingAmount = amount % 200

        if requiredNotes <= atm.getTwoHunNotes():
            atm.setTwoHunNotes(atm.getTwoHunNotes() - requiredNotes)
        else:
            
            remainingAmount += (requiredNotes - atm.getTwoHunNotes()) * 200
            atm.setTwoHunNotes(0)

        if remainingAmount != 0:
            super().withDraw(atm, amount)