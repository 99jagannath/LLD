
from Vehicle import Vehicle
from VehicleType import VehicleType

class Car(Vehicle):

    def __init__(self, no, brand, location, type=VehicleType.Car.value) -> None:
        super().__init__(no, brand, location, type)