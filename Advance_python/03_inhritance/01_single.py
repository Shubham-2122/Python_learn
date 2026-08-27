'''
    Single Level : A to B clas data pass karva
    inheritnace B(A)
        B : child
        A : pranent

'''

class A:

    def getA(self,a):
        self.a = a
    def putA(self):
        print("A : ",self.a)

class B(A):

    def getB(self,b):
        self.b = b

    def putB(self):
        print("B : ",self.b)

demo = B()

demo.getB(20)
demo.getA(10)

demo.putA()
demo.putB()











        
