from User import User
from BalanceSheet import BalanceSheet
class UserController:

    def __init__(self) -> None:
        self.users = []


    def createUser(self, id, name):
        balanceSheet = BalanceSheet()
        user = User(id, name, balanceSheet)
        self.users.append(user)
        return user
    
    def getUser(self, id):
        for user in self.users:
            if user.getId() == id:

    def getAllUser(self):
        return self.users
    
    
