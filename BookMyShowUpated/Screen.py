from SeatType import SeatType
from Seat import Seat
class Screen:

    def __init__(self) -> None:
        self.seats = []

    def addSeat(self, startRow: int, count: int, seatType: SeatType):
        row = startRow
        for i in range(count):
            seat = Seat(i, row, seatType)
            self.seats.append(seat)
            # Add logic to update row