from bidder import Bidder
from mediator import Mediator

def main():
  med = Mediator()
  b1 = Bidder('jp', med)
  b2  = Bidder('jh', med)

  b1.make_bid(100)


if  __name__ == '__main__':
  main()