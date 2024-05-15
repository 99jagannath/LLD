
from abc import ABC, abstractclassmethod

class Payment(ABC):

    @abstractclassmethod
    def make_payment(self, amount):
        pass

class CashPayment(Payment):

    def make_payment(self, amount):
        print("[%s] amount paid in cash" % amount)

class CardPayment(Payment):

    def make_payment(self, amount):
        print("[%s] amount paid in card" % amount)

class UPIPayment(Payment):

    def make_payment(self, amount):
        print("[%s] amount paid in UPI" % amount)

class PaymentFactory:

    def getPaymentMethod(self, paymentMethod):

        if paymentMethod == "CASH":
            return CashPayment()
        elif paymentMethod == "CARD":
            return CardPayment()
        elif paymentMethod == "UPI":
            return UPIPayment()

