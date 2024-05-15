class Product:

  def __init__(self, name, category, price) -> None:
    self.name = name
    self.category = category
    self.price = price

  def get_category(self):
    return self.category

  def get_cost(self):
    return self.price