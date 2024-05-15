
from abc import ABC, abstractclassmethod


class Prototype(ABC):

  @abstractclassmethod
  def clone(self):
    pass