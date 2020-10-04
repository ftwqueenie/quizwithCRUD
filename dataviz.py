# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:05:32 2020

@author: Queenie
"""

import pandas as pd

reader = pd.read_csv("scoreboard.txt",delimiter='\t', header=None)
   
reader.columns = ['player', 'score', 'rating']
reader.to_csv('scoreboard.csv', index=False)