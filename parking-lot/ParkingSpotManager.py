
from abc import ABC, abstractclassmethod

class ParkingStrategy(ABC):

    @abstractclassmethod
    def findParkingSpace(self):
        pass

class NearToEntranceParkingStrategy(ParkingStrategy):

    def findParkingSpace(self, parking_spots):
        return parking_spots[0]
    
class NearToElevatorParkingStrategy(ParkingStrategy):

    def findParkingSpace(self, parking_spots):
        return parking_spots[1]

class ParkingSpotManager:
    def __init__(self, parkingStrategy, parkingSpotList=[]) -> None:
        self.parking_spots = parkingSpotList
        self.parkingStrategy = parkingStrategy

    def addParkingSpot(self, ParkingSpot):
        self.parking_spots.append(ParkingSpot)

    def removeParkingSpot(self, ParkingSpot):
        if ParkingSpot in self.parking_spots:
            self.parking_spots.remove(ParkingSpot)

    def findParkingSpot(self):
        return self.parkingStrategy.findParkingSpace(self.parking_spots)
    
class TwoWheelerParkingSpotManager(ParkingSpotManager):
    def __init__(self,  parkingSpotList=[]) -> None:
        self.parkingStrategy = NearToEntranceParkingStrategy()
        super().__init__(self.parkingStrategy, parkingSpotList)

class FourWheelerParkingSpotManager(ParkingSpotManager):
    def __init__(self, parkingSpotList=[]) -> None:
        self.parkingStrategy = NearToElevatorParkingStrategy()
        super().__init__(self.parkingStrategy, parkingSpotList)

class ParkingSpotManagerFactory:

    def getParkingManager(self, VehicleType):
        
        if VehicleType == 'TWO_WHEELER':
            twoWheelerParkingSpotList = []
            return TwoWheelerParkingSpotManager(twoWheelerParkingSpotList)
        if VehicleType == 'FOUR_WHEELER':
            fourWheelerParkingSpotList = []
            return FourWheelerParkingSpotManager(fourWheelerParkingSpotList)