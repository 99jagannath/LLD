from EmployeeDao import EmployeeDao

class EmployeeDaoImpl(EmployeeDao):

    def createEmployee(self, client):
        print("%s employee is created" % client)