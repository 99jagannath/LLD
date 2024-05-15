from abc import ABC, abstractclassmethod
from Student import Student
class StudentBuilder(ABC):

    def setRollNumber(self, rollNumber):
        self.rollNumber = rollNumber
        return self
    
    def setAge(self, age):
        self.age = age
        return self
    
    def setName(self, name):
        self.name = name
        return self
    
    @abstractclassmethod
    def setSubject(self):
        pass

    def build(self):
        return Student(self)