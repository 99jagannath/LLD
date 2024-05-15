
class Show:
    def __init__(self, id, movie, screen, startTime, endTime) -> None:
        self.id = id
        self.movie = movie
        self.startTime = startTime
        self.endTime = endTime
        self.screen = screen
        self.bookedSeats = []

    def addBookedSeats(self, seat):
        self.bookedSeats.append(seat)

    def isBooked(self, Seat):
        return Seat in self.bookedSeats