from abc import ABC,abstractmethod

class RBI(ABC):

    @abstractmethod # class inherite karvu pade to j abstract method banse
    #abstact class kayre object create thay nahi
    # roi : rate of interest
    def roi(self,r):
        pass

class SBI(RBI):
    def roi(self,r):
        print("Rate of interest given by Sbi is :",r)

class HDFC(RBI):
    def roi(self,r):
        print("Rate of interest given by HDFC is :",r)

s1 = SBI()
s1.roi(6.5)

h1 = HDFC()
h1.roi(7.2)
