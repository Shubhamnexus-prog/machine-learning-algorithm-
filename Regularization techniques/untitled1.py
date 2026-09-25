# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 09:28:31 2026

@author: SHUBHAM
"""
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 20 house, salary (thousand mein) + label
X = [[92], [88], [95], [85], [91], [99], [83], [96], [89], [93],
     [30], [25], [35], [28], [32], [22], [38], [27], [33], [26]]

y = ["Rich"]*10 + ["Middle-class"]*10

# Step 1: Split data in train and test (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 2: Create Model aur train Model
K = 3
model = KNeighborsClassifier(n_neighbors=K)
model.fit(X_train, y_train)

# Step 3: Prediction on test data
y_pred = model.predict(X_test)

# Step 4: Accuracy calculate (How many predictions are correct)
accuracy = accuracy_score(y_test, y_pred)

print("Test data:      ", X_test)
print("Actual labels:  ", y_test)
print("Predicted labels:", list(y_pred))
print(f"\nAccuracy = {accuracy * 100:.2f}%")
'==================================================================='
' Testing the Model'
testing= model.predict([[70]])
print(testing)