# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 10:05:19 2026

@author: SHUBHAM
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"D:\ds 2\N_Batch -- 4.00PM -- Jun 26\3. Mar 26\7th -- REGRESSION PROJECT, POLY MODEL\poly\1.POLYNOMIAL REGRESSION/emp_sal.csv")

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values




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
svr_regressor = SVR(kernel='poly',degree = 6,gamma = 'auto',C=3.0,coef0=2.0 )
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

















