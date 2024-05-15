
from Reservation import Reservation
from VehicleInventoryManager import VehicleInventoryManager
from Bill import Bill
class Store:

    def __init__(self) -> None:
        self.reservationList = []
        self.VehicleInventoryManager = VehicleInventoryManager()

    def makeReservation(self, vehicle, startDate, endDate, reservationType, user):

        reservation = Reservation(vehicle, startDate, endDate, reservationType, user)
        self.reservationList.append(reservation)
        self.VehicleInventoryManager.bookVehicle(vehicle)
        return reservation

    def printBill(self, reservation, amount):
        bill = Bill(reservation, amount)
        bill.printBill()
