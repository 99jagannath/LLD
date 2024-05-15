
from EmployeeDao import EmployeeDao
from EmployDaoImpl import EmployeeDaoImpl


class EmployeeDaoProxy(EmployeeDao):

    def __init__(self) -> None:
        self.employeeDaoImpl = EmployeeDaoImpl()

    def createEmployee(self, client):
        if client != 'ADMIN':
            return False
        self.employeeDaoImpl.createEmployee(client)
        return True