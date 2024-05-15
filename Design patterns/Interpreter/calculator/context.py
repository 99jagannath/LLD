class Context:

  def __init__(self) -> None:
    self.context_map = {}

  def add(self, key, value):
    self.context_map[key] = value


  def get(self, key):
    return self.context_map[key]