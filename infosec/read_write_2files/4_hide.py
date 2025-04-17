# Never place pass, secrets, anything confidential in source code
import json # Refer to credentials.json
# json should always be in double quotes instead of one 

with open('credentials.json', 'r') as cred_file:
    data = json.load(cred_file) # this loads the data as a dictionary
    cred_file.close()

email = data['email_credentials']['email']
password = data['email_credentials']['password']

print(email, password)

if data['print_settings']['everything_upper']:
    print(email.upper())
else:
    print(email)

    # This example shows how you can have a config file to show certain things in a way.
    # it is recommended to have all confidential stuff to another place, like credentials.json

