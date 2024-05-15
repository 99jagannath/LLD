from CashWithDrawalProcessor import CashWithDrawalProcessor

class FiveHunCashWithDrawProcessor(CashWithDrawalProcessor):

    def __init__(self, processor) -> None:
        super().__init__(processor)

    def withDraw(self, atm, amount):
        reqFiveHunNotes = amount // 500
        leftAmount = amount % 500

        if reqFiveHunNotes <= atm.getFiveHunNote():
            atm.setFiveHunNote(atm.getFiveHunNote() - reqFiveHunNotes)
        
        else:
            atm.setFiveHunNote(0)
            leftAmount += reqFiveHunNotes - atm.getFiveHunNote()

        if leftAmount != 0:
            super().withDraw(atm, leftAmount)