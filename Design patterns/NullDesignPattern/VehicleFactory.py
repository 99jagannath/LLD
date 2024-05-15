from Car import Car
from NullVehicle import NullVehicle

class VehicleFactory:

    def getVehicle(self, vehicleType):
        if vehicleType == "Car":
            return Car()
        return NullVehicle()