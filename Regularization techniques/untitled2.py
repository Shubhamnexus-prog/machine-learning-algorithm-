# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 09:36:43 2026

@author: SHUBHAM
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"D:\ds 2\N_Batch -- 4.00PM -- Jun 26\3. Mar 26\9th, 10th - svr, dtr, rf,knn, notes\emp_sal.csv")

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


# svm model
from sklearn.svm import SVR
svr_regressor = SVR(kernel='poly',degree = 5,gamma = 'scale' )
svr_regressor.fit(X,y)

svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)

# knn model 
from sklearn.neighbors import KNeighborsRegressor
knn_reg_model = KNeighborsRegressor(n_neighbors=5, weights='distance', p=2)
knn_reg_model.fit(X,y)

knn_reg_pred = knn_reg_model.predict([[6.5]])
print(knn_reg_pred)


# knn model 
from sklearn.neighbors import KNeighborsRegressor
knn_reg_model = KNeighborsRegressor(n_neighbors=2, weights='distance',p=2)
knn_reg_model.fit(X,y)


knn_reg_pred = knn_reg_model.predict([[6.5]])
print(knn_reg_pred)

#tree algorithm

from sklearn.tree import DecisionTreeRegressor
dt_regressor=DecisionTreeRegressor()
dt_regressor.fit(X,y)
dt_model_pred= dt_regressor.predict([[6.5]])
dt_model_pred

# random forest

from sklearn.ensemble import RandomForestRegressor
rf_reg =RandomForestRegressor(random_state=0,n_estimators=30)
rf_reg.fit(X,y)

rf_model_pred = rf_reg.predict([[6.5]])
print(rf_model_pred)



from sklearn.ensemble import RandomForestRegressor
rf_reg =RandomForestRegressor(random_state=0,n_estimators=40)
rf_reg.fit(X,y)

rf_model_pred = rf_reg.predict([[6.5]])
print(rf_model_pred)


from sklearn.ensemble import RandomForestRegressor
rf_reg =RandomForestRegressor(random_state=0,n_estimators=20)
rf_reg.fit(X,y)

rf_model_pred = rf_reg.predict([[6.5]])
print(rf_model_pred)



from sklearn.ensemble import RandomForestRegressor
rf_reg =RandomForestRegressor(random_state=0,n_estimators=50)
rf_reg.fit(X,y)

rf_model_pred = rf_reg.predict([[6.5]])
print(rf_model_pred)





from sklearn.ensemble import RandomForestRegressor
rf_reg =RandomForestRegressor(random_state=0,n_estimators=8)
rf_reg.fit(X,y)

rf_model_pred = rf_reg.predict([[6.5]])
print(rf_model_pred)











