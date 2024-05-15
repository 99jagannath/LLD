
from product import Product
from shopingCart import ShoppingCart

def main():

  prod = Product("Shirt", "premium", 200)
  prod1 = Product("Pant", "regular", 150)
  cart = ShoppingCart()
  cart.add_item(prod)
  cart.add_item(prod1)

  print(cart.get_total_cost())

if __name__ == '__main__':
  main()