import requests
import json

def get_dict_def(word):
    api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    combined = api_url + word
    response = requests.get(combined)
    response_json = response.json()
    print(response_json)

