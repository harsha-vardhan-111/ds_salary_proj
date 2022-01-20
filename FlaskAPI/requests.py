# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 00:52:41 2022

@author: Harsha Vardhan
"""

import requests 
from data_input import data_in

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": data_in}

r = requests.get(URL,headers=headers, json=data) 

r.json()