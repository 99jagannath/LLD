from abc import ABC, abstractmethod

class Observable(ABC):

    @abstractmethod
    def add_observer():
        pass

    @abstractmethod
    def remove_observer():
        pass

    @abstractmethod
    def notify():
        pass

    @abstractmethod
    def update_state():
        pass

    @abstractmethod
    def get_state():
        pass