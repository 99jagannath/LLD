
class Bill:

    def __init__(self, reservation, amount) -> None:
        self.reservation = reservation
        self.amount = amount

    def printBill(self):
        print("print amount with all the details")