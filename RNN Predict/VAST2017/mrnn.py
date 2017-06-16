# Naive LSTM to learn three-char window to one-char mapping
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.utils import np_utils

import pandas as pd
length = 119

#----------------------------------------------preprocessing--------------------------------------------------------#
file = pd.read_csv('rnn3.csv')
dim = np.arange(length).astype(str)


fileTrain = file.sample(frac=0.8, replace=True)
fileTest = file.sample(frac=0.2, replace=True)

#train
labelTrain = fileTrain[str(length)].values.astype(int)
labelTrain = np_utils.to_categorical(labelTrain, 40)
dataTrain1 = np.asarray(fileTrain[dim].values/39)
dataTrain = np.reshape(dataTrain1, (len(dataTrain1), 1, length))

#test
labelTest = fileTest[str(length)].values.astype(int)
labelTest = np_utils.to_categorical(labelTest, 40)
dataTest1 = np.asarray(fileTest[dim].values/39)
dataTest = np.reshape(dataTest1, (len(dataTest1), 1, length))

print("----------------input----------------")
print(dataTrain)
print(labelTrain)

labels = file[str(length)].values.astype(int)
inputdata1 = np.asarray(file[dim].values/40)
odata = np.asarray(file[dim].values)
inputdata = np.reshape(inputdata1, (len(inputdata1), 1, length))

print(labels)
print(inputdata)
#----------------------------------------------train--------------------------------------------------------#
model = Sequential()
model.add(LSTM(256, return_sequences=True,
               input_shape=(dataTrain.shape[1], dataTrain.shape[2])))  # returns a sequence of vectors of dimension 32
model.add(Dropout(0.5))
model.add(LSTM(256, return_sequences=True))  # returns a sequence of vectors of dimension 32
model.add(Dropout(0.5))
model.add(LSTM(256))  # return a single vector of dimension 32
model.add(Dropout(0.5))
model.add(Dense(40, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])



model.fit(dataTrain, labelTrain, nb_epoch=1000, batch_size=64)



#--------------------------------------predict and evaluation--------------------------------------------------#

print("----------------predict----------------")
output = model.predict_classes(inputdata, batch_size=64, verbose=0)
print(output)
# Final evaluation of the model
scores = model.evaluate(dataTest, labelTest, verbose=0)

print("----------------score----------------")
print("Accuracy: %.2f%%" % (scores[1]*100))

#--------------------------------------output--------------------------------------------------#

# station = pd.read_csv("station.csv").values
# station = station.ravel()
# dict = {}
# dict1 = {}
# dict[0] = 0
# for index, item in enumerate(station):
#     dict[index + 1] = item
#
# for i in range(len(output)):
#     output[i] = dict[output[i]]
#
# for i in range(len(labels)):
#     labels[i] = dict[labels[i]]
#
# print(output)

com = odata[:,len(odata[0]) - 2*20]
print(com)
print(output)
out1 = np.vstack((com, output)).T
print(out1)
result = pd.DataFrame(out1, columns = ['i','o'])
result.to_csv('re1.csv',index=False)
# result.to_csv('../../Documents/code/NesTS-Vis/visitMatrix.csv',index=True)

out2 = np.vstack((com, labels)).T
result = pd.DataFrame(out2, columns = ['i', 'o'])
result.to_csv('re2.csv',index=True)
# result.to_csv('../../Documents/code/NesTS-Vis/visitMatrix3.csv',index=True)