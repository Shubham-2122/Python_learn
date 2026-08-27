'''
    A - C , B - C
    C(A,B)
'''

class A:

    def getA(self,a):
        self.a = a
    def putA(self):
        print("A : ",self.a)

class B:

    def getB(self,b):
        self.b = b

    def putB(self):
        print("B : ",self.b)

class C(A,B):

    def getC(self,c):
        self.c = c

    def putC(self):
        print("C : ",self.c)

demo = C()

demo.getB(20)
demo.getA(10)
demo.getC(30)

demo.putA()
demo.putB()
demo.putC()

