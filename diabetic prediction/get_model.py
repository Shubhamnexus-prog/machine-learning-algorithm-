import pickle
import pandas as pd


class LoadModel:

    # Loading the model
    def __init__(self, MODEL_PATH):
        self.loaded_model = pickle.load(open(MODEL_PATH, 'rb'))

    def predict_class(self, pregnant, insulin, bmi, age, glucose, bp, pedigree):

        # Initialize list of lists
        data = [[pregnant, insulin, bmi, age, glucose, bp, pedigree]]

        # Create pandas DataFrame
        df = pd.DataFrame(
            data,
            columns=[
                'pregnant',
                'insulin',
                'bmi',
                'age',
                'glucose',
                'bp',
                'pedigree'
            ]
        )

        new_pred = self.loaded_model.predict(df)

        return new_pred


# Test LoadModel
if __name__ == '__main__':

    MODEL_PATH = r"C:\Users\SHUBHAM\OneDrive\Desktop\diabetic prediction\models\logistic_regression_model.pkl"

    model = LoadModel(MODEL_PATH)

    predicted_class = model.predict_class(
        6,       # pregnant
        0,       # insulin
        33.6,    # bmi
        50,      # age
        148,     # glucose
        72,      # bp
        0.627    # pedigree
    )

    print(predicted_class)

