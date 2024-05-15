from Airconditioner import AirConditioner
from remoteController import Remote
from turnoffcommand import TurnOffCommand
from TurnOnCommand import TurnOnCommand


class  Client:

  def start(self):

    self.remote = Remote(TurnOnCommand(AirConditioner()))
    self.remote.pressButton()
    self.remote.undo()


Client().start()