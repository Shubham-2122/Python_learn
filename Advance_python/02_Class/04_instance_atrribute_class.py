class Car:

    # constructor : automatically call 
    def __init__(self,brand,model):
        self.brand = brand # instance attribute
        self.model = model # instance attribute

# creating instances of the car class
car1 = Car("Toyota","camry")
car2 = Car("Honda","civic")

print(car1.brand)
print(car1.model)

print(car2.brand)
print(car2.model)
