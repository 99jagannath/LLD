from Director import Director
from EngineeringStudentBuilder import EngineeringStudentBuilder
from MBAStudentBuilder import MBAStudentBuilder

class Client:

    def __init__(self) -> None:
        self.engineeringDirector = Director(EngineeringStudentBuilder())
        self.mbaDirector         = Director(MBAStudentBuilder())

    def getEngineeringStudent(self):
        print(self.engineeringDirector.createEngineeringStudent().toString())


client = Client()

client.getEngineeringStudent()