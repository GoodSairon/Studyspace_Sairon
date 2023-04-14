from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/words', methods = ['POST'])
def how_much_words():
    string = request.json
    return jsonify(str(len(string.split())))

app.run()
