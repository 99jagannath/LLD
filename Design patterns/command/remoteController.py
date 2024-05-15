
class Remote:

  def __init__(self, command):
    self.command = command
    self.stack = []

  def pressButton(self):
    self.stack.append(self.command)
    self.command.execute()

  def undo(self):

    if len(self.stack) > 0:
      command = self.stack.pop()
      command.undo()