from colleague import Colleague

class Bidder(Colleague):

  def __init__(self, name, mediator) -> None:
    self.name = name
    self.mediator = mediator
    self.mediator.add_bidder(self)

  def make_bid(self, amount):
    self.mediator.declare_bid(self, amount)

  def receiveBidNotification(self, amount):
    print("Some one make a bid of amount %s" % amount)

  def getName(self):
    return self.name