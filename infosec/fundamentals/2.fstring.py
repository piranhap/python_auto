# We know we can print on the screen, but there is a trick to print in the required format

name = input('What is your name?')
print(name)

# way 1 
print('Hello! ' + name) # remember to add spaces when using +

# way 2 fstring (format)
print(f'Hello! {name} how are you doing today?')


