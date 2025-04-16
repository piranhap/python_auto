# Everything is an object. This is a way of seeing things as parts of something bigger.. For example, a car
# if we wanted to code a car, that would be incredibly long, since a car is complex. Seeing a car as conjunctions of objects make it easier, that way we can make the object - engine, tire, brakes, etc.
# This makes code re-usable, if you are making a plane, maybe you could take your engine code and tweak it. 

# Let's make our first object. 
names = ['Piranha']
print(type(names)) # if we run this code, we will see that names is an instance of the class list
# goign back to our example of cars, a toyota is an instance of the class car


class Car:
    color = "blue"
    make = "toyota"
    model = "tacoma"

# this is the class car, how can we use it?

car1 = Car()
car1.color = "black" # This sets a new car, car1 with their color as black

car2 = Car()
car2.color = "red"

# To effectively make an instance of it, we need to setup the class in the right way

class Car2:
    def __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model = model
        self.gas = 0 # This makes a predefined setting
    
    def get_gas(self):
        self.gas =+ 10
    
    def check_gas(self):
        return self.gas


# now we can instantiate

car100 = Car2("blue","hyundai","elantra")
car200 = Car2("grey", "lambo", "urus")

print(f"car100 has the color {car100.color}")
print(f"car200 has the color {car200.color}")