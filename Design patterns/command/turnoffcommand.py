from command import Command


class TurnOffCommand(Command):

  def __init__(self, receiver):
    self.receiver = receiver

  def  execute(self):
    self.receiver.turnOff()

  def undo(self):
    self.receiver.turnOn()