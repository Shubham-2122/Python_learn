class Emp:

    def getData(self,fname,lname):
        self.f = fname
        self.l = lname

    def putData(self):
        print("First name : ",self.f)
        print("Last name : ",self.l)

e1 = Emp()
e1.getData("sujal","jadav")
e1.putData()
