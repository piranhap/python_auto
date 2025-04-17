# Let's look into requests and response objects, manipulating headers and using authentication, using sessions, ignore ssl warnings, specific exceptions, etc.

# Request and Response

import requests

url = 'https://github.com/'

response = requests.get(url)

#print(response) # This gets a 200 response, on class = requests.models.Response object, you can google this object to see all the functions you can use, like status codes.

if response.status_code == 200:
    print('url is good!')
elif response.status_code == 403:
    print('you must be logged in, auth required')
elif response.status_code == 404:
    print('error 404, maybe you need to authenticate?')

