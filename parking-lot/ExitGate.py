from CostComputation import CostComputationFactory
from Payment import PaymentFactory
from ParkingSpotManager import ParkingSpotManagerFactory
class ExitGate:

    def __init__(self, ticket) -> None:
        self.CostComputationFactory = CostComputationFactory()
        self.parkingSpotManagerFactory = ParkingSpotManagerFactory()
        self.ticket = ticket
        self.PaymentFactory = PaymentFactory()

    def calculate_price(self):
        return self.CostComputationFactory.getCostComputation(self.ticket).compute()
    
    def make_payment(self):
        amount = self.calculate_price()
        self.PaymentFactory.getPaymentMethod("UPI").make_payment(amount)

    def free_parking_spot(self):
        self.ticket.parking_spots.removeVehicle()

