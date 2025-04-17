# Let's write to files oh yea boi (txt file)
filename = 'test.txt'
test_text = 'This is a test\n'

f = open(filename, mode='a')
# w means that everything in that file will be overwritten
# a means append to the end of the file

f.write(test_text)
f.write('This is line 2')
f.close() # ALWAYS have to close a file after using it



