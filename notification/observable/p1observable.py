from observable import Observable

class P1observalble(Observable):

    def __init__(self) -> None:
        super().__init__()
        self.observer_list = []
        self.state = 0

    def add_observer(self, observer):
        self.observer_list.append(observer)
        print("observer added")

    def remove_observer(self, observer):
        if observer in self.observer_list:
            self.observer_list.remove(observer)
            print("observer removed")
        else:
            print("Observer [%s] not found")

    def notify(self):
        for observer in self.observer_list:
            observer.update()
            print("observer notified")

    def update_state(self, state):
        if self.state != state:
            self.state  = state
            self.notify()
            print("state updated")

    def get_state(self):
        print("Current state is %s" % self.state)

