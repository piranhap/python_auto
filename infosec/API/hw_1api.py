"""

Choose an API from the resource called 'A list of a TON of FREE API's' from the last video. Pick at least 5 different pieces of information from the json response.

Create a text interface that will make requests based on user input.

NOTE: You will need to research how to handle a response that comes from a user searching or trying to search for something that does not exist. 200 is success, what is the response code of an unsuccessful query? Use an if statement to sort this out and allow the user to try again.

"""

import requests
import json

base_url = "https://api.filterlists.com/lists"

try:
    r = requests.get(f'{base_url}')
    r.raise_for_status()
    result = r.json()

    language_37_lists =[]
    for item in result:
        if 'languageIds' in item: # if it exists
            if 37 in item['languageIds']: # if it exists, look for 37
                language_37_lists.append(item) # if both apply, add to the list
        else:
            print('No lists with language 37 here')
    
    for list_item in language_37_lists:
        print("-" * 50)
        print(f"Name: {list_item.get('name')}")
        print(f"Language ID: {list_item.get('languageIds')}")
        print(f"URL: {list_item.get('primaryViewUrl')}")
except:
    print('Error')
























