#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:36:36 2018

@author : gaurav gahukar
        : caffeine110
"""

import pandas as pd


filePath_r = '../data/original_data.csv'

cols = ['sentiment','id','date','query_string','user','text']


df = pd.read_csv(filePath_r,header=None, names=cols,encoding = "cp1252")

# to check the encoding of file
### encoding = utf8 may give error, so try < encoding = "cp1252" or encoding = "ISO-8859-1"

df.sentiment.value_counts()



