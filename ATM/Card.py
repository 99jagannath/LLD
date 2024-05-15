
class Card:

    def __init__(self, pin, backAccount) -> None:
        self.pin = pin
        self.backAccount = backAccount

    def getBankAccount(self):
        return self.backAccount
    
    def validatePin(self, userPin):
        return self.pin == userPin