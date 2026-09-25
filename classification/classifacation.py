# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 09:34:40 2026

@author: SHUBHAM
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import dataset
dataset = pd.read_csv(r"C:\Users\SHUBHAM\Downloads\final1.csv")

# Encode categorical column
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
dataset["Gender"] = le.fit_transform(dataset["Gender"])

# Features and target
X = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:, -1].values

# Split dataset
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=0
)

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Train SVM
from sklearn.svm import SVC

classifier = SVC(kernel='linear', random_state=0)
classifier.fit(X_train, y_train)

# Predict
y_pred = classifier.predict(X_test)

print(y_pred)
