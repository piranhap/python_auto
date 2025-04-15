# Index() returns the index of a list 
spam = ['hello', 'hi', 'howdy']
spam.index('hello')
# Returns 0 
spam.index('howdy')
# Returns 2

# append()
spam.append('yoo')
# This adds yoo to the list

# remove()
spam.append('hello')

# removes it from the list, only once, so if you have duplicates it will only remove the first one

spam.sort() # This one sorts a list, ASCII betical ordering, putting caps first and then lowercase
spam.sort(reverse=True) # reverse order

# sort breaks with numbners and list 

spam = ['ants', 23, 'dogs', 3.14]

