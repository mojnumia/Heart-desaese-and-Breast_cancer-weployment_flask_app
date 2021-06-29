from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import numpy as np 
import pandas as pd 
import pickle
from sklearn.tree import DecisionTreeClassifier
import sklearn
df=pd.read_csv('heart.csv')
X = df.drop('target',1)
y = df.target
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 2)

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
model = DecisionTreeClassifier(max_depth=5,min_samples_split=3)
model.fit(X_train,y_train)

pickle.dump(model, open('heart.pkl', 'wb'))
