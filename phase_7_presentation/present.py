#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:30:22 2019

@author: gaurav
"""

import pandas as pd

fileName = '../phase_3_cleaning/cleaned_sentiment_tweet.csv'


df = pd.read_csv(fileName)

df.columns

df_positive = df[ df['sentiment_value'] == 1 ].head(50)
df_negative = df[ df['sentiment_value'] == 0 ].head(50)


#final_df = pd.concat(df_positive, df_negative, ignore_index=True)


final_df = df_negative
final_df = final_df.append(df_positive)


fileName_w = 'final_test_present.csv'

final_df.to_csv(fileName_w, index=False)





print('EOF')