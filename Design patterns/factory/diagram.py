from abc import ABC, abstractmethod

class Diagram(ABC):

    @abstractmethod
    def draw():
        pass