filename = 'test.txt'
test_text = 'This is a test \n'



lines = []


f = open(filename, 'r') # r for read 

lines = f.readlines()


f.close()

for line in lines:
    print(line)
