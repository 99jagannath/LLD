from context import Context
from multiplyNonterminalExpression import MultiplyNonterminalExpression
from terminalExpression import  TerminalExpression


def main():

  context = Context()
  context.add('a', 5)
  context.add('b', 2)

  expression  = MultiplyNonterminalExpression(TerminalExpression('a'), TerminalExpression('b'))
  print(expression.interpret(context)) # Output: a * b = 2

if __name__ == '__main__':
  main()