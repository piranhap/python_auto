import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout, TooManyRedirects

url = 'https://reddit.com'

try:
    response = requests.get(url)
except ConnectionError:
    print('DNS, refused connection')
except HTTPError:
    print('This is due to a response code being 4xx or 5xx')
except Timeout:
    print('Connection timed out, slow connection or url issue')
except TooManyRedirects:
    print('There were more redirects than what you allowed')


# This helps you with Troubleshooting if you are messing with requests, handling the exception will save you time in the long run 