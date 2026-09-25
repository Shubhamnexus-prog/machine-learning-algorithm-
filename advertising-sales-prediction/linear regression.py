# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:30:03 2026

@author: SHUBHAM
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

dataset = pd.read_csv(r'C:\Users\SHUBHAM\OneDrive\Desktop\machine learning\advertising-sales-prediction/Advertising.csv')

dataset.head()

# Check the shape of dataset
print("Dataset Shape:", dataset.shape)

print("\nFirst 5 rows:")
print(dataset.head())


# ------------------------------------------------------------
# 4. Independent and Dependent Variables
# ------------------------------------------------------------

# Independent variable = TV advertising
# Dependent variable   = Sales

x = dataset[["TV"]]
y = dataset["sales"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=0)


# train model
regressor = LinearRegression()
regressor.fit(x_train,y_train)

#predict
y_pred = regressor.predict(x_test)
print(y_pred)

# 8. Compare Actual and Predicted values

comparison = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

print("\nActual vs Predicted:")
print(comparison)

# plot

plt.scatter(
    x_train,
    y_train,
    color="red"
)

plt.plot(
    x_train,
    regressor.predict(x_train),
    color="blue"
)

plt.title("TV Advertising vs Sales - Training Set")
plt.xlabel("TV Advertising Budget")
plt.ylabel("Sales")

plt.show()

# 10. Test Set Visualization

plot_df = pd.DataFrame({
    "TV": x_test["TV"].values,
    "Sales": y_test.values,
    "Predicted": y_pred
})

plot_df = plot_df.sort_values("TV")


plt.scatter(
    plot_df["TV"],
    plot_df["Sales"],
    color="red"
)

plt.plot(
    plot_df["TV"],
    plot_df["Predicted"],
    color="blue"
)

plt.title("TV Advertising vs Sales - Test Set")
plt.xlabel("TV Advertising Budget")
plt.ylabel("Sales")

plt.show()

#Intercept and Coefficient

print(regressor.intercept_)
print(regressor.coef_[0])


m = regressor.coef_[0]
b = regressor.intercept_

print(f"Sales = {m:.4f} × TV + {b:.4f}")

# bias and variance

bias = regressor.score(x_train, y_train)

variance = regressor.score(x_test, y_test)

print(bias)
print(variance)


print("\n========== STATISTICS ==========")

print("\nMean:")
print(dataset.mean(numeric_only=True))

print("\nTV Mean:")
print(dataset["TV"].mean())

print("\nSales Mean:")
print(dataset["sales"].mean())

print("\nMedian:")
print(dataset.median(numeric_only=True))

print("\nSales Mode:")
print(dataset["sales"].mode())

print("\nDescribe:")
print(dataset.describe())

print("\nVariance:")
print(dataset.var(numeric_only=True))

print("\nStandard Deviation:")
print(dataset.std(numeric_only=True))

print("\nCorrelation:")
print(dataset.corr(numeric_only=True))

#mea mse r2 rmes


from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

MAE = mean_absolute_error(y_test, y_pred)

MSE = mean_squared_error(y_test, y_pred)

RMSE = np.sqrt(MSE)

R2 = r2_score(y_test, y_pred)


print("\n========== MODEL EVALUATION ==========")

print("MAE :", MAE)
print("MSE :", MSE)
print("RMSE:", RMSE)
print("R²  :", R2)


# sse ssr sst
y_test_mean = np.mean(y_test)


# SST = Total Sum of Squares
SST = np.sum(
    (y_test - y_test_mean) ** 2
)


# SSR = Regression Sum of Squares
SSR = np.sum(
    (y_pred - y_test_mean) ** 2
)


# SSE = Sum of Squared Errors
SSE = np.sum(
    (y_test - y_pred) ** 2
)


print("\n========== SUM OF SQUARES ==========")

print("SST:", SST)

print("SSR:", SSR)

print("SSE:", SSE)

print("SSR + SSE:", SSR + SSE)


print("\nChecking:")

print(
    "SST ≈ SSR + SSE:",
    np.isclose(SST, SSR + SSE)
)


R2_manual = 1 - (SSE / SST)

print("\nManual R²:")
print(R2_manual)

print("\nSklearn R²:")
print(R2)


R2_using_SSR = SSR / SST

print("\nR² using SSR/SST:")
print(R2_using_SSR)


new_data = pd.DataFrame({
    "TV": [250]
})

new_prediction = regressor.predict(new_data)

print("\n========== NEW PREDICTION ==========")

print("TV Advertising Budget:", 250)


print("Predicted Sales:", new_prediction[0])


import pickle
filename = 'linear_regressor_sales_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(regressor, file)
print("Model has been pickled and saved as linear_regression_model.pkl")

import os
print(os.getcwd())

