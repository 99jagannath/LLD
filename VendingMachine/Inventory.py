from ItemSelf import ItemShelf
class Inventory:

    def __init__(self, size) -> None:
        self.size = size
        self.inventory = [None]*size
        self.inventoryInitialization()

    def inventoryInitialization(self):
        code = 101
        for i in range(self.size):
            shelf = ItemShelf()
            shelf.code = code
            shelf.soldOut = True
            self.inventory[i] = shelf
            code += 1

    def addItem(self, item, code):
        for i in range(self.size):
            if self.inventory[i].code == code:
                if self.Inventory[i].isSoldOut == True:
                    self.inventory[i].item = item
                    self.Inventory[i].isSoldOut == False
                else:
                    raise Exception("Item already there")
                break

    def getItem(self, code):

        for i in range(self.size):
            if self.inventory[i].code == code:
                if self.inventory[i].isSoldOut == False:
                    return self.inventory.item
                else:
                    raise Exception("This item is sold out.")
                

    def updateSoldOutItem(self, code):
        for shelf in self.Inventory:
            if shelf.code == code and not shelf.isSoldOut:
                shelf.isSoldOut=True

        
