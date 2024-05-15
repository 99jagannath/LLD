
class User:

    def __init__(self, BackAccount, name, card) -> None:
        self.bankAccount = BackAccount
        self.name = name
        self.card = card

    def getCard(self):
        return self.card
    
    def getBankAccount(self):
        return self.bankAccount