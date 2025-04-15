# part 1 
# Lets say we are gonna enter a number (age) and calculate their age plus 30 years 

age = int(input('Enter your age to see how old you will be in 30 years ')) 


# here we know we need to use int to convert the input (that comes in str) to int

# what if the freaking user inputs strings instead of a number? That is when we use try - exception :D

# # if you as teh programmer do not handle the exceptions, the hacker will # # 

try:
    age = int(input('Enter your age to see how old you will be in 30 years ')) 
    print(age + 30)
except: # There is a list of exceptions online https://docs.python.org/3/library/exceptions.html 
    print('Something went wrong')