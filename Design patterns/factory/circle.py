from diagram import Diagram

class Circle(Diagram):

    def __init__(self) -> None:
        super().__init__()

    def draw(self):
        print("Drawing a circle....")