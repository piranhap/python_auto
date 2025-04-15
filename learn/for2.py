# You can use the list function to convert range to list 
# list(range(4))
# will convert to [0,1,2,3] instead of (0,4)

# a good technique to do is for i in range(len(someList)): having i as an index
# for example 
supplies = ['pens', 'staplers', 'binders', 'pc']
for i in range(len(supplies)):
    print('Index', str(i), 'in supplies is:', supplies[i])

# which returns 
"""
Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: binders
Index 3 in supplies is: pc

"""

# Multiple assignment short cut 

cat = ['fat', 'orange', 'loud'] # To assign each to a different variable we could do
size = cat[0]
color = cat[1]
personality = cat[2]

# OR WE COULD DO

size, color, personality = cat

# or 

size, color, personality = 'skinny', 'black', 'quiet'

# this is often used to swap variables 

a = 'AAA'
b = 'BBB'

a, b = b, a # this swaps aaa and bbb so b = aaa and a = bbb

# to do incrementals you could do 
spam = 42
spam = spam + 1
# or 
spam += 1 
