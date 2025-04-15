# dictionaries have keys and values, like a word - definition 
# so we can have our key: goon 
# and value : addicted to ****
# The way you write is key:value

person = {
    'name': 'piranha',
    'job' : 'jobless'
} # dictionary is curly braces 
# do you see how a dictionary is SO similar to JSON? it is important to know this since we could use that in infosec. 

print(person)

# to add to teh dictionary you do:

person['eats_pizza'] = True

# you can nest dictionaries inside of a list and crazy stuff like that

people = [{'name: Piranha'},{'name: poranha'}, {'name: puranha'}]
for person in people: 
    print(person) # print everything
    print(person['name']) # print just names

