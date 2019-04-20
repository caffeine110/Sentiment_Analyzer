#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 02:30:41 2019

@author: gaurav
"""



##########################################################################################
from test_processing import X, timestamp
max_fatures = 2000


from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from keras.utils.np_utils import to_categorical

import pandas as pd
import numpy as np




def build_model(X):    

    embed_dim = 128
    lstm_out = 196
    
    # building sequential model
    model = Sequential()
    
    # adding embedding layer
    model.add(Embedding(max_fatures, embed_dim,input_length = X.shape[1]))

    # adding Spatial Dropout layer
    model.add(SpatialDropout1D(0.4))

    # add LSTM layer
    model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))

    # adding Dense Output layer
    model.add(Dense(2,activation='softmax'))

    # compile model
        # optimiser is : adam
        # loss : categorical crossentropy
    model.compile(loss = 'binary_crossentropy', optimizer='adam',metrics = ['accuracy'])

    # printing model summary
    print(model.summary())

    return model



saved_model = build_model(X)

#saved_model.load_weights('../checkpoints/Weights-003--0.41985.hdf5')
saved_model.load_weights('../checkpoints/Weights-004--0.41576.hdf5')
#saved_model.load_weights('../checkpoints/Weights-003--0.41985.hdf5')


y_pred = saved_model.predict(X)


print(y_pred)
y_pred.shape


tar = np.argmax(y_pred, axis=1)
print(len(tar))
print(tar)





new_df = pd.Series(tar)
type(new_df)

timestamp['sentiment'] = new_df

timestamp.head()

#fileName = 'final_pred_ChowkidarChorHai.csv'


fileName = 'final_pred_MainBhiChowkidar.csv'


timestamp.to_csv(fileName)


"""
from sklearn.metrics import accuracy_score

acc = accuracy_score(Y_test, y_pred)
print('Model Accuracy is :',acc)
"""








print('program Exicuted Succesfully...')