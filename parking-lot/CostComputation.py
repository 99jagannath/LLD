from datetime import datetime
class PricingStrategy:

    def calculate_price(self, ticket):
        currentTime = datetime.utcnow("dd-mm-yy %h:%m:%s:%sz")
        return ticket.parkingSpot.price * (currentTime.sec - ticket.entryTime.sec)
    
class HourlyPricingStrategy(PricingStrategy):

    def calculate_price(self, ticket):
        currentTime = datetime.utcnow("dd-mm-yy %h:%m:%s:%sz")
        return ticket.parkingSpot.price * (currentTime.hour - ticket.entryTime.hour)
    
class MinutePricingStrategy(PricingStrategy):

    def calculate_price(self, ticket):
        currentTime = datetime.utcnow("dd-mm-yy %h:%m:%s:%sz")
        return ticket.parkingSpot.price * (currentTime.min - ticket.entryTime.min)
        


class CostComputation:

    def __init__(self, ticket, pricingStrategy = PricingStrategy()) -> None:
        self.PricingStrategy = pricingStrategy
        self.ticket = ticket

    def compute(self):
        return self.PricingStrategy.calculate_price(self.ticket)
    
class TwoWheelerCostComputation(CostComputation):

    def __init__(self, ticket, pricingStrategy=MinutePricingStrategy()) -> None:
        super().__init__(ticket, pricingStrategy)

class FourWheelerCostComputation(CostComputation):

    def __init__(self, ticket, pricingStrategy=HourlyPricingStrategy()) -> None:
        super().__init__(ticket, pricingStrategy)


class CostComputationFactory:

    def getCostComputation(self, ticket):
        if ticket.vehicleType == "TWO_WHEELER":
            return TwoWheelerCostComputation(ticket)
        elif ticket.VehicleType == "FOUR_WHEELER":
            return FourWheelerCostComputation(ticket)
