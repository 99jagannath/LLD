class Student:

    def __init__(self, builder) -> None:
        self.name = builder.name
        self.age = builder.age
        self.rollNumber = builder.rollNumber
        self.subject = builder.subject

    def toString(self):
        return f"Name : {self.name}, Age : {self.age}, Roll Number: {self.rollNumber}, subject: {self.subject}"


# in Java language we have to build multiple constructor for different type of objects to get rid of multiple constructor creation we build builder design pattern