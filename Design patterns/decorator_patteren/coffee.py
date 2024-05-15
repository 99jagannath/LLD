from abc import ABC, abstractclassmethod
class coffee:

    def price(self):
        return 8
    

class decorator(ABC):

    @abstractclassmethod
    def price(self):
        pass


class milk_decorator(decorator):

    def __init__(self, coffee) -> None:
        self.baseCoffee = coffee

    
    def price(self):
        return self.baseCoffee.price() + 5
    
class  sugar_decorator(decorator):

    def __init__(self, coffee) -> None:
        self.baseCoffee = coffee

    def price(self):
        return self.baseCoffee.price() + 2
    

coffee = coffee()

milk_coffee = milk_decorator(coffee)

milk_with_sugar_coffee = sugar_decorator(milk_coffee)

print(milk_with_sugar_coffee.price())