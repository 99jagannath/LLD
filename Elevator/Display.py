
class Display:

    def __init__(self, direction, floor) -> None:
        self.direction = direction
        self.floor = floor
    def setDisplay(self, floor, direction):
        self.direction = direction
        self.floor = floor

    def showDisplay(self):
        print("DIR %s\n Floor %s" % (self.direction, self.floor))