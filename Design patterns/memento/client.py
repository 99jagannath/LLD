# It's a behavioral design pattern

# it has three components
# 1. Originator :- It represents the objects which states are stored. It exposed two methods save memento and restore memento
# 2. Memento : It is the snapshot of the object that need to be stored.
# 3. care taker : it stores the list of memento so that can be restored.

from careTaker import CareTaker
from originator import Originator


def main():
  careTaker = CareTaker()
  obj = Originator(1,2,3,4)
  print(obj.height, obj.height)
  careTaker.add_memento(obj.create_memento())
  obj.set_height(6)
  obj.set_weight(7)
  print(obj.height, obj.height)
  obj.undo(careTaker.undo())
  print(obj.height, obj.height)


if __name__ == '__main__':
  main()




