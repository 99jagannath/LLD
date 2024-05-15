# class should depend upon interface rather than concrete class

class MacBook:

    # Two instance Variable
    # WiredKeyboard
    # WiredMouse

    def __init__(self) -> None:
        self.wiredKeyboard = WiredKeyBoard()
        self.wiredMouse = WiredMouse()

    # but now if we want to switch to  a wireless keyboard and mouse, then it's problem bcz we are using a concrete class as variable
        
    def __init__(self) -> None:
        self.keyBoard = WirelessKeyboard()
        self.mouse = WirelessMouse()


