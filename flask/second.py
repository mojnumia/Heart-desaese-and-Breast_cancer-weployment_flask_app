from flask import Blueprint,render_template,url_for,request
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import sklearn
import pickle
from sklearn.preprocessing import MinMaxScaler

loaded_model = pickle.load(open('heart1.pkl', 'rb'))
loaded_model1 = pickle.load(open('breast.pkl', 'rb'))




second=Blueprint("second", __name__)
@second.route('/home')
def home():
	return render_template('base.html')

@second.route('/heart')
def heart():
	return render_template('heart.html')

@second.route('/skin')
def skin():
	return render_template('skin.html')
@second.route('/breast')
def breast():
	return render_template('breast.html')

@second.route('/predict', methods=['GET', 'POST'])
def hpredict():
	if request.method == 'POST' :
		data1= request.form['a']
		data2=request.form['b']
		data3=request.form['c']
		data4=request.form['d']
		data5=request.form['e']
		data6=request.form['f']
		data7=request.form['g']
		data8=request.form['h']
		data9=request.form['i']
		data10=request.form['j']
		data11=request.form['k']
		data12=request.form['l']
		data13=request.form['m']
		arr=np.array([[data1,data4,data8,data3,data2,data6,data7,data11,data12,data13,data9,data10,data5]])
		
		pre=loaded_model.predict(arr)
		return render_template('prediction.html', data=pre)

@second.route('/predicts', methods=['GET', 'POST'])
def bpredict():
	if request.method == 'POST' :
		data1= request.form['a']
		data2=request.form['b']
		data3=request.form['c']
		data4=request.form['d']
		data5=request.form['e']
		data6=request.form['f']
		data7=request.form['g']
		data8=request.form['h']
		data9=request.form['i']
		data10=request.form['j']
		data11=request.form['k']
		data12=request.form['l']
		data13=request.form['m']
		data14=request.form['n']
		arr=np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14]])
		pre=loaded_model1.predict(arr)
		return render_template('predictions.html', data=pre)