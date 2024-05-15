from abc import ABC , abstractclassmethod


class Flyweight(ABC):

  @abstractclassmethod
  def display(self):
    pass