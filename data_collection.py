# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 20:55:25 2022

@author: Harsha Vardhan
"""

import glassdoor_scrapper as gs
import pandas as pd

path = 'C:/Users/Harsha Vardhan/projects/ds_salary_proj/chromedriver'
df = gs.get_jobs('data scientist',15,False,path,15)
df