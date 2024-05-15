
class Student:

  def __init__(self, name, age, email) -> None:
    self.name = name
    self.age = age
    self.__email = email


def  main():

  s1 = Student("jp", 12, "99jaga@gmail.com")

  s2 = Student(s1.name, s1.age, s1.__email)


if __name__ in ['main', '__main__']:
  main()



## since Email is private member we cannot clone the student object