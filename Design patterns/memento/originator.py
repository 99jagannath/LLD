from memento import Memento
class Originator:

  def __init__(self, height, weight, unnecessaryProp1, unnecessaryProp2) -> None:
    self.height = height
    self.weight = weight
    self.unnecessaryProp1 = unnecessaryProp1
    self.unnecessaryProp2 = unnecessaryProp2

  def set_height(self, height):
    self.height = height

  def set_weight(self, weight):
    self.weight = weight

  def create_memento(self):
    return Memento(self.height, self.weight)

  def undo(self, memento):
    self.height = memento.height
    self.weight = memento.weight