from flyweight import Flyweight

class TreeRobot(Flyweight):

  def __init__(self, type, body):
    self.__type = type
    self.__body = body

  def getType(self): return self.__type

  def getBody(self): return self.__body

  def display(self, x, y):
    print(f'Position {x}, {y}')