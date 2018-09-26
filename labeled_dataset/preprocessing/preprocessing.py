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



import pandas as pd
import numpy as np
import os
import re

field_names = ['sentiment_value', 'id', 'date_and_time', 'query','handler', 'tweet']



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
        
        

    def scaler(self,df):
        pass


    def get_Details(self,df):
        print(df.count)
        #print(df.dtypes)
        #print(df.columns)
        #print(df.head())
        #print(df.info)



    def new_CSV(self,df):
        newFilePath = 'labeled_dataset/preprocessing/processed_data.csv'
        df.to_csv(newFilePath, index= False)
        
        
    def make_Tweet_File(self, df):
        newFilePath = 'labeled_dataset/clean_tweet/sentiment_tweet.csv'
        df.to_csv(newFilePath, index=False)


        
def main():

    filepath = 'labeled_dataset/original_data/original_data.csv'
    df = pd.read_csv(filepath, encoding='cp1252')


    #initialising object    
    api = PreProcessor(df)

    #calling functinos
    api.remove_Duplicates(df)
    api.changeColumnNames(df)
    api.remove_NaN(df)
    api.get_Details(df)
    api.new_CSV(df)


    filepath = 'labeled_dataset/preprocessing/processed_data.csv'
    df = pd.read_csv(filepath, usecols=['sentiment_value','tweet'])
    
    api.make_Tweet_File(df)
    

if __name__ == "__main__":
    #calling main function
    main()
