# -*- coding: utf-8 -*-
"""
Logistic Regression - Complete Code
Author: Shubham Gupta
"""

# Import Libraries


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Load Dataset

dataset = pd.read_csv(r"C:\Users\SHUBHAM\Downloads\logit classification.csv")

print(dataset.head())
print(dataset.info())
print(dataset.describe())


# Independent & Dependent Variable

X = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:, -1].values


# Train Test Split


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=100
)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=80
)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=60
)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=51
)

# Feature Scaling


from sklearn.preprocessing import StandardScaler

sc = StandardScaler()


X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# Logistic Regression Model


from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression(random_state=0)

classifier.fit(X_train, y_train)


# Prediction

y_pred = classifier.predict(X_test)



# Prediction Probability

y_prob = classifier.predict_proba(X_test)

print("\nProbability Prediction")
print(y_prob)


# Actual vs Predicted


result = pd.DataFrame({

    "Actual": y_test,
    "Predicted": y_pred

})

print(result)


# Accuracy


from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy =", accuracy)



# Confusion Matrix

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix")
 
print(cm)


# Classification Report


from sklearn.metrics import classification_report

print("\nClassification Report")

print(classification_report(y_test, y_pred))




# Precision


from sklearn.metrics import precision_score

precision = precision_score(y_test, y_pred)

print("\nPrecision =", precision)


# Recall


from sklearn.metrics import recall_score

recall = recall_score(y_test, y_pred)

print("Recall =", recall)

# F1 Score


from sklearn.metrics import f1_score

f1 = f1_score(y_test, y_pred)

print("F1 Score =", f1)


# ROC AUC Score 

from sklearn.metrics import roc_auc_score

roc = roc_auc_score(y_test, y_pred)

print("ROC AUC Score =", roc)



new_data = sc.transform([[30,87000]])

prediction = classifier.predict(new_data)

print("\nPrediction for New Customer =", prediction)

if prediction==1:
    print("Customer will Purchase")
else:
    print("Customer will NOT Purchase")

# ===============================
# Decision Boundary Visualization
# ===============================

from matplotlib.colors import ListedColormap

X_set, y_set = X_train, y_train

X1, X2 = np.meshgrid(
    np.arange(start=X_set[:,0].min()-1,
              stop=X_set[:,0].max()+1,
              step=0.01),

    np.arange(start=X_set[:,1].min()-1,
              stop=X_set[:,1].max()+1,
              step=0.01)
)

plt.contourf(
    X1,
    X2,
    classifier.predict(
        np.array([X1.ravel(),X2.ravel()]).T
    ).reshape(X1.shape),
    alpha=0.75,
    cmap=ListedColormap(('red','green'))
)

plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())

for i,j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set==j,0],
        X_set[y_set==j,1],
        c=ListedColormap(('red','green'))(i),
        label=j
    )

plt.title("Logistic Regression (Training Set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()
plt.show()

# ===============================
# Model Coefficients
# ===============================

print("\nIntercept")

print(classifier.intercept_)

print("\nCoefficients")

print(classifier.coef_)








