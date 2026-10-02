import pandas as pd
import pickle
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# =========================
# 1. Load Dataset
# =========================

data = pd.read_csv(r"C:\Users\SHUBHAM\OneDrive\Desktop\machine learning\multiple linear regression\car price predication\CAR DETAILS FROM CAR DEKHO.csv")

print("Dataset Shape:", data.shape)
print(data.head())


# =========================
# 2. Features and Target
# =========================

X = data[
    [
        "name",
        "year",
        "km_driven",
        "fuel",
        "seller_type",
        "transmission",
        "owner"
    ]
]

y = data["selling_price"]


# =========================
# 3. Categorical Features
# =========================

categorical_columns = [
    "name",
    "fuel",
    "seller_type",
    "transmission",
    "owner"
]

numerical_columns = [
    "year",
    "km_driven"
]


# =========================
# 4. Preprocessing
# =========================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        )
    ],
    remainder="passthrough"
)


# =========================
# 5. Multiple Linear Regression
# =========================

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", LinearRegression())
    ]
)


# =========================
# 6. Train Test Split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# =========================
# 7. Train
# =========================

model.fit(X_train, y_train)


# =========================
# 8. Prediction
# =========================

y_pred = model.predict(X_test)


# =========================
# 9. Evaluation
# =========================

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("\nModel Performance")
print("-------------------------")
print("MAE      :", mae)
print("MSE      :", mse)
print("RMSE     :", rmse)
print("R2 Score :", r2)


# =========================
# 10. Actual vs Predicted
# =========================

plt.figure(figsize=(8, 6))

plt.scatter(y_test, y_pred)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()]
)

plt.xlabel("Actual Selling Price")
plt.ylabel("Predicted Selling Price")
plt.title("Actual vs Predicted Car Prices")

plt.grid(True)
plt.show()


# =========================
# 11. Save Model
# =========================

with open("car_price_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved successfully!")