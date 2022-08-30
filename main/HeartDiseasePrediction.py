# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model

filename = 'stc.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':

        age = int(request.form['age'])
        sex = request.form.get('sex')
        height = request.form.get('height')
        weight = int(request.form['weight'])
        smoke = int(request.form['smoke'])
        stroke = request.form.get('stroke')
        alcohol = int(request.form['alcohol'])
        physicalhealth = int(request.form['physicalhealth'])
        mentalhealth = request.form.get('mentalhealth')
        diffwalking = float(request.form['diffwalking'])
        diabetes = request.form.get('diabetes')
        asthma = int(request.form['asthma'])
        kidneydisease = request.form.get('kidneydisease')
        skincancer = request.form.get('skincancer')
        physicalActivity = request.form.get('physicalActivity')
        Genhealth = request.form.get('Genhealth')
        sleep = request.form.get('sleep')
        
        if height == 0:
            height = 1.69
        if weight == 0:
            weight = 65


        BMI = weight/(height**2)
        Severity = sum(asthma, kidneydisease, skincancer, diabetes)

        if age>= 29:
            AgeCategory25to29 = 1
        elif (age >= 30) & (age>= 34):
            AgeCategory30to34 = 1
        elif (age >= 35) & (age<= 39):
            AgeCategory35to39 = 1            
        elif (age >= 40) & (age<= 44):
            AgeCategory40to44 = 1
        elif (age >= 45) & (age<= 49):
            AgeCategory45to49 = 1
        elif (age >= 50) & (age<= 54):
            AgeCategory50to54 = 1
        elif (age >= 55) & (age<= 59):
            AgeCategory55to59 = 1
        elif (age >= 60) & (age<= 64):
            AgeCategory60to64 = 1
        elif (age >= 65) & (age<= 69):
            AgeCategory65to69 = 1
        elif (age >= 70) & (age<= 74):
            AgeCategory70to74 = 1
        elif (age >= 75) & (age<= 79):
            AgeCategory75to79 = 1
        elif age >= 80:
            AgeCategory80orolder = 1

        sleep = (sleep - 0) / (23)
        physicalhealth = physicalhealth /30
        mentalhealth = mentalhealth /30
    
        data = np.array([[BMI, physicalhealth, mentalhealth, Genhealth, sleep,
        Severity, smoke, alcohol, stroke,
        diffwalking, sex, AgeCategory25to29, AgeCategory30to34,
        AgeCategory35to39, AgeCategory40to44, AgeCategory45to49,
        AgeCategory50to54, AgeCategory55to59, AgeCategory60to64,
        AgeCategory65to69, AgeCategory70to74, AgeCategory75to79,
        AgeCategory80orolder, physicalActivity]])

        my_prediction = model.predict(data)
        
        return render_template('result.html', prediction=my_prediction)
        
        

if __name__ == '__main__':
	app.run(debug=True)