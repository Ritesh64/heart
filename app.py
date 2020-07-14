from flask import Flask, render_template, request
#import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('heartprediction.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        sex=int(request.form['sex'])
        cp=int(request.form['cp'])
        tresbps=int(request.form['tresbps'])
        chol=int(request.form['chol'])
        fbs=int(request.form['fbs'])
        rer=int(request.form['rer'])
        thalach=int(request.form['thalach'])
        exang=int(request.form['exang'])
        oldpeak=float(request.form['oldpeak'])
        slope=int(request.form['slope'])
        ca=int(request.form['ca'])
        thal=int(request.form['thal'])
        data =model.predict([[age,sex,cp,tresbps,chol,fbs,rer,thalach,exang,oldpeak,slope,ca,thal]])
        output=data[0]
        if output==0:
            return render_template('index.html',prediction_texts="You Dont Have Heart Disease")
        else:
            return render_template('index.html',prediction_text="You Have Heart Disease")
    else:
        return render_template('index.html')
if __name__ == '__main__':
    app.run()    