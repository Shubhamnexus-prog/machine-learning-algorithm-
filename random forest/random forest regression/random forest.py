# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 12:47:02 2026

@author: SHUBHAM
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"D:\ds 2\N_Batch -- 4.00PM -- Jun 26\3. Mar 26\7th -- REGRESSION PROJECT, POLY MODEL\poly\1.POLYNOMIAL REGRESSION/emp_sal.csv")

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


#random forest---

from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators=27,random_state=0)
rf_reg.fit(X, y) 

rf_reg_pred= rf_reg.predict([[6.5]])
rf_reg_pred


#random forest---

from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(random_state=0)
rf_reg.fit(X, y) 

rf_reg_pred= rf_reg.predict([[6.5]])
rf_reg_pred


from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators=100,random_state=0)
rf_reg.fit(X, y) 

rf_reg_pred= rf_reg.predict([[6.5]])
rf_reg_pred

from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators=15)
rf_reg.fit(X, y) 

rf_reg_pred= rf_reg.predict([[6.5]])
rf_reg_pred



from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators=45,random_state=0,max_depth=None,max_samples=5,min_samples_leaf=2)
rf_reg.fit(X, y) 

rf_reg_pred= rf_reg.predict([[6.5]])
rf_reg_pred

