from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update():
        pass

    @staticmethod
    def notify_me():
        pass