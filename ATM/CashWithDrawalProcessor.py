from abc import ABC

class CashWithDrawalProcessor(ABC):

    def __init__(self, processor) -> None:
        self.processor = processor

    def withDraw(self, atm, amount):
        if self.processor is not None:
            self.processor.withDraw(atm, amount)