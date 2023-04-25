import requests

def calc():
    responce = requests.post("http://127.0.0.1:5000/calc")
    #if responce.ok:

calc()
