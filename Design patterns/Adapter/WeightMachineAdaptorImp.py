
from WeightMachineApator import WeightMachineAdaptor

class WeightMachineAdaptorImp(WeightMachineAdaptor):

    def __init__(self, weightMachine) -> None:
        self.weightMachine = weightMachine

    def getWeightInKg(self):
        return self.weightMachine.getWeightInPound() * (0.45)