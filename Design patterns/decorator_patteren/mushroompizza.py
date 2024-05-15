from pizzadecorator import Pizzadecorator


class Mushroompizza(Pizzadecorator):

    def __init__(self, basepizza) -> None:
        self.basepizza = basepizza

    def cost(self):
        return self.basepizza.cost() + 50
