from Computation import Computation
from Notification import Notification
from ProductDao import ProductDao
# Hide complexcity of implementation of productDao, costComputation and  notification.

class OrderFacade:

  def __init__(self) -> None:
    self.costComputation  = Computation()
    self.notification = Notification()
    self.productDao = ProductDao()

  def makeOrder(self):
    self.productDao.getProductById(3)
    self.costComputation.getTotalComputation()
    self.notification.sendNotification()
