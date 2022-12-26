# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 15:31:30 2022

@author: misha
"""

from flask import Flask, jsonify, request
import redis
import uuid

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')
def hello():
    return 'Welcome on the web server !'

@app.route('/users', methods=['POST'])
def create_user():
    id = str(uuid.uuid4()) # generate a unique ID for the user
    name = request.json['name']
    email = request.json['email']
    r.hmset(f'user:{id}', {'name': name, 'email': email})
    return jsonify({'id': id, 'name': name, 'email': email})


if __name__ == '__main__':
    app.run()