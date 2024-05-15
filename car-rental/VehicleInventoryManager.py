
from VehicleStatus import VehicleStatus
class VehicleInventoryManager:

    def __init__(self, vehicleList) -> None:
        self.vehicleList = vehicleList

    def listVehicle(self):
        return self.vehicleList
    
    def addVehicle(self, vehicle):
        self.vehicleList.append(vehicle)

    def removeVehicle(self, vehicle):
        self.vehicleList.remove(vehicle)

    def bookVehicle(self, vehicle):
        for i in range(len(self.vehicleList)):
            if self.vehicleList[i].no == vehicle.no:
                self.vehicleList[i].status = VehicleStatus.BOOKED.value
                break

    def makeVehicleAvailable(self, vehicle):
        for i in range(len(self.vehicleList)):
            if self.vehicleList[i].no == vehicle.no:
                self.vehicleList[i].status = VehicleStatus.AVAILABLE.value
                break
