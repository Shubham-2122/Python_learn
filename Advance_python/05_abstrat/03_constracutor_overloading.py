'''
    Method Ek j but Argument ni leg defualt behivir kari
    rhi che aetle controctor ne overloading
    object
    class inside init method only one create
'''

class Rectangle:
    def __init__(self,*args):
        if len(args) == 0:
            self.width = 0
            self.height = 0
        elif len(args) == 1:
            self.width = args[0]
            self.height = args[0] #square case
        elif len(args) == 2:
            self.width = args[0]
            self.height = args[1]

    def display(self):
        print(f"width : {self.width} , height : {self.height}")

# creating Rectangel objects in different ways
r1 = Rectangle() # default rectangle (0*0)
r2 = Rectangle(5) # square(5*5)
r3 =  Rectangle(4,6) # Reactangle (4*6)

r1.display()
r2.display()
r3.display()
