# Write a program that takes an age and will tell you if you are able to drive or not

age = int(input('Please enter your age '))

# Heres an if statement, it is a moment where we ask for 2 paths 
# in this case is age below 18? 
if age >= 18:
    print('you can drive')
elif age <= 18:
    print('you canNOT drive')