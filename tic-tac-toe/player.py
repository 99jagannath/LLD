
class Player:

    def __init__(self, name=None, PieceType=None) -> None:
        self.name = name
        self.PieceType = PieceType

    def getName(self):
        return self.name
    
    def getPieceType(self):
        return self.PieceType