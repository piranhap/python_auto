spam = 42 # Global variable = global scope 

def eggs():
    spam = 42 # Local variable = local scope, more temporary


# Code in the global scope cannot use anything in the local scope 

def spam():
    eggs = 99

spam()
print(eggs)

# This function will trhough an error , this is because once the function is called, once the function finishes it deletes its variables. so when eggs is called eggs has a value of None


# Local scopes can't use variables from other local scopes 

def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

# This runs spam, assigns the local scope of spam, with variable eggs = 99, then goes to bacon, defines variables ham and eggs, however, this eggs are separate from spam eggs.
#  Once the bacon function finishes, it deletes all the variables and does not return anything since there is no return word. 
# Then eggs print, instead of being 0, staying as 99 


# Code in a local scope can access a global variable 

def spam():
    print(eggs)

eggs = 42 # global eggs variable 
spam()

# This prints the global variable called eggs 
# how do I know the variable? if it is local  or not? it depends if there is an assignment within the fucntion or not. 

def spam():
    eggs = 'Hello' # local variable inside function 
    print(eggs) # Prints Hello

eggs = 42 
spam()
print(eggs) # global since out of def 

# If on functions you define global variable, then python knows to use the global version and not the local scope of it

def spam():
    global eggs
    eggs = 'Hello'
    print(eggs)

eggs = 42 
spam()
print(eggs)

# this makes the eggs variable (hello) as GLOBAL overwriting 42 when spam is called. 





