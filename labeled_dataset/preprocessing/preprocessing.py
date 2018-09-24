#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:36:36 2018

@author : gaurav gahukar
        : caffeine110
    
Aim     : To preprocess the data in csv to removes NaN, and rounding of Float variables

        : input file  <<  .../to_csv/original_details.csv
        : output file <<  .../to_csv/complete_details.csv


"""
"""
        #print(df.dtypes)
        #print(df.columns)
        #print(df.head())
        #print(df.info)

"""


"""

import pandas as pd

filePath = 'datasets/labeled_dataset/processed_data.csv'
df = pd.read_csv(filePath, usecols=['sentiment_value','tweet'])

df['sentiment_value'].astype(str).astype(int)

newFilePath = 'datsets/labeled_dataset/labeled_tweets.csv'
df.to_csv(newFilePath, index=False)
"""


import pandas as pd
import numpy as np
import os

field_names = ['sentiment_value', 'id', 'date_and_time', 'query', 'tweet']



class PreProcessor(object):
    def __init__ (self,df):
        self.df = df


    def remove_Duplicates(self,df):
        df.drop_duplicates(inplace=True)

    def changeColumnNames(self,df):
        df.columns = ['sentiment_value','id','date_and_time','query','handler','tweet']


    def remove_NaN(self,df):
        
        df['sentiment_value'].fillna('Unknown', inplace=True)
        df['id'].fillna('Unknown', inplace=True)
        df['date_and_time'].fillna('Unknown', inplace=True)
        df['query'].fillna('Unknown', inplace=True)
        df['handler'].fillna('Unknown', inplace=True)
        df['tweet'].fillna('Unknown', inplace=True)
        
        
    
    def clean_tweet(self,df):
        try:
        
            return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", df.tweet).split())
        
        except:
            return 'this is neutral'


    """
    def label_Encoding(self,df):
        
        place = "Maize"
        df['crop'].fillna(place, inplace=True)
        
        
        from sklearn import preprocessing
        labelEncoder_croptype = preprocessing.LabelEncoder()
        labelEncoder_croptype.fit(df['crop'])
        labelEncoder_croptype.classes_

        labelEncoder_croptype.transform(df['crop'])
        df['crop'] = labelEncoder_croptype.fit_transform(df['crop'])
    """


    def scaler(self,df):
        pass


    def get_Details(self,df):
        print(df.count)



    def new_CSV(self,df):
        newFilePath = 'datasets/labeled_dataset/processed_data.csv'
        df.to_csv(newFilePath, index= False)
        
        
        
def main():

    filepath = 'datasets/labeled_dataset/original_data.csv'
    df = pd.read_csv(filepath, encoding='cp1252')
    print(df.count)



    #initialising object    
    api = PreProcessor(df)

    #calling functinos
    api.remove_Duplicates(df)
    api.changeColumnNames(df)
    api.remove_NaN(df)
    api.get_Details(df)
    api.new_CSV(df)


if __name__ == "__main__":
    #calling main function
    main()
