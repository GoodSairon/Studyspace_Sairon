import requests

def message(message):

    responce = requests.post('http://127.0.0.1:5000/chat', json = message)

    if responce.ok:
        return print(responce.json())

    return None

while True:
    message(input())

