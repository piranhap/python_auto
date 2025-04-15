# There are a lot of builtin functions, the Standard Library. 
# the math module has mathematical functions, before using them, you need to import them.

import random
random.randint(1,10)

# you can import several stuff with commas 

import random, sys, os , math

# or import everything from random, so you can just call the function 

from random import * 
randint(1,10)
# it is more normal to use the first example instead of this

# there are several modules online that are third party, like asyncio or stuff. you need to use pip to install them on the terminal 
# on the terminal, type pip install <package>
