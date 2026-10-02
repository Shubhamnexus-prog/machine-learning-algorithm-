# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:58:41 2026

@author: SHUBHAM
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"D:\ds 2\N_Batch -- 4.00PM -- Jun 26\3. Mar 26\7th -- REGRESSION PROJECT, POLY MODEL\poly\1.POLYNOMIAL REGRESSION/emp_sal.csv")

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


# kNN model
# k-nearest neighbour

from sklearn.neighbors import KNeighborsRegressor
knn_reg =KNeighborsRegressor()
knn_reg.fit(X,y)

knn_pred=knn_reg.predict([[6.5]])
print(knn_pred)




# knn model 

from sklearn.neighbors import KNeighborsRegressor
knn_reg_model = KNeighborsRegressor(n_neighbors=5, weights='distance', p=2)
knn_reg_model.fit(X,y)

knn_reg_pred = knn_reg_model.predict([[6.5]])
print(knn_reg_pred)