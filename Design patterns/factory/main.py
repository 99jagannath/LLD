from diagramfactory import DiagramFactory

def main():

    diagramFactory = DiagramFactory()

    circle = diagramFactory.get_diagram('circle')
    circle.draw()

if __name__ in ['main', '__main__']:
    main()