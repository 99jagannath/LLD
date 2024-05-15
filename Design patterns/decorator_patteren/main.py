from mushroompizza import Mushroompizza
from vegdelight import Vegdelight
import sys

def main():
    pizza = Mushroompizza((Vegdelight()))

    print(pizza.cost())

if __name__  in ['main' , '__main__']:
    sys.exit(main())