'''
    override : base class nad dirved class ame
    method same overide and same paramter

    problem

    solution
    super() : method Base class method shot skarse

'''

class A:
    def show(self):
        print("shot from class A")
class B(A):
    def show(self):
        super().show()
        print("shot from class B")
class C(A):
    def show(self):
        super().show()
        print("shot from class C")

class D(B,C):
    def show(self):
        super().show()
        print("shot from class D")

d1 = D()
d1.show()

