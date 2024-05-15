from diagram import Diagram

class Rectangle(Diagram):

    def __init__(self) -> None:
        super().__init__()

    def draw(self):
        print("Drawing rectangle ....")