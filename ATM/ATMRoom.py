from ATM import ATM
from User import User
from BankAccount import BackAccount
from Card import Card


class ATMRoom:

    def __init__(self) -> None:
        self.atm = ATM(3000, 4, 3, 4)
        self.user = None
        self.initializeUser()

    def initializeUser(self):
        bankAccount = self.createBankAccount()
        card = self.createCard(bankAccount)
        self.user = User(bankAccount, "Jagan", card)

    def createBankAccount(self):
        account = BackAccount(101, 5000)
        return account
    
    def createCard(self, backAccount):
        return Card("1234", backAccount)
    

