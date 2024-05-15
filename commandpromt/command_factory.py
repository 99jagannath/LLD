from kernel import Kernel
from File_Create_command import FileCreateCmd
class Command_factory:

    def __init__(self) -> None:
        self.kernel = Kernel.get_Kernel()

    def get_command(self, keyward):
        if keyward == "touch":
            return FileCreateCmd(self.kernel)
