from VehicleInventoryManager import VehicleInventoryManager

class CarInventoryManager(VehicleInventoryManager):

    def __init__(self, carList=[]) -> None:
        super().__init__(carList)