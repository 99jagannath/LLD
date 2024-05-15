
from Prototype import Prototype

class Student(Prototype):

  def __init__(self, name, age, email) -> None:
    self.name = name
    self.age = age
    self.__email = email


  def clone(self):
    return Student(self.name, self.age, self.__email)
