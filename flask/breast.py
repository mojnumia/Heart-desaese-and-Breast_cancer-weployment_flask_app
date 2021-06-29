
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler,StandardScaler,LabelEncoder
import numpy as np 
import pandas as pd 
import pickle
from sklearn.tree import DecisionTreeClassifier
import sklearn
df=pd.read_csv('data.csv')
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
df.diagnosis = le.fit_transform(df.diagnosis)
y=df.diagnosis
y
x=df.drop(['texture_mean','diagnosis','smoothness_mean','compactness_mean','smoothness_se','symmetry_se','fractal_dimension_se','symmetry_mean','texture_se',
	'perimeter_se','compactness_se','concavity_se','concave points_se','fractal_dimension_mean','smoothness_worst','symmetry_worst','fractal_dimension_worst'],axis=1)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators = 15, criterion='entropy', random_state=0)
model.fit(x_train,y_train)
pickle.dump(model, open('breast.pkl', 'wb'))
