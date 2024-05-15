from Floor import Floor

class Building:

    def __init__(self) -> None:
        self.floorList = []

    def addFloor(self, floor):
        self.floorList.append(floor)

    def removeFloor(self, floor):
        if floor in self.floorList:
            self.floorList.remove(floor)

    def getAllFloor(self):
        return self.floorList