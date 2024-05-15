from abc import ABC, abstractclassmethod

class WeightMachineAdaptor(ABC):

    @abstractclassmethod
    def getWeightInKg(self):
        pass