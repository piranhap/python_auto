# list aka arrays
# A list is a variable that stores multiple values :D

names = [] # this is how to define a list

#print all names 

for name in names:
    print(name)

# OR 

while True:
    name = input('enter a name  ')
    names.append(name) # append() is a builtin function we could use with lists to make your life easier
    print(name)