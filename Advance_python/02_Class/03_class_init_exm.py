class Car:
    wheels = 4 # class attribute same valu re

    # constructor : automatically call 
    def __init__(self,brand,model):
        self.brand = brand # instance attribute
        self.model = model # instance attribute

# creating instances of the car class
car1 = Car("Toyota","camry")
car2 = Car("Honda","civic")

print(car1.wheels)
print(car2.wheels)

print(car1.brand)
print(car1.model)

print(car2.brand)
print(car2.model)
