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
class C(B):
    def show(self):
        super().show()
        print("shot from class C")

c1 = C()
c1.show()

