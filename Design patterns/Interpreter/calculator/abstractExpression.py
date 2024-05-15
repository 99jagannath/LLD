from abc import ABC, abstractclassmethod


class AbstractExpression(ABC):

  @abstractclassmethod
  def interpret(self, context):
    pass