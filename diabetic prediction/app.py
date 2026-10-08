
from flask import Flask, render_template, request

import sys
import os

# Add current project folder to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from get_model import LoadModel


# Loading the model
MODEL_PATH = r"C:\Users\SHUBHAM\OneDrive\Desktop\diabetic prediction\models\logistic_regression_model.pkl"

model = LoadModel(MODEL_PATH)


# App config
DEBUG = True

app = Flask(__name__)

app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


# Home route
@app.route("/")
def index():
    return render_template("index.html")


# Diagnosis route
@app.route("/diagnosis", methods=['POST'])
def diagnosis():

    name = request.form['name']

    age = int(request.form['age'])
    pregnant = int(request.form['pregnant'])
    insulin = float(request.form['insulin'])
    bmi = float(request.form['bmi'])
    pedigree = float(request.form['pedigree'])
    glucose = float(request.form['glucose'])
    bp = float(request.form['bp'])

    # Predict
    prediction = model.predict_class(
        pregnant,
        insulin,
        bmi,
        age,
        glucose,
        bp,
        pedigree
    )

    print("Prediction:", prediction)

    # Result
    if prediction[0] == '1':
        return render_template("positive.html", result="true")

    elif prediction[0] == '0':
        return render_template("negetive.html", result="true")


if __name__ == "__main__":
    app.run(debug=True)

