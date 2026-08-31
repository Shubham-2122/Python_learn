'''
    oprator overloading 

    Object create thay tyre init called thay costri

    __str__ : return string nakhvi jauri che
    __str__ : class object print kariye to called karse

    __add__ : new object data show thay
'''

class Point:
    def __init__(self,x,y):
         print("init called")
         self.x = x
         self.y = y

    def __str__(self):
        print("str called")
        # argument
        return "[{0},{1}]".format(self.x,self.y)

    def __add__(self,obj):
        print("Add Called")
        x = self.x + obj.x
        y = self.y + obj.y
        return Point(x,y)
    
p1 = Point(10,20)
print(p1) # to str vali called thas

p2 = Point(30,40)
print(p2)
# + use kari s __add__ use thase
print("Addition of objects : ",p1+p2)
