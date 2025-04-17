# Headers is metadata from either the response or the request. It is important to know this because we need to manipulate some stuff becasue some websites like to block you thinking you are a crawling bot, the website needs to know the user agent to keep websites responsive.


import requests


url = 'https://github.com/'
h = {
    'User-Agent': 'Mozilla/5.0' # If you change this to GoogleBot, it will probably be blocked.
}

# Some websites block python requests as well, so you need to change the User-Agent to something that will likely be accepted.




response = requests.get(url)

print(response.headers)