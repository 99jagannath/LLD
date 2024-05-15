from abc import ABC, abstractclassmethod

class Iterator(ABC):

  @abstractclassmethod
  def  has_next(self) -> bool:
    pass

  @abstractclassmethod
  def next(self) -> int:
    pass