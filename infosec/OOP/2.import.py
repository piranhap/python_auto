# We learned how to make the class Car, can I use it on a different program. Yes! 
# From last example we created the class Car and Car2
# for sanity, we will make it official, making cars.py with our class

import cars #As you can see, we were able to import cars.py

car1 = cars.Car("green", "honda", "civic")
print(car1.color) # This prints green

# you can also import certain functions or classes from other files using from
from cars import Car