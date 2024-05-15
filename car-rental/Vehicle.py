
from VehicleStatus import VehicleStatus

class Vehicle:

    def __init__(self, no, brand, location, type) -> None:
        self.no = no
        self.brand = brand
        self.location = location
        self.type = type
        self.status = VehicleStatus.AVAILABLE.value

    def updateStatus(self, status):
        self.status = status