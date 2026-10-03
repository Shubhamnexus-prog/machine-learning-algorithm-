# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 16:30:59 2026

@author: SHUBHAM
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"D:\ds 2\N_Batch -- 4.00PM -- Jun 26\3. Mar 26\7th -- REGRESSION PROJECT, POLY MODEL\poly\1.POLYNOMIAL REGRESSION/emp_sal.csv")

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# linear model  -- linear algor ( degree - 1)

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# polynomial model  ( bydefeaut degree - 2)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures()
X_poly = poly_reg.fit_transform(X)

poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)



# polynomial model  ( bydefeaut degree - 3)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=3)
X_poly = poly_reg.fit_transform(X)

poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)


# polynomial model  ( bydefeaut degree - 4)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)

poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)


# polynomial model  ( bydefeaut degree - 5)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=5)
X_poly = poly_reg.fit_transform(X)

poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# polynomial model  ( bydefeaut degree - 6)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=6)
X_poly = poly_reg.fit_transform(X)

poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)



# linear regression visualizaton 

plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Linear Regression graph')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


# poly nomial visualization 

plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Level or Salary(Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()



lin_model_pred = lin_reg.predict([[6.5]])
lin_model_pred

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
poly_model_pred



# svr model
# support vector regression



from sklearn.svm import SVR
svr_regressor = SVR(kernel='poly',degree = 4,gamma = 'auto' )
svr_regressor.fit(X,y)

svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)

from sklearn.svm import SVR
svr_regressor = SVR( )
svr_regressor.fit(X,y)

svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)

#degree-3 kernal poly

from sklearn.svm import SVR
svr_regressor = SVR(kernel='poly',degree = 3,gamma = 'scale' )
svr_regressor.fit(X,y)
svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)

from sklearn.svm import SVR
svr_regressor = SVR(kernel='poly',degree = 3,gamma = 'auto' )
svr_regressor.fit(X,y)
svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)

#degree---3 kernal linear

from sklearn.svm import SVR
svr_regressor = SVR(kernel='linear',degree = 3,gamma = 'scale' )
svr_regressor.fit(X,y)

svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)


from sklearn.svm import SVR
svr_regressor = SVR(kernel='linear',degree = 3,gamma = 'auto' )
svr_regressor.fit(X,y)
print(svr_model_pred)

#degree--3 kernal--rbf

from sklearn.svm import SVR
svr_regressor = SVR(kernel='rbf',degree = 3,gamma = 'scale' )
svr_regressor.fit(X,y)
svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)

from sklearn.svm import SVR
svr_regressor = SVR(kernel='rbf',degree = 3,gamma = 'auto' )
svr_regressor.fit(X,y)
svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)

#degree--3  kernal sigmoid

from sklearn.svm import SVR
svr_regressor = SVR(kernel='sigmoid',degree = 3,gamma = 'scale' )
svr_regressor.fit(X,y)
svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)

from sklearn.svm import SVR
svr_regressor = SVR(kernel='sigmoid',degree = 3,gamma = 'auto' )
svr_regressor.fit(X,y)
svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)


#degree--4 karnal poly


from sklearn.svm import SVR
svr_regressor = SVR(kernel='poly',degree = 4,gamma = 'scale' )
svr_regressor.fit(X,y)
svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)

from sklearn.svm import SVR
svr_regressor = SVR(kernel='poly',degree = 4,gamma = 'auto' )
svr_regressor.fit(X,y)
svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)

#degree---4 kernal linear

from sklearn.svm import SVR
svr_regressor = SVR(kernel='linear',degree = 4,gamma = 'scale' )
svr_regressor.fit(X,y)

svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)


from sklearn.svm import SVR
svr_regressor = SVR(kernel='linear',degree = 4,gamma = 'auto' )
svr_regressor.fit(X,y)
print(svr_model_pred)

#degree--4 kernal--rbf

from sklearn.svm import SVR
svr_regressor = SVR(kernel='rbf',degree = 4,gamma = 'scale' )
svr_regressor.fit(X,y)
svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)

from sklearn.svm import SVR
svr_regressor = SVR(kernel='rbf',degree = 4,gamma = 'auto' )
svr_regressor.fit(X,y)
svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)

#degree--4  kernal sigmoid

