# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 13:18:18 2026

@author: SHUBHAM
"""


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

# Input: study hours
X = np.array([
    [1], [2], [3], [4], [5],
    [6], [7], [8], [9], [10]
])

# Output: 0 = Fail, 1 = Pass
y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Create and train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

print("Actual values:", y_test)
print("Predicted values:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Predict for a student who studies 6 hours

new_student = np.array([[2]])
prediction = model.predict(new_student)
probability = model.predict_proba(new_student)[0][1]

print("Pass probability:", round(probability * 100, 2), "%")
print("Prediction:", "Pass" if prediction[0] == 1 else "Fail")

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
 
# Plot sigmoid probability curve
hours = np.linspace(0, 11, 200).reshape(-1, 1)
probabilities = model.predict_proba(hours)[:, 1]

plt.scatter(X.ravel(), y, label="Training examples")
plt.plot(hours.ravel(), probabilities, label="Logistic curve")
plt.axhline(0.5, linestyle="--", label="Decision threshold")
plt.xlabel("Study Hours")
plt.ylabel("Probability of Passing")
plt.title("Logistic Regression: Student Pass Prediction")
plt.legend()
plt.grid(True)
plt.show()