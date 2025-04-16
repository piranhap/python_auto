# Json is very similar to dictionary information, we can interact with APIs and get json in return, in this we will use api.chucknorris.io
# The website tells you how to use it 
from urllib import response
import urllib
import requests
import json


r = requests.get('https://api.chucknorris.io/jokes/random')
r = r.json() # using . json returns everything as a dictionary

# from this request we get this:

"""
{'categories': [], 'created_at': '2020-01-05 13:42:23.484083', 'icon_url': 'https://api.chucknorris.io/img/avatar/chuck-norris.png', 'id': 'uWIZNxwIREymjuSX7Xg_fA', 'updated_at': '2020-01-05 13:42:23.484083', 'url': 'https://api.chucknorris.io/jokes/uWIZNxwIREymjuSX7Xg_fA', 'value': 'Zebras were created when Chuck Norris kicked the color out of horses.'}
"""

# now we can get out values that we want, like the joke
joke = r['value']

print(f'{joke}')

# Keep in mind that you can get different things from the endpoint 
# like using https://api.chucknorris.io/jokes/random?category={money} will get us stuff like that.