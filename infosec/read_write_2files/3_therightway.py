# Proper way to open and close files 

filename = 'test.txt'
test_text = 'This is a test'

with open(filename, 'w') as f: # With this you don't have to automatically close it
    f.write('hello\n')

# NEVER place keys, secrets, passwords inside of your source code! ! ! !


