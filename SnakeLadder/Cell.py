
class Cell:

    def __init__(self, jump=None, user=None) -> None:
        self.jump = jump
        self.user = user

    def getJump(self):
        return self.jump
    
    def getUser(self):
        return self.user
    