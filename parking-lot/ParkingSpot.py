
class ParkingSpot:

    def __init__(self, id, position, floor, price=5) -> None:
        self.id  = id
        self.position = position
        self.floor = floor
        self.isEmpty = True
        self.Vehicle = None
        self.price = price

    def addVehicle(self, Vehicle):
        self.Vehicle = Vehicle
        self.isEmpty = False

    def removeVehicle(self):
        self.Vehicle = None
        self.isEmpty = True

class TwoWheelerParkingSpot(ParkingSpot):
    def __init__(self, id, position, floor):
        super().__init__(id, position, floor, price=10)
    
class FourWheelerParkingSpot(ParkingSpot):
    def __init__(self, id, position, floor) -> None:
        super().__init__(id, position, floor, price=15)