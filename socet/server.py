from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/chat', methods = ['POST'])

def chat():

    message = request.json

    dt = {
    "1":"one",
    "2":"two",
    "3":"three"
    }

    if message in dt.keys():
        return jsonify(dt[message])
    else:
        return jsonify('Hi')

app.run()

