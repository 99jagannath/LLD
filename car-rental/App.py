

class App:

    def __init__(self) -> None:
        self.storeList = []
        self.useList = []

    def getStore(self, location):
        return self.storeList[0]
    
    # add , remove store & user