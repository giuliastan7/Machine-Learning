# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15zP2jZ3Eek3nVX_dpOl-jGHQMfNqfGB8
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

date_inima = pd.read_csv('/content/data.csv')

date_inima.head()

date_inima.tail()

date_inima.shape

date_inima.info()

date_inima.isnull().sum()

date_inima.describe()

"""Verificam distributia variabilei target in tot setul de date"""

date_inima["target"].value_counts()







X=date_inima.drop(columns='target',axis=1)
Y=date_inima['target']
print(X)
print(Y)

"""Impartim datele in training data si test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Training my model- Logistic Regression"""

model= LogisticRegression()

model.fit(X_train, Y_train)

"""Evaluarea modelului - acuratetea"""

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on training data :  ', training_data_accuracy)

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on test data :  ', test_data_accuracy)

input_data=(71,0,1,160,302,0,1,162,0,0.4,2,2,2)

input_data_as_numpy_array=np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction=model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]==0):
  print("Persoana nu este bolnava ")
else:
  print("Persoana  este bolnava")