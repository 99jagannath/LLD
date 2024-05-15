from Flyweight import Flyweight

class HumanoidRobot(Flyweight):

  def __init__(self, type, body) -> None:
    self.__type = type
    self.__body = body

  def getBody(self):
    return self.__body
  
  def getType(self):
    return self.__type
  
  def display(self, x, y):
    print(f'Position is {x}, {y}')
