from flask import Flask, request, render_template
import numpy as np

import pickle

app = Flask(__name__)


with open('model.pkl', "rb") as f:
    model = pickle.load(f)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    output = 0
    if request.method == "POST":
        output = "0"
        f = request.form['Fever']
        cough = request.form['Cough']
        SoreThroat = request.form['Sore_Throat']
        sob = request.form['Shorteness_of_breath']
        Head_Ache = request.form['Head_Ache']
        age = request.form['age']
        gender = request.form['gender']
        test_indication = request.form['Test_indication']

        #     Converting all the categorical Features into Numberical
        #     Converting Fever(1)
        if f == "yes":
            f = "1"
            f = int(f)
        elif f == "no":
            f = "0"
            f = int(f)
        #     Converting cough
        if cough == "yes":
            cough = "1"
            cough = int(cough)
        elif cough == "no":
            cough = "0"
            cough = int(cough)

        # Converting Sore Throat
        if SoreThroat == "yes":
            SoreThroat = "1"
            SoreThroat = int(SoreThroat)
        elif SoreThroat == "no":
            SoreThroat = "0"
            SoreThroat = int(SoreThroat)

        # Converting SOB
        if sob == "yes":
            sob = "1"
            sob = int(sob)
        elif sob == "no":
            sob = "0"
            sob = int(sob)
        # Converting Head_Ache
        if Head_Ache == "yes":
            Head_Ache = "1"
            Head_Ache = int(Head_Ache)
        elif Head_Ache == "no":
            Head_Ache = "0"
            Head_Ache = int(Head_Ache)

        # Converting age
        if age == "yes":
            age = "1"
            age = int(age)
        elif age == "no":
            age = "0"
            age = int(age)

        # Converting gender
        if gender == "male":
            gender = "1"
            gender = int(gender)
        elif gender == "female":
            gender = "0"
            gender = int(age)

        test_indication = int(test_indication)

        feat = [np.array([int(cough), int(f), int(SoreThroat), int(sob), int(Head_Ache), int(age), int(gender), int(test_indication)])]
        prediction = model.predict_proba(feat)
        output = '{0:.{1}f}'.format(prediction[0][1], 2)
        output = float(output)
        output = round(output*100, 2)
        return render_template('index.html', pred=output)
    output = float(output)
    output = round(output * 100, 2)
    return render_template('index.html', pred=output)


if __name__ == '__main__':
    app.run(debug=True)
