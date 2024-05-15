class CareTaker:

  def __init__(self) -> None:
    self.history = []

  def add_memento(self, memento):
    self.history.append(memento)

  def undo(self):
    if  len(self.history) > 0:
      return self.history.pop()
    return None