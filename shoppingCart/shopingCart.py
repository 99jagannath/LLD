from percentageCoupon import PercentageCoupon
from categotyCoupon import CategoryCoupon
class ShoppingCart:

  def __init__(self) -> None:
    self.items = []
  
  def add_item(self, product):
    self.items.append(CategoryCoupon(PercentageCoupon(product, 0.1), 0.2, 'premium'))

  def get_total_cost(self):
    total_cost = 0
    for  item in self.items:
      total_cost += item.get_cost()
    return total_cost