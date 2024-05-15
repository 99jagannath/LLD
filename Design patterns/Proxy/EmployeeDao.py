from abc import ABC, abstractclassmethod

class EmployeeDao(ABC):

    @abstractclassmethod
    def createEmployee(self, client):
        pass