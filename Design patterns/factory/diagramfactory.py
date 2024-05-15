from circle import Circle
from rectanlge import Rectangle

class DiagramFactory:

    def get_diagram(self, diagram):

        match diagram:
            case 'circle':
                return Circle()
            case 'rectangle':
                return Rectangle()