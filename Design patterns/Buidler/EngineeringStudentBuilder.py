from StudentBuilder import StudentBuilder

class EngineeringStudentBuilder(StudentBuilder):

    def setSubject(self):
        self.subject = ['ee', 'cse']
        return self