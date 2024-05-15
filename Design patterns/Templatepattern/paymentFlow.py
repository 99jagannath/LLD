# it is a behavioral design pattern
# It is used when all the classes need to follow common steps
# Each class should have independent logic

from abc import ABC, abstractclassmethod

class paymentFlow(ABC):

  @abstractclassmethod
  def validate_request(self):
    pass

  @abstractclassmethod
  def debit_money(self):
    pass

  @abstractclassmethod
  def credit_money(self):
    pass