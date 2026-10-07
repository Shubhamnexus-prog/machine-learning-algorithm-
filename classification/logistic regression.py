# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:09:18 2026

@author: SHUBHAM
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv(r"D:\ds 2\N_Batch -- 4.00PM -- Jun 26\3. Mar 26\13th, 16th - logistic, pca\15. Logistic regression with future prediction\15. Logistic regression with future prediction/Social_Network_Ads.csv")



X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, -1].values

'''
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25,random_state=0)

X_test.shape


y_test.shape
'''
# split data 20%--
'''
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 20,random_state=0)
'''

# using random state 100--
'''
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 20,random_state=100)
'''

# using random state 51--
'''
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 20,random_state=51)

'''

# using random state 41--

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 20,random_state=41)



#norimalizer--
#from sklearn.preprocessing import Normalizer

#sc = Normalizer()

#X_train = sc.fit_transform(X_train)
#X_test = sc.transform(X_test)

#print(X_test)




from sklearn.linear_model import LogisticRegression 
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

y_pred


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)


from sklearn.metrics import accuracy_score 
ac = accuracy_score(y_test, y_pred)
print(ac) 



from sklearn.metrics import classification_report

cr = classification_report(y_test, y_pred)
print(cr) 

bias=classifier.score(X_train,y_train)
print(bias)


variance=classifier.score(X_test,y_test)
variance
  


# Hyperparameter Tuning

from sklearn.model_selection import GridSearchCV

param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],
    'solver': ['lbfgs', 'liblinear'],
    'class_weight': [None, 'balanced']
}

grid = GridSearchCV(
    LogisticRegression(max_iter=1000),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

grid.fit(X_train, y_train)

print("Best Parameters:", grid.best_params_)
print("Best CV Accuracy:", grid.best_score_)

# Best model prediction
best_model = grid.best_estimator_
y_pred_tuned = best_model.predict(X_test)

print("Tuned Accuracy:", accuracy_score(y_test, y_pred_tuned))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_tuned))
print("Classification Report:\n",
      classification_report(y_test, y_pred_tuned))
print("Training Accuracy:", best_model.score(X_train, y_train))
print("Testing Accuracy:", best_model.score(X_test, y_test))
