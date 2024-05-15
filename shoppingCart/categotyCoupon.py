from productDecorator import ProductDecorator

class CategoryCoupon(ProductDecorator):
  def __init__(self, baseProduct, percentage, category):
    self.baseProduct = baseProduct
    self.percentage = percentage
    self.category = category

  def get_cost(self):
    return (self.baseProduct.get_cost() - (self.baseProduct.get_cost() * self.percentage / 100)) if self.category == 'premium' else self.baseProduct.get_cost()