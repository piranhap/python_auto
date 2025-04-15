# we know that print(), len() and more are functions that exists, but you can make your own functions using def

def hello():
    print('Howdy!')
    print('Howdy!')
    print('Howdy!')

hello()
hello()
hello()

# This calls that function and runs it  3 times
# The main purpose of functions is to put functions so you don't having to write things over and over again. 

# functions can take arguments 
def hello(name):
    print("Hello "+ name)

hello('Alice')
hello('Bob')

# you can specify what will be returned at the end of a function 

def plusOne(number):
    return number + 1

plusOne(5)

# since all functions return values, what about the print function being empty?
# that is when we talk about the None value
# None = the lack of a value
# keyword arguments are optional for a function, like print, that has the keyword arguments end and sep 