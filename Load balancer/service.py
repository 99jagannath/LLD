
class Service:

  def __init__(self, name):
    self.name = name
    self.destinations = set()

  def  add_destination(self, destination):
    self.destinations.add(destination)

  def remove_destinations(self, destination):
    self.destinations.remove(destination)