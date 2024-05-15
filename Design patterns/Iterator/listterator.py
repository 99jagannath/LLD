from iterator import Iterator

class ListIterator(Iterator):

  def __init__(self, num_list) -> None:
    self.list = num_list
    self.index = 0

  def has_next(self):
    return self.index < len(self.list)
  
  def next(self):
    if self.has_next():
      value = self.list[self.index]
      self.index += 1
      return value