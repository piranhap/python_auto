def div42by(divideby):
    return 42 / divideby

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

# This crashes de code since 42 can't be divided by 0, so the program exits. What if we don't want the program to shut down and continue but notify the user, this is when we use try except. 

def div42by(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print('Error, you tried to divide by 0')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

# this does not crash the prorgam and the program just prints everything. 

print('How many cats do you own?')
numCats = input()
if int(numCats) >= 4:
    print('That is a lot of cats')
else:
    print('That is not that many cats')

# if we put 6 or space or a string 'six', this will kill the program

print('How many cats do you own?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats')
    else:
        print('That is not that many cats')
except:
        print('You did not enter a number, or entered a negative number')


print('How many cats do hyou have')
numcats = input()
try:
    if int(numCats) >= 4:
        print('that is a lot')
    else: 
        print('not a lot')
except Exception:
    print('exception')