from sklearn.svm import SVR
svr_regressor = SVR(kernel='sigmoid',degree = 4,gamma = 'scale' )
svr_regressor.fit(X,y)
svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)

from sklearn.svm import SVR
svr_regressor = SVR(kernel='sigmoid',degree = 4,gamma = 'auto' )
svr_regressor.fit(X,y)
svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)





#degree--5 karnal poly


from sklearn.svm import SVR
svr_regressor = SVR(kernel='poly',degree = 5,gamma = 'scale' )
svr_regressor.fit(X,y)
svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)

from sklearn.svm import SVR
svr_regressor = SVR(kernel='poly',degree = 5,gamma = 'auto' )
svr_regressor.fit(X,y)
svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)

#degree---5 kernal linear

from sklearn.svm import SVR
svr_regressor = SVR(kernel='linear',degree = 5,gamma = 'scale' )
svr_regressor.fit(X,y)

svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)


from sklearn.svm import SVR
svr_regressor = SVR(kernel='linear',degree = 5,gamma = 'auto' )
svr_regressor.fit(X,y)
print(svr_model_pred)

#degree--5 kernal--rbf

from sklearn.svm import SVR
svr_regressor = SVR(kernel='rbf',degree = 5,gamma = 'scale' )
svr_regressor.fit(X,y)
svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)

from sklearn.svm import SVR
svr_regressor = SVR(kernel='rbf',degree = 5,gamma = 'auto' )
svr_regressor.fit(X,y)
svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)

#degree--5  kernal sigmoid

from sklearn.svm import SVR
svr_regressor = SVR(kernel='sigmoid',degree = 5,gamma = 'scale' )
svr_regressor.fit(X,y)
svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)

from sklearn.svm import SVR
svr_regressor = SVR(kernel='sigmoid',degree = 5,gamma = 'auto' )
svr_regressor.fit(X,y)
svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)


from sklearn.svm import SVR
svr_regressor = SVR(kernel='poly',degree = 6,gamma = 'auto',C=3.0,coef0=1.0 )
svr_regressor.fit(X,y)
svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)


#svr show graph visulazation

plt.scatter(X, y, color='red')
plt.plot(X, svr_regressor.predict(X), color='blue')
plt.title('Level or Salary (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show() 



#knn---k nerest nighbors-----------------

# knn model 


from sklearn.neighbors import KNeighborsRegressor
knn_reg_model = KNeighborsRegressor()
knn_reg_model.fit(X,y)

knn_reg_pred = knn_reg_model.predict([[6.5]])
print(knn_reg_pred)



from sklearn.neighbors import KNeighborsRegressor
knn_reg_model = KNeighborsRegressor(n_neighbors=4, weights='distance', p=1,algorithm='brute')
knn_reg_model.fit(X,y)

knn_reg_pred = knn_reg_model.predict([[6.5]])
print(knn_reg_pred)



from sklearn.neighbors import KNeighborsRegressor
knn_reg_model = KNeighborsRegressor(n_neighbors=2, weights='uniform', p=2,algorithm='auto')
knn_reg_model.fit(X,y)

knn_reg_pred = knn_reg_model.predict([[6.5]])
print(knn_reg_pred)



from sklearn.neighbors import KNeighborsRegressor
knn_reg_model = KNeighborsRegressor(n_neighbors=4, weights='uniform')
knn_reg_model.fit(X,y)

knn_reg_pred = knn_reg_model.predict([[6.5]])
print(knn_reg_pred)



from sklearn.neighbors import KNeighborsRegressor
knn_reg_model = KNeighborsRegressor(n_neighbors=5, weights='distance', p=1)
knn_reg_model.fit(X,y)

knn_reg_pred = knn_reg_model.predict([[6.5]])
print(knn_reg_pred)


from sklearn.neighbors import KNeighborsRegressor
knn_reg_model = KNeighborsRegressor(n_neighbors=4, weights='distance', p=1)
knn_reg_model.fit(X,y)

knn_reg_pred = knn_reg_model.predict([[6.5]])
print(knn_reg_pred)



# decission tree--------

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



#xgboost

import xgboost as xg

xgb_r = xg.XGBRegressor(
    objective='reg:squarederror',
    n_estimators=4
)

xgb_r.fit(X, y)

xgb_reg_pred = xgb_r.predict([[6.5]])
print(xgb_reg_pred)





 
























