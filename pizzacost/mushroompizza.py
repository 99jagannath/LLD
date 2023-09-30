from pizzadecorator import Pizzadecorator


class Mushroompizza(Pizzadecorator):

    def __init__(self, basepizza) -> None:
        super().__init__()
        self.basepizza = basepizza

    def cost(self):
        return self.basepizza.cost() + 50
