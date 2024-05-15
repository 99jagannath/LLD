
class Reservation:

    def __init__(self, vehicle, startDate, endDate, reservationType, user) -> None:
        self.vehicle = vehicle
        self.startDate = startDate
        self.endDate = endDate
        self.reservationType = reservationType
        self.user = user