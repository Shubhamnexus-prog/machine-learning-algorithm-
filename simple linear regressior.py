import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

dataset=pd.read_csv(r'D:\ds 2\N_Batch -- 4.00PM -- Jun 26\3. Mar 26\3rd, 4th  - SLR\SIMPLE LINEAR REGRESSION/Salary_Data.csv')

x=dataset.iloc[:,:-1]
y=dataset.iloc[:,-1]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)


from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)
print(regressor)
print(regressor.get_params())

y_pred=regressor.predict(x_test)

comparision=pd.DataFrame({'Actual':y_test,'Prediction':y_pred})
print(comparision)


plt.scatter(x_test, y_test, color = 'Red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')
plt.title('Salary of employee based on experience')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()

#feture data

c_inter=regressor.intercept_
print(f'Intercept:{regressor.intercept_}')

m_coef=regressor.coef_
print(f'Cofficient:{regressor.coef_}')


y_12=m_coef*12+ c_inter
print(y_12)

y_20 =m_coef*20+c_inter
print(y_20)

#bias

bias_training = regressor.score(x_train,y_train)
print(bias_training)

variance_testing = regressor.score(x_test,y_test)
print(variance_testing)


#statistices  math----

dataset.mean()

dataset['Salary'].mean()

#median

dataset.median()
dataset['Salary'].median()

#mode

dataset.mode()
dataset['Salary'].mode


#Variance

dataset.var()

# salary variance

dataset['Salary'].var()

dataset['YearsExperience'].var()

# standarad derivstion

dataset.std()
dataset['Salary'].std()

# cofficent of variance---

from scipy.stats import variation

variation(dataset.values)

variation(dataset['Salary'])


#corelation

dataset.corr()

dataset['Salary'].corr(dataset['YearsExperience'])

#skewness

dataset.skew()

dataset['Salary'].skew()

#standard error

dataset.sem()

dataset['Salary'].sem()

#z-score--

import scipy.stats as stats

dataset.apply(stats.zscore)

stats.zscore(dataset['Salary'])

#degree of freedom

a=dataset.shape[0]
b=dataset.shape[1]
degreeoffreedom = a-b
print(degreeoffreedom)


#sum of squares regression (SSR)

y_mean=np.mean(y)
SSR=np.sum((y_pred-y_mean)**2)
print(SSR)

#SSE

y=y[0:6]
SSE=np.sum((y-y_pred)**2)
print(SSE)

#SST

mean_total=np.mean(dataset.values)
SST=np.sum((dataset.values-mean_total)**2)
print(SST) 

# R2

r_square=1-SSR/SST
print(r_square)



# pickle

import pickle
filename='linear_regression_model.pkl'
with open(filename,'wb')as file:
    pickle.dump(regressor,file)
print('model has been pickled and saved as linear_regression_model.pkl')    

