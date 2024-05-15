
from abc import ABC, abstractclassmethod
from product import Product
class ProductDecorator(ABC, Product):

  @abstractclassmethod
  def get_cost(self):
    pass