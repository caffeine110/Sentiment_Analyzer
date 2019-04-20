#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 01:06:08 2019

@author: gaurav
"""
    
##########################################################################################
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from keras.utils.np_utils import to_categorical
#import re


##########################################################################################
from preprocessing import X, Y, X_train, X_test, Y_train, Y_test
max_fatures = 2000


##########################################################################################
embed_dim = 128
lstm_out = 196

model = Sequential()
model.add(Embedding(max_fatures, embed_dim,input_length = X.shape[1]))
model.add(SpatialDropout1D(0.4))
model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(2,activation='softmax'))
model.compile(loss = 'binary_crossentropy', optimizer='adam',metrics = ['accuracy'])
print(model.summary())






##########################################################################################
### Saving the checkpoints
from keras.callbacks import ModelCheckpoint

checkpoint_name = '../checkpoints/Weights-{epoch:03d}--{val_loss:.5f}.hdf5' 
checkpoint = ModelCheckpoint(checkpoint_name, monitor='val_loss', verbose = 1, save_best_only = True, mode ='auto')
callbacks_list = [checkpoint]





##########################################################################################
### training the model    
#history = model.fit(X_train, Y_train, epochs=20, batch_size=8, validation_split = 0.2, callbacks=callbacks_list)


batch_size = 64
history = model.fit(X_train, Y_train, epochs = 5, batch_size=batch_size, validation_split = 0.4, callbacks=callbacks_list, verbose = 1)




##########################################################################################
SaveFileName = '../saved_model/Saved_model_weights.h5'
Saved_model = model.save_weights(SaveFileName)




##########################################################################################
### importing matplotlib
import matplotlib.pyplot as plt

# list all data in history
# summarize history for loss
def plot_Loss(history):
        
    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    

# summarize history for accuracy
def plot_Accuracy(history):
    # summarize history for accuracy
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()



##########################################################################################
plot_Accuracy(history)
plot_Loss(history)

#print(type(history))
print(history.history.keys())
print(history.history.values())

 

##########################################################################################
"""
from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='val_loss', patience=4)

clf_model.save('saved_model/my_clf_Model.h5')  # creates a HDF5 file 'my_model.h5'
clf_model.save_weights('checkpoints/my_clf_Model_weights.h5')
"""





print('Exicuted Succesfully EOF...')
