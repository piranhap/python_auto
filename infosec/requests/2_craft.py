# Let's craft a request
import requests 

url = 'https://github.com/'

# cookies need to be set up at dictionaries
c = {
    'test_cookie': 'say something random'
}
h = {
    'User-Agent': 'Mozilla/5.0'
}




response = requests.get(
    url,
    cookies=c,
    headers=h
)

code = response.status_code
print(code)


# As you can see, we can setup different things within our request function. It would be good if you lookup the request.get functions and give them a try.