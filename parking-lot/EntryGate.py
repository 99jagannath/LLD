from Ticket import Ticket
from datetime import datetime
class EntryGate:

    def __init__(self, parkingSpotManagerFactory) -> None:
        self.parkingSpotManagerFactory = parkingSpotManagerFactory

    def bookSpot(self, vehicle):
        parkingSpotManager = self.parkingSpotManagerFactory.getParkingManager(vehicle.VehicleType)
        parkingSpot = parkingSpotManager.findParkingSpot()
        parkingSpot.addVehicle(vehicle)
        return parkingSpot

    def fileTicket(self, vehicle):
        parkingSpot = self.bookSpot(vehicle)
        ticket=Ticket(datetime().now(), vehicle, parkingSpot)
        return ticket