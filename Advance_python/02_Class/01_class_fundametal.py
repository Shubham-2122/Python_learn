'''
    class is object blue print of object
    self automatically varibale banavase
    self is compusry it is object defualt banavelo lo

    Class name First always be capital
'''
    
class Student:

    def getData(self,fname,lname):
        self.f = fname
        self.l = lname
        
    def putData(self):
        print("First Name : ",self.f)
        print("Last Name : ",self.l)

s1 = Student()
s1.getData("shubham","jadav")
s1.putData()
