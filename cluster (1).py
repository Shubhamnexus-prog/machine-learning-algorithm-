# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 09:32:27 2026

@author: SHUBHAM
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 

# Importing the dataset
dataset = pd.read_csv(r"C:\Users\SHUBHAM\Downloads\Churn_Modelling.csv")
X = dataset.iloc [:,3:-1].values
y = dataset.iloc[:, -1].values

print(X)
print(y)


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
X[:,2]=le.fit_transform(X[:,2])

print(X)


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[1])],remainder='passthrough')

X=np.array(ct.fit_transform(X))


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


from xgboost import XGBClassifier
classifier = XGBClassifier()

classifier.fit(X_train,y_train)



y_pred = classifier.predict(X_test)
                            
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("Accuracy:", accuracy_score(y_test, y_pred))



print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))



print("\nClassification Report")
print(classification_report(y_test, y_pred))


from sklearn.model_selection import cross_val_score

accuracies = cross_val_score(
    estimator=classifier,
    X=X_train,
    y=y_train,
    cv=5
)

print("Accuracy: {:.2f}%".format(accuracies.mean() * 100))

print("Standard Deviation: {:.2f}%".format(accuracies.std() * 100))














