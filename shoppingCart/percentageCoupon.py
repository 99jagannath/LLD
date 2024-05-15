from productDecorator import ProductDecorator


class PercentageCoupon(ProductDecorator):

  def __init__(self, baseProduct, percentage) -> None:
    self.baseProduct  = baseProduct
    self.percentage = percentage

  def get_cost(self):
    return (self.baseProduct.get_cost() -  (self.baseProduct.get_cost() * self.percentage / 100)) if self.baseProduct.get_cost() > 100 else self.baseProduct.get_cost()