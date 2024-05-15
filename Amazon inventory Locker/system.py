from item import Item

class System:

  def __init__(self) -> None:
    self.product_list = {}
    self.locker_list = {}
    self.free_locker_map = {} # Map of size to the set of  free lockers in that size
    self.product_item_map = {}
    self.item_locker_map = {}

  def place_item(self, product):
    item = Item(product.id + "Item", product.id)
    locker = self.get_free_locker_space(product.get_size())
    locker.add_item(item)
    self.item_locker_map[item.get_unique_id()] = locker.get_id()

  def update_free_locker_space(self, locker):
    self.free_locker_map[locker.get_size()].remove(locker.id)

  def add_item_to_product_map(self, item):
    product_id = item.get_product_id()
    if product_id not in self.product_item_map:
      self.product_item_map[product_id] = []
    self.product_item_map[product_id].append(item)

  def get_item(self, product_name):
    product = self.get_product(product_name)
    item = self.product_item_map[product.id].pop()
    locker_id = self.item_locker_map[item.id]
    return self.locker_list[locker_id]


    
