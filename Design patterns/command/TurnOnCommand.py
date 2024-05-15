from command import Command

class TurnOnCommand(Command):

  def  __init__(self, receiver):

    self.receiver = receiver


  def execute(self):
    self.receiver.turnOn()

  def undo(self):
    self.receiver.turnOff()
