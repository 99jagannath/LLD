from EngineeringStudentBuilder import EngineeringStudentBuilder
from MBAStudentBuilder import MBAStudentBuilder

class Director:

    def __init__(self, studentBuilder) -> None:
        self.studentBuilder = studentBuilder

    def getStudent(self):

        if isinstance(self.studentBuilder, EngineeringStudentBuilder):
            return self.createEngineeringStudent()
        else:
            return self.createMBAStudent()
        
    def createEngineeringStudent(self):
        return self.studentBuilder.setRollNumber(1).setAge(24).setName("Jagan").build()
    
    def createMBAStudent(self):
        return self.studentBuilder.setRollNumber(2).setAge(25).setName("Jagannath").build()