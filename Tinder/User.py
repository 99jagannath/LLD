
class User:

  def __init__(self, id, name, gender, location, radius, looking_for) -> None:
    self.id = id
    self.name = name
    self.gender = gender
    self.location = location
    self.radius = radius
    self.looking_for = looking_for

  def update_radius(self, radius):
    self.radius = radius