# if class B is a subclass of A then we should be able to replace obj A with Object B without breaking the code flow.
# child class should extend the capability of parent class rather than reducing the capability

class Vehicle:

    def getEngine(self):
        pass

    def noOfWheel(self):
        pass

class Car(Vehicle):

    def getEngine(self):
        return "BS6"

    def noOfWheel(self):
        return 4


class BiCycle(Vehicle):

    def getEngine(self): # here we are reducing the capability of parent
        return None
    
    def noOfWheel(self):
        return 2
    

def main():

    vehicles = [Car(), BiCycle()]

    for vehicle in vehicles:
        print(vehicle.getEngine().upper())  # calling method from base class using derived object

if __name__ in ['main', '__main__']:
    main()

## solution
# keep the methods which are  common to all classes as they are in the parent class and add new methods  to child if there is a functionality

class Vehicle:
    def noOfWheel(self):
        pass