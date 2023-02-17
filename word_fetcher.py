import requests
import json

def get_word():
    response = requests.get('https://random-word-api.herokuapp.com/word')
    response_list = response.json()
    word = response_list[0]
    return word

