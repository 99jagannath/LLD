from abstractExpression import AbstractExpression


class TerminalExpression(AbstractExpression):

  def __init__(self, state) -> None:
    self.state = state

  def interpret(self, context):
    return context.get(self.state)