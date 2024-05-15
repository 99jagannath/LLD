from ExternalButtonDispacher import ExternalButtonDispacher
class Floor:

    def __init__(self, no) -> None:
        self.externalButtonDispacher = ExternalButtonDispacher()
        self.no = no

    def pressButton(self):
        inputDir = input()
        self.externalButtonDispacher.submitRequest(self.no, inputDir)