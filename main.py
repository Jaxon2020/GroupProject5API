from flask import Flask, jsonify, escape, request, Response
import random
import hashlib
import math

# instansiate the Flask object
app = Flask(__name__)

# the main route url route
@app.route('/')
def hello():
    return "Hello, Welcome to group project #5."

''' example
@app.route('/md5/<string>')
def json_response():
    resp = Response('{ "foo": "bar", "baz": "bat" }')
    resp.headers['Content-Type'] = 'application/json'
    return resp
'''
# Calculation for factorials
def factorial():
    n = int(input("enter a number:"))
    factorial = 1
    if n == 0:
        print("The factorial of 0 is 1")
    else:
       for i in range(1,n + 1):
           factorial = factorial*i
       print("The factorial of number:",factorial)  
