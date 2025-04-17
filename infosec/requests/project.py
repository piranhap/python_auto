import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout, TooManyRedirects
from gtoken import get_token



token = get_token()
user = 'piranhap'
auth_header = (user,token)
header = {
    'Authorization': 'token ' + token
}

base_url = 'https://api.github.com'

# Login using token to get username from header
login = requests.get(f"{base_url}/user", headers=header)
print(login.json())

# Create a session to get a cookie

s = requests.Session()
for i in range(1,5):
    s.get(f'{base_url}/users/{user}/repos', headers=header)


# List Repos https://api.github.com/users/piranhap/repos