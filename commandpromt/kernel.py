from threading import Lock
class Kernel:

    __kernel = None
    lock = Lock()

    def get_Kernel():

        if Kernel.__kernel is not None:
            return Kernel.__kernel
        with Kernel.lock:
            Kernel.__kernel = Kernel()
            return Kernel.__kernel
        
    def destroy_kernel():
        Kernel.__kernel = None


    def __init__(self) -> None:
        self.memory = {}

    def create_file(self):
        file = File()
        self.memory[file.get_id()] = file
        print("File created successfully")

k = Kernel.get_Kernel()

    