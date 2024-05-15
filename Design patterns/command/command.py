from abc import ABC, abstractclassmethod


class Command(ABC):

  @abstractclassmethod
  def execute(self):
    pass

  @abstractclassmethod
  def undo(self):
    pass