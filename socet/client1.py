import requests

def how_much_words(string):
    responce = requests.post('http://127.0.0.1:5000/words', json = string)
    if responce.ok:
        return print(responce.json())
    return None

while True:
    how_much_words(input())
