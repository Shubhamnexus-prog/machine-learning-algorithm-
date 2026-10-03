# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 12:22:53 2026

@author: SHUBHAM
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"D:\ds 2\N_Batch -- 4.00PM -- Jun 26\3. Mar 26\7th -- REGRESSION PROJECT, POLY MODEL\poly\1.POLYNOMIAL REGRESSION/emp_sal.csv")

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# decision tree---


from sklearn.tree import DecisionTreeRegressor
dt_reg = DecisionTreeRegressor()   
dt_reg.fit(X, y)

dt_reg_pred= dt_reg.predict([[6.5]])
dt_reg_pred


from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(criterion = 'absolute_error',splitter = 'random')
dt_reg.fit(X, y)

dt_reg_pred= dt_reg.predict([[6.5]])
dt_reg_pred

#square error---- 

from sklearn.tree import DecisionTreeRegressor
dt_reg = DecisionTreeRegressor(criterion='squared_error',splitter='best')   
dt_reg.fit(X, y)

dt_reg_pred= dt_reg.predict([[6.5]])
dt_reg_pred


from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(criterion = 'squared_error',splitter = 'random=12')
dt_reg.fit(X, y)

dt_reg_pred= dt_reg.predict([[6.5]])
dt_reg_pred

#splitter

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(criterion = 'poisson',splitter = 'random=12')
dt_reg.fit(X, y)

dt_reg_pred= dt_reg.predict([[6.5]])
dt_reg_pred


from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(criterion = 'poisson',splitter = 'best=12')
dt_reg.fit(X, y)

dt_reg_pred= dt_reg.predict([[6.5]])
dt_reg_pred


#max_depth---


from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(criterion = 'poisson',splitter = 'random=12',max_depth=int)
dt_reg.fit(X, y)

dt_reg_pred= dt_reg.predict([[6.5]])
dt_reg_pred



from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(criterion = 'poisson',splitter = 'random=12',max_depth=None)
dt_reg.fit(X, y)

dt_reg_pred= dt_reg.predict([[6.5]])
dt_reg_pred

