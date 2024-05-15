
from WeightMachineAdaptorImp import WeightMachineAdaptorImp
from WeightMachineForBabies import WightMachineForBabies


class main:

    def __init__(self) -> None:
        self.WeightMachineAdaptor = WeightMachineAdaptorImp(WightMachineForBabies())


    def getWeightInKg(self):
        print(self.WeightMachineAdaptor.getWeightInKg())

main().getWeightInKg()