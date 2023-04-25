from flask import Flask, jsonify, request
import asyncio

app = Flask(__name__)

@app.route('/calc', methods = ['POST'])

async def calc():
    a = input()
    b = input()
    print(a+b)

app.run()

