name = ''
while name != 'your name':
    print('Please type your name')
    name = input()
print('thank you')


# The loop runs until the user inputs 'your name'

# We can also uset the break word to exit the loop 

name = ''
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

# Continue statements can be used in while loop, where the it gets restarted 

spam = 0 
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is '+ str(spam))

# If you run this code above, it will print everything but 3, since the interpreter hits continue and immediately goes back to the start

