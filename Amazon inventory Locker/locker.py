
class Locker:

  def __init__(self, id, size, distance) -> None:
    self.id = id
    self.size = size
    self.distance = distance
    self.item = None

  def add_item(self, item):
    self.item = item

  def remove_item(self):
    self.item = None