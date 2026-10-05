
from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import base64
import os

app = Flask(__name__)

# Current project folder
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Image is in the same folder as app.py
IMAGE_PATH = os.path.join(BASE_PATH, "house.jpg")


# Load ML models
model_names = [
    'LinearRegression',
    'RobustRegression',
    'RidgeRegression',
    'LassoRegression',
    'ElasticNet',
    'PolynomialRegression',
    'SGDRegressor',
    'ANN',
    'RandomForest',
    'SVM',
    'LGBM',
    'XGBoost',
    'KNN'
]

models = {}

for name in model_names:
    model_path = os.path.join(BASE_PATH, f"{name}.pkl")

    if os.path.exists(model_path):
        with open(model_path, 'rb') as file:
            models[name] = pickle.load(file)
    else:
        print(f"Model not found: {name}.pkl")


# Load evaluation results
results_path = os.path.join(
    BASE_PATH, "model_evaluation_results.csv"
)

results_df = pd.read_csv(results_path)


# Convert house.jpg into Base64
def get_image_base64(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(
                image_file.read()
            ).decode("utf-8")

        print("House image loaded successfully")
        return encoded_image

    print("House image not found:", image_path)
    return None


house_image = get_image_base64(IMAGE_PATH)


# Home page
@app.route('/')
def index():
    return render_template(
        'index.html',
        model_names=list(models.keys()),
        house_image=house_image
    )


# House price prediction
@app.route('/predict', methods=['POST'])
def predict():
    model_name = request.form['model']

    input_data = {
        'Avg. Area Income': float(
            request.form['Avg. Area Income']
        ),
        'Avg. Area House Age': float(
            request.form['Avg. Area House Age']
        ),
        'Avg. Area Number of Rooms': float(
            request.form['Avg. Area Number of Rooms']
        ),
        'Avg. Area Number of Bedrooms': float(
            request.form['Avg. Area Number of Bedrooms']
        ),
        'Area Population': float(
            request.form['Area Population']
        )
    }

    input_df = pd.DataFrame([input_data])

    if model_name in models:
        model = models[model_name]
        prediction = model.predict(input_df)[0]

        return render_template(
            'results.html',
            prediction=prediction,
            model_name=model_name,
            house_image=house_image
        )

    return jsonify({
        'error': 'Model not found'
    }), 400


# Model evaluation page
@app.route('/results')
def results():
    return render_template(
        'model.html',
        tables=[
            results_df.to_html(
                classes='data',
                index=False
            )
        ],
        titles=results_df.columns.values,
        house_image=house_image
    )


if __name__ == '__main__':
    app.run(debug=True)

