from abc import ABC, abstractclassmethod

class WeightMachine(ABC):

    @abstractclassmethod
    def getWeightInPound(self):
        pass

