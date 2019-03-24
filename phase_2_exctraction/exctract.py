#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:36:36 2018

@author : gaurav gahukar
        : caffeine110
    
Aim     : To read downloaded file using proper encodeing
        : To remove NaN
        : To Exctract importent data
        
        : input file  <<  ...data/original_details.csv
        : output file <<  ...phase_1_exctraion/sentiment_tweet.csv
"""



# importing pandas
import pandas as pd


# remove duplicates
def removeDuplicates(df):
    df.drop_duplicates(inplace=True)
    return df

# function to change cloumn names
def changeColumnNames(df):
    df.columns = ['sentiment_value','id','date_and_time','query','handler','tweet']
    return df

# removing empty fields
def removeNaN(df):
    #remove NaN
    df['sentiment_value'].fillna('neutral', inplace=True)
    df['id'].fillna('Unknown', inplace=True)
    df['date_and_time'].fillna('Unknown', inplace=True)
    df['query'].fillna('Unknown', inplace=True)
    df['handler'].fillna('Unknown', inplace=True)
    df['tweet'].fillna('Unknown', inplace=True)
    return df

# get MetaData
def getDetails(df):
    print("Columns of csv")
    print(df.columns)

    print("Data types of each data fields")
    print(df.dtypes)

    print("Counts of each data Fields")
    print(df.count)

    print("Sample of data is")
    print(df.head(10))

    print("Meta data")
    print(df.info)


# write file
def writeFile(df):
    # filePath to write the sentiment_tweet file
    filePath_w = 'exctracted_sentiment_tweet.csv'
    cols = ['sentiment_value','tweet']

    # write into file
    df.to_csv(filePath_w, index = False, columns = cols)


# main Method
def main():

    filePath_o = '../data/original_data.csv'
    df = pd.read_csv(filePath_o, encoding = 'cp1252')
    
    # removing the duplicates entries
    df = removeDuplicates(df)
    
    # modify column names
    df = changeColumnNames(df)

    # remove NaN
    df = removeNaN(df)    
    
    # get Meta data
    #df = getDetails(df)

    #replace sentiment values    
    df = df.replace(4,1)
    
    # function call to witer file
    writeFile(df)
    #print(df.head(5))
    #print(df.tail(5))

    print("End of main...")






if __name__ == "__main__":
    main()