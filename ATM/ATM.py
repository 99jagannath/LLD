
class ATM:

    def __init__(self, balance, FiveHunNote, twoHunNote, oneHunNote)-> None:
        self.balance = balance
        self.FiveHunNote = FiveHunNote
        self.twoHunNote = twoHunNote
        self.oneHunNote = oneHunNote
        self.ATMState = IdleState()

    def getATMState(self):
        return self.ATMState
    
    def setATMState(self, state):
        self.ATMState = state

    def getBalance(self):
        return self.balance
    
    def setBalance(self, newBalance):
        self.balance = newBalance

    def getFiveHunNote(self):
        return self.FiveHunNote
    
    def setFiveHunNote(self, newFiveHunNotes):
        self.FiveHunNote = newFiveHunNotes

    def setTwoHunNotes(self, newTwoHunNotes):
        self.twoHunNote = newTwoHunNotes

    def getTwoHunNotes(self):
        return self.twoHunNote
    
    def getOneHunNotes(self):
        return self.oneHunNote
    
    def setOneHunNotes(self, newOneHunNotes):
        self.oneHunNote = newOneHunNotes