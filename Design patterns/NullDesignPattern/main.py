from VehicleFactory import VehicleFactory

class Test:

    def __init__(self) -> None:
        self.VehicleFactory = VehicleFactory()

    def run(self):
        vehicle = self.VehicleFactory.getVehicle("Car")
        print(vehicle.getFuelCapacity())
        vehicle = self.VehicleFactory.getVehicle("Bike")
        print(vehicle.getFuelCapacity())

Test().run()
