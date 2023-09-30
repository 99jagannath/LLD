from observer import Observer

class U1observer(Observer):

    def __init__(self, observable) -> None:
        super().__init__()
        self.observable = observable

    def update(self):
        print("The observable state is [%s]" % self.observable.state)

    def notify_me(self):
        self.observable.add_observer(self)
        print("added to notification list")