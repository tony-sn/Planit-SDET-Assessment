''' Challenge 006:
Make an API call to https://petstore.swagger.io/v2/pet/findByStatus?status=available and display a count of the number of pets in the result
'''

import requests
import json

API = 'https://petstore.swagger.io/v2/pet/findByStatus?status=available'
response_API = requests.get(API)

data = response_API.text
pet_list = json.loads(data)

print('Number of pet from the API are {number}'.format(number=len(pet_list)))