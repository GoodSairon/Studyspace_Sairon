from flask import Flask, jsonify, request
import logging as log

log.basicConfig(level = log.INFO, filename = 'log/log.log', filemode = 'a', format = "%(asctime)s %(levelname)s %(message)s")

app = Flask(__name__)

log.info("Server started")

@app.route('/chat', methods = ['POST'])

def chat():

    message = request.json

    dt = {
    "1":"one",
    "2":"two",
    "3":"three"
    }

    if message in dt.keys():
        log.warning("Message isn't in dictionary")
        log.error("I don't know xD")
        return jsonify(dt[message])
    else:
        return jsonify('Hi')

app.run()

