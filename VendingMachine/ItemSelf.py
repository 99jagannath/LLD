class ItemShelf:

    def __init__(self, item, code) -> None:
        self.item = item
        self.code = code
        self.soldOut = False

    def isSoldOut(self):
        return self.soldOut
    
    def setSoldOut(self):
        self.soldOut = True