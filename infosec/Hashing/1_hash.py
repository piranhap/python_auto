# Hash converts passwords so they are stored securely so they cannot be read in plain text. 
#  Hash -> one way function -> you can't really un-blend a smoothie, but you can keep trying to make fruit combinations until you get the same taste. Then you know what the recipe was, this is called 'cracking', and that is the correct way to refer to hashed passwords. Passwords are cracked, or hash looked up, but they aren't 'reversed', 'decrypted', 'bruteforced' . . .

# We use Bcrypt for this demo

import bcrypt 

password = 'Password123'

# What is a salt ? 
# to salt a hash is to insert characters somewhere in the hash of something.

# b crypt only works in bytes, so we need to use .encode

hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() # This hashed our password and encodes it so it works as bytes.Then, we use the gensalt function to just generate a salt for us
# The problem, is that if we want to print the hash, to see it, we need to decode it since it is still bytes.

# How do we check to see if it is the correct password?

given = input('Please enter a password ')
is_correct = bcrypt.checkpw(given.encode(), hashed.encode())
# Run this and try diff passwords and then the right one, bcrypt checks the password and compares to what its given, and then hashed
print(is_correct)