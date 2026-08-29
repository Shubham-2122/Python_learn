class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def descibe(self):
        return f"{self.name} is {self.age} years old."


student = Student("shubham",27)
print(student.descibe()) # instace method call
