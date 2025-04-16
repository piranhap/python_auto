# What is an API? A way 2 apps can communicate with each other. An API endpoint is a web server that receives api requests only. 
# In order to make a request to an API endpoint, we need certain packages, a third party one called requests

import requests #if you don't have it just do pip install requests

r = requests.get('https://www.google.com')
print(r)

# If we run this, we will get a 200 response back from the server

print(r.text)

# this will return the HTML from that site, as if you were loading it
