# interface should be such that client should implement unnecessary function they don't need

from abc import ABC, abstractmethod

class RestaurantEmployee(ABC):

    @abstractmethod
    def washDish(self):
        pass

    @abstractmethod
    def  takeOrder(self):
        pass

    @abstractmethod
    def makeFood(self):
        pass

# now let say i am creating a cook class then i have to implement the wsh dish and makeFood method 
#
# which are not required for cook class so we need to segregate the interface into multiple interfaces
    

class ChefAbsClass(ABC):

    @abstractmethod
    def cookFood(self):
        pass

class WaiterAbsClass(ABC):

    @abstractmethod
    def serveFood(self):
        pass
    

