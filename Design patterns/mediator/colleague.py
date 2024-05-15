from abc import ABC, abstractclassmethod


class Colleague(ABC):

  @abstractclassmethod
  def make_bid(self):
    pass

  @abstractclassmethod
  def receiveBidNotification(self):
    pass

  @abstractclassmethod
  def getName(self):
    pass
