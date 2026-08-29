from abc import ABC,abstractmethod

class Tops(ABC):
    def show(self):
        print("This Show From Tops")

    @abstractmethod # class inherite karvu pade to j abstract method banse
    #abstact class kayre object create thay nahi
    def courses(self):
        pass

class TopsNikol(Tops):
    def courses(self):
        print("you can lern python,java,php,Testing")
    
t1 = TopsNikol()
t1.show()
t1.courses()
