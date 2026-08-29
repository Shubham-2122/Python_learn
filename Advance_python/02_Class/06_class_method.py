class Student:
    subject = "python" # class attribute
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def get_subject(cls):
        return cls.subject

    @classmethod
    def set_subject(cls,new_subject):
        cls.subject = new_subject
        
#calling class method
print(Student.get_subject()) # python

# modifying class attribute using class method
Student.set_subject("javascript")
print(Student.get_subject())
        
