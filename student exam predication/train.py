# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 23:19:53 2026

@author: SHUBHAM
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#load the dataset

dataset=pd.read_csv(r"C:\Users\SHUBHAM\Downloads/Exam_Score_Prediction.csv")

print('dataset shape:',dataset.shape)

dataset.head()

x = dataset[["study_hours"]]
y = dataset["exam_score"]

#missing value--
# Check missing values
print(dataset.isnull().sum())

from sklearn.model_selection import train_test_split
x_train ,x_test ,y_train ,y_test =train_test_split(x,y, test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

#predict the model

y_pred=regressor.predict(x_test)

#plot

plt.figure(figsize=(8, 5))

plt.scatter(
    x_test,
    y_test,
    color="red",
    alpha=0.3,
    s=15,
    label="Actual Data"
)

plt.plot(
    x_train,
    regressor.predict(x_train),
    color="blue",
    linewidth=2,
    label="Regression Line"
)

plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.legend()
plt.grid(alpha=0.2)

plt.show()
# slop and intercept

print(f"Intercept: {regressor.intercept_}")
print(f"Coefficient: {regressor.coef_}")



bias = regressor.score(x_train, y_train)
print(bias)

variance = regressor.score(x_test,y_test)
print(variance)

# comprision actual predict

comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(comparison)

#STATISTICS FOR MACHINE LEARNING

print("Mean:", dataset['exam_score'].mean())
print("Median:", dataset['exam_score'].median())
print("Mode:", dataset['exam_score'].mode()[0])
print("Variance:", dataset['exam_score'].var())
print("Standard Deviation:", dataset['exam_score'].std())

print("\nDescription:")
print(dataset['exam_score'].describe())

print("\nCorrelation:")
print(dataset[['study_hours', 'exam_score']].corr())


from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, y_pred)
print("MAE:", mae)

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)

import numpy as np

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("RMSE:", rmse)



import numpy as np

# Predictions
y_train_pred = regressor.predict(x_train)
y_pred = regressor.predict(x_test)

# -------------------------
# SSR
# -------------------------
y_test_mean = np.mean(y_test)

SSR = np.sum((y_pred - y_test_mean) ** 2)
print("SSR:", SSR)

# -------------------------
# SSE
# -------------------------
SSE = np.sum((y_test - y_pred) ** 2)
print("SSE:", SSE)

# -------------------------
# SST
# -------------------------
SST = np.sum((y_test - y_test_mean) ** 2)
print("SST:", SST)

# -------------------------
# R²
# -------------------------
r_square = 1 - (SSE / SST)
print("R²:", r_square)

# -------------------------
# Training and Testing R²
# -------------------------
train_r2 = regressor.score(x_train, y_train)
test_r2 = regressor.score(x_test, y_test)

print("Training R²:", train_r2)
print("Testing R²:", test_r2)
