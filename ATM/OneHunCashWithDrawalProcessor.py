from CashWithDrawalProcessor import CashWithDrawalProcessor

class OneHunCashWithDrawalProcessor(CashWithDrawalProcessor):

    def __init__(self, processor) -> None:
        super().__init__(processor)

    def withDraw(self, atm, amount):
        requiredNotes = amount // 100
        remainingAmount = amount % 100

        if requiredNotes <= atm.getOneHunNotes():
            atm.setOneHunNotes(atm.getOneHunNotes() - requiredNotes)
        else:
            
            remainingAmount += (requiredNotes - atm.getOneHunNotes()) * 200
            atm.setOneHunNotes(0)

        if remainingAmount != 0:
            print("Something is wrong")