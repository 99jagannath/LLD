
class Mediator:

  def __init__(self) -> None:
    self.colleague = []

  def add_bidder(self, bidder):
    self.colleague.append(bidder)

  def declare_bid(self, cur_bidder, amount):
    for bidder in self.colleague:
      if bidder.getName() != cur_bidder.getName():
        bidder.receiveBidNotification(amount)