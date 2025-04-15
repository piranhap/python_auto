# value that contains multiple values in an ordered sequence
# They have [] brackets

spam = ['cat', 'rat', 'bat']
# to call something on the list you do list and index number
spam[0] # this is cat, since indexes start at 0


# you can make a list of lists

spam = [['cat', 'bat'], [10, 20, 30, 40]]
spam[0][1] # first index, then second word, bat

# negative indexes
spam = ['cat', 'rat', 'bat']
spam[-2] # this just counts from rigjt to left -2 being rat

# slices can get several values from a list
spam[1:2]
# this goes from 1 to 2, [1:15] will go from 1 to 15 without counting 15


# assign values to a list
spam = [10, 20, 30]
spam[1] = 'hello'
# This changes 20 to Hello 

# we can delete stuff from lists

spam = ['cat', 'rat', 'bat', 'elephant']
del spam[2] # this unassigns from index 2, in this case bat

# to see what is or isnt on a list 

'howdy' in ['hello', 'hi', 'howdy', 'heya'] # this returns True

'howdy' not in ['hello', 'hi', 'howdy', 'heya'] # this returns False, since it is there