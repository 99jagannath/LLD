from abstractExpression import AbstractExpression

class MultiplyNonterminalExpression(AbstractExpression):

  def __init__(self, left_expression, right_expression) -> None:
    self.left_expression = left_expression
    self.right_expression = right_expression


  def  interpret(self, context):

    return  self.left_expression.interpret(context) * self.right_expression.interpret(context)