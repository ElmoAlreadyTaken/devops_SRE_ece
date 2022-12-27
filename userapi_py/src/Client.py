# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:10:26 2022

@author: misha
"""
import requests

def test_create_user():
    response = requests.post('http://localhost:5000/users', json={'name': 'John', 'email': 'john@example.com'})
    print(response.text)
    assert response.status_code == 200

def test_access_main_page():
    response = requests.get('http://localhost:5000/')
    print(response)
    assert response.status_code == 200

def test_alive():
    response = requests.get('http://localhost:5000/alive')
    print(response)
    assert response.status_code == 200


test_create_user()
test_access_main_page()
test_alive()