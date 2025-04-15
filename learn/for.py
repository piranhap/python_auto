# For loops, instead of iterating until something happens, you set up already how many times it will iterate over the loop 

print('my name is: ')
for i in range(5):
    print('Jimmy Five Times '+ str(i))

# This will print Jimmy Give Times 0 to 4 

# let's calculate 1+2+3+4+5+ . . . 100

total = 0 
for num in range(101):
    total = total + num
print(total)

# You can still do a while loop to do the same as a for loop, but a for loop is more concise 

print('My name is')
i = 0 
while i < 5:
    print('Jimmy Five Times '+ str(i))
    i = i + 1

# you can also do break or continue statements in for loops the same way you do in while 